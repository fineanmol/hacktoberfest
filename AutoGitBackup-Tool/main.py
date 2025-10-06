#!/usr/bin/env python3
"""
Auto Git Backup Tool
Main launcher script that provides both GUI setup and service execution
"""

import os
import sys
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config_manager import ConfigManager
from backup_service import AutoGitBackupService

class ConfigGUI:
    """Simple GUI for initial configuration setup"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto Git Backup - Configuration")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        self.config_manager = ConfigManager()
        self.setup_ui()
        self.load_current_config()

    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="Auto Git Backup Configuration", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Folder path
        ttk.Label(main_frame, text="Project Folder:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.folder_var = tk.StringVar()
        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        folder_frame.columnconfigure(0, weight=1)

        ttk.Entry(folder_frame, textvariable=self.folder_var, width=50).grid(row=0, column=0, sticky=(tk.W, tk.E))
        ttk.Button(folder_frame, text="Browse", command=self.browse_folder).grid(row=0, column=1, padx=(5, 0))

        # Git remote
        ttk.Label(main_frame, text="Git Remote URL:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.remote_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.remote_var, width=60).grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Commit interval
        ttk.Label(main_frame, text="Commit Interval (seconds):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.interval_var = tk.StringVar(value="300")
        interval_frame = ttk.Frame(main_frame)
        interval_frame.grid(row=3, column=1, sticky=tk.W, pady=5)
        ttk.Entry(interval_frame, textvariable=self.interval_var, width=10).grid(row=0, column=0)
        ttk.Label(interval_frame, text="(minimum: 10)").grid(row=0, column=1, padx=(10, 0))

        # Log level
        ttk.Label(main_frame, text="Log Level:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.log_level_var = tk.StringVar(value="INFO")
        log_combo = ttk.Combobox(main_frame, textvariable=self.log_level_var, 
                                values=["DEBUG", "INFO", "WARNING", "ERROR"], 
                                state="readonly", width=10)
        log_combo.grid(row=4, column=1, sticky=tk.W, pady=5)

        # Information text
        info_text = tk.Text(main_frame, height=8, width=70, wrap=tk.WORD)
        info_text.grid(row=5, column=0, columnspan=3, pady=(20, 10), sticky=(tk.W, tk.E, tk.N, tk.S))

        info_content = """Setup Instructions:
1. Select your project folder (the folder you want to backup)
2. Enter your Git remote URL (e.g., git@github.com:username/repo.git or https://github.com/username/repo.git)
3. Set the commit interval (how often to check for changes and backup)
4. Click 'Save & Start' to save configuration and start the backup service

Note: Make sure you have:
- Git installed and configured
- SSH keys setup for your Git remote (if using SSH)
- Write permissions to the selected folder"""

        info_text.insert(tk.END, info_content)
        info_text.config(state=tk.DISABLED)

        # Scrollbar for text
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=info_text.yview)
        scrollbar.grid(row=5, column=3, sticky=(tk.N, tk.S), pady=(20, 10))
        info_text.configure(yscrollcommand=scrollbar.set)

        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=20)

        ttk.Button(button_frame, text="Save Configuration", command=self.save_config).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save & Start Service", command=self.save_and_start).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Start Service Only", command=self.start_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # Configure row weights for resizing
        main_frame.rowconfigure(5, weight=1)

    def browse_folder(self):
        """Open folder browser dialog"""
        folder = filedialog.askdirectory(title="Select Project Folder")
        if folder:
            self.folder_var.set(folder)

    def load_current_config(self):
        """Load current configuration into the form"""
        config = self.config_manager.config

        self.folder_var.set(config.get('folder_path', ''))
        self.remote_var.set(config.get('git_remote', ''))
        self.interval_var.set(str(config.get('commit_interval', 300)))
        self.log_level_var.set(config.get('log_level', 'INFO'))

    def validate_config(self) -> tuple[bool, str]:
        """Validate the configuration"""
        folder_path = self.folder_var.get().strip()
        remote_url = self.remote_var.get().strip()

        if not folder_path:
            return False, "Please select a project folder"

        if not os.path.exists(folder_path):
            return False, f"Folder does not exist: {folder_path}"

        if not remote_url:
            return False, "Please enter a Git remote URL"

        try:
            interval = int(self.interval_var.get())
            if interval < 10:
                return False, "Commit interval must be at least 10 seconds"
        except ValueError:
            return False, "Commit interval must be a valid number"

        return True, "Configuration is valid"

    def save_config(self):
        """Save the configuration"""
        is_valid, message = self.validate_config()
        if not is_valid:
            messagebox.showerror("Configuration Error", message)
            return False

        try:
            config = {
                'folder_path': self.folder_var.get().strip(),
                'git_remote': self.remote_var.get().strip(),
                'commit_interval': int(self.interval_var.get()),
                'log_level': self.log_level_var.get(),
                'max_log_size': 10485760
            }

            self.config_manager.config = config
            self.config_manager.save_config()

            messagebox.showinfo("Success", "Configuration saved successfully!")
            return True

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {str(e)}")
            return False

    def save_and_start(self):
        """Save configuration and start service"""
        if self.save_config():
            self.start_service()

    def start_service(self):
        """Start the backup service"""
        try:
            # Validate configuration first
            is_valid, message = self.config_manager.validate_config()
            if not is_valid:
                messagebox.showerror("Configuration Error", 
                                   f"Please fix configuration first: {message}")
                return

            # Hide the configuration window
            self.root.withdraw()

            # Start the service
            service = AutoGitBackupService()
            service.run()

        except Exception as e:
            messagebox.showerror("Service Error", f"Failed to start service: {str(e)}")
            self.root.deiconify()  # Show window again on error

    def run(self):
        """Run the GUI"""
        self.root.mainloop()

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--service":
            # Run as service without GUI
            service = AutoGitBackupService()
            return service.run()
        elif sys.argv[1] == "--help":
            print("Auto Git Backup Tool")
            print("Usage:")
            print("  python main.py          - Run with configuration GUI")
            print("  python main.py --service - Run as service without GUI")
            print("  python main.py --help   - Show this help message")
            return 0

    # Check if configuration exists
    config_manager = ConfigManager()
    if (config_manager.get('folder_path') and 
        config_manager.get('git_remote') and
        os.path.exists("config.json")):

        # Configuration exists, ask user what to do
        try:
            import tkinter.messagebox as msgbox
            root = tk.Tk()
            root.withdraw()  # Hide root window

            choice = msgbox.askyesnocancel(
                "Auto Git Backup",
                "Configuration found. What would you like to do?\n\n"
                "Yes - Start service immediately\n"
                "No - Open configuration window\n"
                "Cancel - Exit"
            )

            root.destroy()

            if choice is True:
                # Start service directly
                service = AutoGitBackupService()
                return service.run()
            elif choice is False:
                # Open configuration GUI
                app = ConfigGUI()
                app.run()
                return 0
            else:
                # User cancelled
                return 0

        except ImportError:
            # Fallback if tkinter is not available
            service = AutoGitBackupService()
            return service.run()
    else:
        # No configuration, open GUI
        app = ConfigGUI()
        app.run()
        return 0

if __name__ == "__main__":
    sys.exit(main())
