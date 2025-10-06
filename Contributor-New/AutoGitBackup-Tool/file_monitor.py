import time
import logging
from pathlib import Path
from typing import Callable
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent

class BackupEventHandler(FileSystemEventHandler):
    """Custom event handler for file system changes"""

    def __init__(self, callback: Callable, logger: logging.Logger):
        super().__init__()
        self.callback = callback
        self.logger = logger
        self.last_event_time = 0
        self.debounce_time = 1.0  # Debounce events within 1 second

    def _should_ignore_path(self, path: str) -> bool:
        """Check if path should be ignored"""
        ignore_patterns = [
            '.git',
            '__pycache__',
            '.pyc',
            '.tmp',
            '.temp',
            '~$',
            '.DS_Store',
            'Thumbs.db'
        ]

        path_lower = path.lower()
        for pattern in ignore_patterns:
            if pattern in path_lower:
                return True

        return False

    def _handle_event(self, event: FileSystemEvent):
        """Handle file system event with debouncing"""
        if event.is_directory:
            return

        if self._should_ignore_path(event.src_path):
            return

        current_time = time.time()
        if current_time - self.last_event_time < self.debounce_time:
            return

        self.last_event_time = current_time

        event_type = type(event).__name__
        self.logger.debug(f"File event: {event_type} - {event.src_path}")

        # Call the callback function
        self.callback()

    def on_created(self, event):
        self._handle_event(event)

    def on_modified(self, event):
        self._handle_event(event)

    def on_deleted(self, event):
        self._handle_event(event)

    def on_moved(self, event):
        self._handle_event(event)

class FileMonitor:
    """Monitors file system changes using watchdog"""

    def __init__(self, folder_path: str, callback: Callable, logger: logging.Logger):
        self.folder_path = Path(folder_path).resolve()
        self.callback = callback
        self.logger = logger
        self.observer = None
        self.event_handler = None
        self.is_monitoring = False

    def start_monitoring(self) -> bool:
        """Start monitoring the specified folder"""
        if self.is_monitoring:
            self.logger.warning("Monitoring is already active")
            return True

        try:
            if not self.folder_path.exists():
                self.logger.error(f"Folder does not exist: {self.folder_path}")
                return False

            self.event_handler = BackupEventHandler(self.callback, self.logger)
            self.observer = Observer()
            self.observer.schedule(
                self.event_handler,
                str(self.folder_path),
                recursive=True
            )

            self.observer.start()
            self.is_monitoring = True

            self.logger.info(f"Started monitoring folder: {self.folder_path}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to start monitoring: {str(e)}")
            return False

    def stop_monitoring(self):
        """Stop monitoring the folder"""
        if not self.is_monitoring:
            return

        try:
            if self.observer:
                self.observer.stop()
                self.observer.join(timeout=5.0)
                self.observer = None

            self.event_handler = None
            self.is_monitoring = False

            self.logger.info("Stopped file monitoring")

        except Exception as e:
            self.logger.error(f"Error stopping monitor: {str(e)}")

    def is_active(self) -> bool:
        """Check if monitoring is currently active"""
        return self.is_monitoring and self.observer and self.observer.is_alive()
