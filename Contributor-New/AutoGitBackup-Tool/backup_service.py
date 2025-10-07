import os
import sys
import time
import signal
import logging
import threading
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional

from config_manager import ConfigManager
from git_manager import GitManager
from file_monitor import FileMonitor
from system_tray import SystemTrayApp

class AutoGitBackupService:
    """Main service class for the Auto Git Backup tool"""

    def __init__(self):
        # Initialize configuration
        self.config_manager = ConfigManager()

        # Setup logging
        self.logger = self._setup_logging()

        # Initialize components
        self.git_manager: Optional[GitManager] = None
        self.file_monitor: Optional[FileMonitor] = None
        self.system_tray: Optional[SystemTrayApp] = None

        # State management
        self.is_active = False
        self.is_running = True
        self.last_backup_time = datetime.now()
        self.last_commit = None
        self.last_error = None
        self.pending_changes = False

        # Threading
        self.backup_thread: Optional[threading.Thread] = None
        self.tray_thread: Optional[threading.Thread] = None
        self.shutdown_event = threading.Event()

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        log_level = self.config_manager.get('log_level', 'INFO')
        max_log_size = self.config_manager.get('max_log_size', 10485760)  # 10MB

        # Create logs directory
        logs_dir = Path('logs')
        logs_dir.mkdir(exist_ok=True)

        # Configure logger
        logger = logging.getLogger('AutoGitBackup')
        logger.setLevel(getattr(logging, log_level))

        # Remove existing handlers
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        # File handler with rotation
        log_file = logs_dir / 'backup.log'

        # Simple file handler (you could use RotatingFileHandler for production)
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(getattr(logging, log_level))

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

    def _signal_handler(self, signum, frame):
        """Handle system signals for graceful shutdown"""
        self.logger.info(f"Received signal {signum}, shutting down...")
        self.shutdown()

    def initialize(self) -> bool:
        """Initialize all components"""
        self.logger.info("Initializing Auto Git Backup Service...")

        # Validate configuration
        is_valid, error_msg = self.config_manager.validate_config()
        if not is_valid:
            self.logger.error(f"Configuration validation failed: {error_msg}")
            return False

        # Initialize Git manager
        folder_path = self.config_manager.get('folder_path')
        git_remote = self.config_manager.get('git_remote')

        self.git_manager = GitManager(folder_path, git_remote, self.logger)
        success, msg = self.git_manager.initialize_repository()
        if not success:
            self.logger.error(f"Git initialization failed: {msg}")
            return False

        # Initialize file monitor
        self.file_monitor = FileMonitor(
            folder_path,
            self._on_file_change,
            self.logger
        )

        # Initialize system tray
        self.system_tray = SystemTrayApp(
            self.start_monitoring,
            self.pause_monitoring,
            self.shutdown,
            self.get_status,
            self.logger
        )

        self.logger.info("Service initialized successfully")
        return True

    def _on_file_change(self):
        """Callback for file system changes"""
        self.logger.debug("File change detected, marking for backup")
        self.pending_changes = True

    def start_monitoring(self):
        """Start the backup monitoring"""
        if self.is_active:
            self.logger.info("Monitoring is already active")
            return

        self.logger.info("Starting backup monitoring...")

        # Start file monitoring
        if self.file_monitor and self.file_monitor.start_monitoring():
            self.is_active = True
            self.last_error = None

            # Start backup thread
            self.backup_thread = threading.Thread(target=self._backup_loop, daemon=True)
            self.backup_thread.start()

            self.logger.info("Backup monitoring started successfully")
        else:
            self.last_error = "Failed to start file monitoring"
            self.logger.error(self.last_error)

    def pause_monitoring(self):
        """Pause the backup monitoring"""
        if not self.is_active:
            self.logger.info("Monitoring is already paused")
            return

        self.logger.info("Pausing backup monitoring...")
        self.is_active = False

        # Stop file monitoring
        if self.file_monitor:
            self.file_monitor.stop_monitoring()

        self.logger.info("Backup monitoring paused")

    def _backup_loop(self):
        """Main backup loop running in a separate thread"""
        commit_interval = self.config_manager.get('commit_interval', 300)

        while self.is_active and self.is_running:
            try:
                current_time = datetime.now()

                # Check if it's time for a scheduled backup or if there are pending changes
                time_for_backup = (current_time - self.last_backup_time).total_seconds() >= commit_interval

                if (self.pending_changes and time_for_backup) or \
                   (self.pending_changes and self.git_manager.has_changes()):

                    self._perform_backup()

                # Sleep for a short interval
                time.sleep(5)

            except Exception as e:
                self.last_error = f"Backup loop error: {str(e)}"
                self.logger.error(self.last_error)
                time.sleep(10)  # Wait longer on error

    def _perform_backup(self):
        """Perform the actual backup operation"""
        try:
            self.logger.info("Starting backup operation...")

            # Check for changes
            if not self.git_manager.has_changes():
                self.logger.debug("No changes detected, skipping backup")
                self.pending_changes = False
                return

            # Commit changes
            success, msg = self.git_manager.commit_changes()
            if not success:
                self.last_error = f"Commit failed: {msg}"
                self.logger.error(self.last_error)
                return

            self.last_commit = self.git_manager.get_last_commit_info()

            # Push to remote
            success, msg = self.git_manager.push_changes()
            if not success:
                self.last_error = f"Push failed: {msg}"
                self.logger.warning(self.last_error)
                # Note: We don't return here, as local commit succeeded
            else:
                self.last_error = None  # Clear any previous errors
                self.logger.info("Backup completed successfully")

            self.last_backup_time = datetime.now()
            self.pending_changes = False

        except Exception as e:
            self.last_error = f"Backup error: {str(e)}"
            self.logger.error(self.last_error)

    def get_status(self) -> Dict[str, Any]:
        """Get current service status"""
        return {
            'is_active': self.is_active,
            'is_running': self.is_running,
            'last_commit': self.last_commit,
            'last_error': self.last_error,
            'last_backup_time': self.last_backup_time.isoformat() if self.last_backup_time else None,
            'folder_path': self.config_manager.get('folder_path'),
            'git_remote': self.config_manager.get('git_remote')
        }

    def run(self):
        """Main run method"""
        if not self.initialize():
            self.logger.error("Failed to initialize service")
            return 1

        try:
            self.logger.info("Starting Auto Git Backup Service...")

            # Start system tray in a separate thread
            self.tray_thread = self.system_tray.run_in_thread()

            # Auto-start monitoring
            self.start_monitoring()

            # Main loop
            while self.is_running and not self.shutdown_event.is_set():
                # Update tray menu periodically
                if self.system_tray:
                    self.system_tray.update_menu()

                # Wait for shutdown signal
                self.shutdown_event.wait(timeout=30)

            return 0

        except KeyboardInterrupt:
            self.logger.info("Received keyboard interrupt")
            return 0
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            return 1
        finally:
            self._cleanup()

    def shutdown(self):
        """Shutdown the service gracefully"""
        self.logger.info("Shutting down Auto Git Backup Service...")

        self.is_running = False
        self.shutdown_event.set()

        # Pause monitoring
        self.pause_monitoring()

        # Stop system tray
        if self.system_tray:
            self.system_tray.stop_tray()

        self.logger.info("Service shutdown completed")

    def _cleanup(self):
        """Cleanup resources"""
        if self.file_monitor:
            self.file_monitor.stop_monitoring()

        if self.system_tray:
            self.system_tray.stop_tray()

def main():
    """Main entry point"""
    service = AutoGitBackupService()
    return service.run()

if __name__ == "__main__":
    sys.exit(main())
