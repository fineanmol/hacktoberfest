# Modern File Manager

A comprehensive file manager application built with Python and Tkinter, featuring a modern interface and advanced file operations.

## Features

### Core File Operations
- **Navigation**: Browse directories with back/forward buttons and address bar
- **File Management**: Copy, cut, paste, delete, rename files and folders
- **File Creation**: Create new files and folders
- **File Opening**: Open files with default applications
- **Properties**: View detailed file properties and metadata

### Advanced Features
- **Dual Panel Interface**: Tree view for navigation and detailed file list
- **File Search**: Search for files and folders by name
- **File Properties**: Detailed file information including size, dates, permissions
- **Context Menu**: Right-click context menu for quick operations
- **Keyboard Shortcuts**: Common keyboard shortcuts for file operations
- **Cross-Platform**: Works on Windows, macOS, and Linux

### User Interface
- **Modern Design**: Clean, intuitive interface with professional styling
- **Responsive Layout**: Adapts to different window sizes
- **Status Bar**: Shows current directory information and file counts
- **Toolbar**: Quick access to common operations
- **Address Bar**: Direct path navigation

## Installation

### Requirements
- Python 3.6 or higher
- Tkinter (usually included with Python)
- Standard library modules only

### Installation Steps
1. Clone or download the project
2. Navigate to the project directory
3. Run the application:

```bash
python file_manager.py
```

## Usage

### Basic Navigation
- **Double-click** folders to enter them
- **Double-click** files to open them
- Use **back/forward** buttons for navigation history
- Use **up** button to go to parent directory
- Use **home** button to go to home directory

### File Operations
- **Select files** by clicking on them
- **Right-click** for context menu
- Use **Ctrl+A** to select all files
- **Copy/Cut** files for moving between locations
- **Paste** files in current directory

### Advanced Features
- **Search**: Click search button to find files by name
- **Properties**: Right-click and select "Properties" for file details
- **New Folder/File**: Use toolbar buttons to create new items
- **Refresh**: Update directory contents

## File Operations

### Supported Operations
- **Copy**: Copy files to clipboard
- **Cut**: Cut files for moving
- **Paste**: Paste files from clipboard
- **Delete**: Delete selected files (with confirmation)
- **Rename**: Rename files and folders
- **Create**: Create new files and folders
- **Open**: Open files with default application
- **Properties**: View detailed file information

### File Types Supported
- All file types are supported
- Automatic file type detection
- MIME type recognition
- File size formatting
- Date/time display

## Interface Components

### Toolbar
- **Navigation**: Back, Forward, Up, Home buttons
- **File Operations**: New Folder, New File, Copy, Cut, Paste, Delete
- **Tools**: Refresh, Search, Properties

### Address Bar
- Shows current directory path
- Direct path entry and navigation
- "Go" button for path navigation

### Tree Panel
- Hierarchical folder structure
- Quick navigation to parent directories
- Visual folder hierarchy

### File Panel
- Detailed file listing with columns:
  - **Name**: File/folder name
  - **Size**: File size (formatted)
  - **Modified**: Last modification date
  - **Type**: File type or MIME type

### Status Bar
- Current directory information
- File and folder counts
- Operation status messages

## Keyboard Shortcuts

- **Ctrl+A**: Select all files
- **F5**: Refresh directory
- **Enter**: Open selected file/folder
- **Delete**: Delete selected files
- **F2**: Rename selected file
- **Ctrl+C**: Copy selected files
- **Ctrl+X**: Cut selected files
- **Ctrl+V**: Paste files

## File Properties

The properties dialog shows:
- **Basic Info**: Name, path, type, size
- **Dates**: Created, modified, accessed
- **Permissions**: Read, write, execute permissions
- **File Type**: MIME type and description
- **Hash**: MD5 hash for files

## Search Functionality

- **Real-time Search**: Search files and folders by name
- **Case-insensitive**: Search is not case-sensitive
- **Recursive**: Searches in subdirectories
- **Results Display**: Shows matching files with full paths
- **Background Search**: Non-blocking search operation

## Cross-Platform Support

### Windows
- Uses `os.startfile()` for opening files
- Native Windows file associations
- Windows-style path handling

### macOS
- Uses `open` command for file opening
- macOS file associations
- Unix-style path handling

### Linux
- Uses `xdg-open` for file opening
- Linux file associations
- Unix-style path handling

## Customization

### Themes
The application uses Tkinter's built-in themes:
- **clam**: Default modern theme
- **alt**: Alternative theme
- **classic**: Classic theme
- **default**: System default theme

### Colors
- Background: Light gray (#f0f0f0)
- Tree view: White background
- Headers: Light gray (#e0e0e0)
- Text: Black foreground

## Error Handling

The application includes comprehensive error handling:
- **Permission Errors**: Graceful handling of permission denied
- **File Not Found**: Proper error messages for missing files
- **Invalid Paths**: Validation of user-entered paths
- **Operation Failures**: Clear error messages for failed operations

## Performance

### Optimizations
- **Lazy Loading**: Tree view loads on demand
- **Background Operations**: Search runs in separate thread
- **Efficient Updates**: Only updates changed parts of interface
- **Memory Management**: Proper cleanup of resources

### Large Directories
- Handles directories with many files
- Efficient file listing
- Responsive interface even with large file counts

## Contributing

Areas for improvement:
- Add file compression/decompression
- Implement file preview functionality
- Add file comparison features
- Create plugin system for extensions
- Add file synchronization capabilities
- Implement file tagging system
- Add file encryption/decryption
- Create file backup functionality

## Technical Details

### Architecture
- **MVC Pattern**: Model-View-Controller separation
- **Event-Driven**: Tkinter event handling
- **Threading**: Background operations for responsiveness
- **Path Handling**: Uses `pathlib.Path` for modern path operations

### Dependencies
- **Python 3.6+**: Modern Python features
- **Tkinter**: GUI framework
- **pathlib**: Modern path handling
- **threading**: Background operations
- **hashlib**: File hashing
- **mimetypes**: File type detection

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Common Issues
1. **Permission Denied**: Ensure you have proper file permissions
2. **File Not Opening**: Check if default application is set
3. **Slow Performance**: Large directories may take time to load
4. **Search Not Working**: Ensure you have read permissions for directories

### System Requirements
- **RAM**: Minimum 512MB, recommended 1GB+
- **Storage**: Minimal disk space required
- **OS**: Windows 7+, macOS 10.9+, Linux (any modern distribution)
- **Python**: 3.6 or higher
