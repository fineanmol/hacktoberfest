# Auto Git Backup Tool

A complete Windows-compatible Python tool that automatically monitors a project folder and backs up changes to a remote Git repository.

## Features

- **Automatic File Monitoring**: Watches for file changes (add, modify, delete) in real-time
- **Git Integration**: Automatically stages, commits, and pushes changes to remote repository
- **System Tray Interface**: Runs silently in background with Start, Pause, and Exit controls
- **Comprehensive Logging**: Logs all operations to file with configurable log levels
- **Error Handling**: Robust error handling for network issues, Git failures, etc.
- **Configuration Management**: Easy setup through JSON config file or GUI
- **Background Service**: Runs as a Windows background service

## Installation

### Prerequisites
- Python 3.10 or higher
- Git installed and configured
- SSH keys configured for your Git remote (recommended)

### Quick Setup
1. Extract all files to a folder
2. Run `setup.bat` to install dependencies
3. Run `python main.py` to start with configuration GUI

### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Configuration

The tool uses a `config.json` file with the following settings:

```json
{
    "folder_path": "C:\\path\\to\\your\\project",
    "git_remote": "git@github.com:username/repository.git",
    "commit_interval": 300,
    "log_level": "INFO",
    "max_log_size": 10485760
}
```

### Configuration Options

- **folder_path**: Full path to the folder you want to monitor and backup
- **git_remote**: Git remote URL (SSH or HTTPS)
- **commit_interval**: Minimum seconds between commits (default: 300)
- **log_level**: Logging level (DEBUG, INFO, WARNING, ERROR)
- **max_log_size**: Maximum log file size in bytes (default: 10MB)

## Usage

### First Time Setup
1. Run `python main.py`
2. Configure your project folder and Git remote URL
3. Click "Save & Start Service"
4. The tool will appear in your system tray

### Running as Service
```bash
# Start with GUI configuration
python main.py

# Start directly as service (config must exist)
python main.py --service

# Show help
python main.py --help
```

### System Tray Controls
- **Right-click** the tray icon to access the menu
- **Start**: Begin monitoring and automatic backups
- **Pause**: Stop monitoring (keeps the tool running)
- **Exit**: Completely shut down the tool

## File Structure

```
auto-git-backup/
├── main.py                 # Main launcher and configuration GUI
├── backup_service.py       # Core backup service
├── config_manager.py       # Configuration management
├── git_manager.py          # Git operations handler
├── file_monitor.py         # File system monitoring
├── system_tray.py          # System tray interface
├── config.json             # Configuration file
├── requirements.txt        # Python dependencies
├── setup.bat              # Windows setup script
├── run.bat                # Windows run script
├── test_installation.py   # Installation test script
└── logs/                  # Log files directory
    └── backup.log         # Main log file
```

## How It Works

1. **File Monitoring**: Uses `watchdog` library to monitor file system changes
2. **Change Detection**: Detects file additions, modifications, and deletions
3. **Git Operations**: Uses `GitPython` to handle staging, committing, and pushing
4. **Debouncing**: Prevents excessive commits by batching changes
5. **Error Recovery**: Continues running even if individual operations fail
6. **Logging**: Records all operations for debugging and monitoring

## Dependencies

- **watchdog**: File system monitoring
- **GitPython**: Git repository operations  
- **pystray**: System tray functionality
- **Pillow**: Image handling for tray icons
- **tkinter**: Configuration GUI (included with Python)

## Troubleshooting

### Common Issues

**Git Authentication Errors**
- Ensure SSH keys are set up for your Git remote
- For HTTPS, you may need personal access tokens
- Test Git operations manually first: `git clone <your-remote-url>`

**File Monitoring Not Working**
- Check that the folder path exists and is accessible
- Verify you have read/write permissions to the folder
- Check logs in `logs/backup.log` for detailed error messages

**System Tray Icon Missing**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Try running from command line to see error messages
- Check Windows notification area settings

### Testing Installation
Run the test script to verify everything is working:
```bash
python test_installation.py
```

## Quick Start Instructions

1. **Setup**: Run `setup.bat` (or `pip install -r requirements.txt`)
2. **Launch**: Run `python main.py`  
3. **Configure**: Set project folder and Git remote URL
4. **Start**: Click "Save & Start Service"
5. **Monitor**: Look for system tray icon (right-click for options)

## License

This tool is provided as-is for educational and personal use.
