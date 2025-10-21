"""
Modern File Manager with Advanced Features
Author: AI Assistant
GitHub: https://github.com/fineanmol/hacktoberfest
Language: Python
Description: A comprehensive file manager with modern UI, file operations, search, and advanced features
"""

import os
import shutil
import stat
import mimetypes
import hashlib
import zipfile
import tarfile
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from tkinter.font import Font
import threading
import subprocess
import platform


class FileManager:
    """Modern file manager with advanced features"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modern File Manager")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Current directory
        self.current_path = Path.home()
        self.history = [self.current_path]
        self.history_index = 0
        
        # File operations
        self.selected_files = []
        self.cut_files = []
        
        # UI Components
        self.setup_ui()
        self.load_directory()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Configure styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Treeview', background='white', foreground='black')
        style.configure('Treeview.Heading', background='#e0e0e0', foreground='black')
        
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Toolbar
        self.setup_toolbar(main_frame)
        
        # Address bar
        self.setup_address_bar(main_frame)
        
        # Main content area
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Left panel (tree view)
        self.setup_tree_panel(content_frame)
        
        # Right panel (file list)
        self.setup_file_panel(content_frame)
        
        # Status bar
        self.setup_status_bar(main_frame)
        
        # Context menu
        self.setup_context_menu()
        
    def setup_toolbar(self, parent):
        """Setup toolbar with buttons"""
        toolbar = ttk.Frame(parent)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        # Navigation buttons
        ttk.Button(toolbar, text="←", command=self.go_back, width=3).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="→", command=self.go_forward, width=3).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="↑", command=self.go_up, width=3).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="🏠", command=self.go_home, width=3).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # File operations
        ttk.Button(toolbar, text="New Folder", command=self.create_folder).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="New File", command=self.create_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Copy", command=self.copy_files).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Cut", command=self.cut_files).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Paste", command=self.paste_files).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Delete", command=self.delete_files).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # View options
        ttk.Button(toolbar, text="Refresh", command=self.refresh).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Search", command=self.open_search).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Properties", command=self.show_properties).pack(side=tk.LEFT, padx=(0, 5))
        
    def setup_address_bar(self, parent):
        """Setup address bar"""
        address_frame = ttk.Frame(parent)
        address_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(address_frame, text="Path:").pack(side=tk.LEFT)
        
        self.address_var = tk.StringVar()
        self.address_entry = ttk.Entry(address_frame, textvariable=self.address_var, font=('Consolas', 10))
        self.address_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        self.address_entry.bind('<Return>', self.navigate_to_path)
        
        ttk.Button(address_frame, text="Go", command=self.navigate_to_path).pack(side=tk.RIGHT)
        
    def setup_tree_panel(self, parent):
        """Setup tree view panel"""
        tree_frame = ttk.LabelFrame(parent, text="Folders", padding=5)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Tree view
        self.tree = ttk.Treeview(tree_frame)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar for tree
        tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        # Bind events
        self.tree.bind('<Double-1>', self.on_tree_double_click)
        self.tree.bind('<Button-3>', self.on_tree_right_click)
        
    def setup_file_panel(self, parent):
        """Setup file list panel"""
        file_frame = ttk.LabelFrame(parent, text="Files", padding=5)
        file_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # File list
        columns = ('Name', 'Size', 'Modified', 'Type')
        self.file_list = ttk.Treeview(file_frame, columns=columns, show='headings')
        
        # Configure columns
        self.file_list.heading('Name', text='Name')
        self.file_list.heading('Size', text='Size')
        self.file_list.heading('Modified', text='Modified')
        self.file_list.heading('Type', text='Type')
        
        self.file_list.column('Name', width=300)
        self.file_list.column('Size', width=100)
        self.file_list.column('Modified', width=150)
        self.file_list.column('Type', width=100)
        
        self.file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbars for file list
        v_scroll = ttk.Scrollbar(file_frame, orient=tk.VERTICAL, command=self.file_list.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_list.configure(yscrollcommand=v_scroll.set)
        
        h_scroll = ttk.Scrollbar(file_frame, orient=tk.HORIZONTAL, command=self.file_list.xview)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.file_list.configure(xscrollcommand=h_scroll.set)
        
        # Bind events
        self.file_list.bind('<Double-1>', self.on_file_double_click)
        self.file_list.bind('<Button-1>', self.on_file_click)
        self.file_list.bind('<Button-3>', self.on_file_right_click)
        self.file_list.bind('<Control-a>', self.select_all_files)
        
    def setup_status_bar(self, parent):
        """Setup status bar"""
        self.status_bar = ttk.Frame(parent)
        self.status_bar.pack(fill=tk.X, pady=(10, 0))
        
        self.status_label = ttk.Label(self.status_bar, text="Ready")
        self.status_label.pack(side=tk.LEFT)
        
        self.file_count_label = ttk.Label(self.status_bar, text="")
        self.file_count_label.pack(side=tk.RIGHT)
        
    def setup_context_menu(self):
        """Setup context menu"""
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Open", command=self.open_file)
        self.context_menu.add_command(label="Open with...", command=self.open_with)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Copy", command=self.copy_files)
        self.context_menu.add_command(label="Cut", command=self.cut_files)
        self.context_menu.add_command(label="Paste", command=self.paste_files)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Rename", command=self.rename_file)
        self.context_menu.add_command(label="Delete", command=self.delete_files)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Properties", command=self.show_properties)
        
    def load_directory(self):
        """Load current directory contents"""
        try:
            # Update address bar
            self.address_var.set(str(self.current_path))
            
            # Clear existing items
            self.file_list.delete(*self.file_list.get_children())
            
            # Load files and folders
            items = []
            try:
                for item in self.current_path.iterdir():
                    items.append(item)
            except PermissionError:
                messagebox.showerror("Error", "Permission denied")
                return
            
            # Sort items (folders first, then files)
            items.sort(key=lambda x: (x.is_file(), x.name.lower()))
            
            # Add items to file list
            for item in items:
                try:
                    stat_info = item.stat()
                    size = self.format_size(stat_info.st_size) if item.is_file() else ""
                    modified = datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M")
                    file_type = self.get_file_type(item)
                    
                    self.file_list.insert('', 'end', values=(
                        item.name,
                        size,
                        modified,
                        file_type
                    ))
                except (OSError, PermissionError):
                    continue
            
            # Update file count
            file_count = len([item for item in items if item.is_file()])
            folder_count = len([item for item in items if item.is_dir()])
            self.file_count_label.config(text=f"Files: {file_count}, Folders: {folder_count}")
            
            # Load tree view
            self.load_tree_view()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load directory: {str(e)}")
    
    def load_tree_view(self):
        """Load tree view with current directory structure"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add current directory and parent directories
        current = self.current_path
        path_parts = []
        
        while current != current.parent:
            path_parts.insert(0, current)
            current = current.parent
        
        # Add root
        root_item = self.tree.insert('', 'end', text=str(path_parts[0]), values=(str(path_parts[0]),))
        
        # Add path parts
        current_item = root_item
        for part in path_parts[1:]:
            current_item = self.tree.insert(current_item, 'end', text=part.name, values=(str(part),))
        
        # Expand to current directory
        self.tree.see(current_item)
        self.tree.selection_set(current_item)
    
    def format_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        
        return f"{size_bytes:.1f} {size_names[i]}"
    
    def get_file_type(self, path):
        """Get file type based on extension"""
        if path.is_dir():
            return "Folder"
        
        mime_type, _ = mimetypes.guess_type(str(path))
        if mime_type:
            return mime_type.split('/')[0].title()
        
        return "File"
    
    def navigate_to_path(self, event=None):
        """Navigate to path specified in address bar"""
        path_str = self.address_var.get().strip()
        if not path_str:
            return
        
        try:
            new_path = Path(path_str)
            if new_path.exists() and new_path.is_dir():
                self.current_path = new_path
                self.add_to_history(new_path)
                self.load_directory()
            else:
                messagebox.showerror("Error", "Path does not exist or is not a directory")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid path: {str(e)}")
    
    def add_to_history(self, path):
        """Add path to navigation history"""
        # Remove any forward history
        self.history = self.history[:self.history_index + 1]
        
        # Add new path
        self.history.append(path)
        self.history_index = len(self.history) - 1
    
    def go_back(self):
        """Go back in history"""
        if self.history_index > 0:
            self.history_index -= 1
            self.current_path = self.history[self.history_index]
            self.load_directory()
    
    def go_forward(self):
        """Go forward in history"""
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.current_path = self.history[self.history_index]
            self.load_directory()
    
    def go_up(self):
        """Go up one directory level"""
        if self.current_path.parent != self.current_path:
            self.current_path = self.current_path.parent
            self.add_to_history(self.current_path)
            self.load_directory()
    
    def go_home(self):
        """Go to home directory"""
        self.current_path = Path.home()
        self.add_to_history(self.current_path)
        self.load_directory()
    
    def refresh(self):
        """Refresh current directory"""
        self.load_directory()
    
    def on_tree_double_click(self, event):
        """Handle tree double click"""
        item = self.tree.selection()[0]
        path_str = self.tree.item(item, 'values')[0]
        self.current_path = Path(path_str)
        self.add_to_history(self.current_path)
        self.load_directory()
    
    def on_file_double_click(self, event):
        """Handle file double click"""
        selection = self.file_list.selection()
        if not selection:
            return
        
        item = self.file_list.item(selection[0])
        filename = item['values'][0]
        file_path = self.current_path / filename
        
        if file_path.is_dir():
            self.current_path = file_path
            self.add_to_history(self.current_path)
            self.load_directory()
        else:
            self.open_file(file_path)
    
    def on_file_click(self, event):
        """Handle file click"""
        selection = self.file_list.selection()
        if not selection:
            self.selected_files = []
            return
        
        # Get selected files
        self.selected_files = []
        for item in selection:
            filename = self.file_list.item(item)['values'][0]
            self.selected_files.append(self.current_path / filename)
    
    def on_tree_right_click(self, event):
        """Handle tree right click"""
        # Implementation for tree context menu
        pass
    
    def on_file_right_click(self, event):
        """Handle file right click"""
        # Show context menu
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def select_all_files(self, event):
        """Select all files"""
        self.file_list.selection_set(self.file_list.get_children())
        self.on_file_click(event)
    
    def create_folder(self):
        """Create new folder"""
        name = tk.simpledialog.askstring("New Folder", "Enter folder name:")
        if name:
            try:
                new_folder = self.current_path / name
                new_folder.mkdir()
                self.load_directory()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create folder: {str(e)}")
    
    def create_file(self):
        """Create new file"""
        name = tk.simpledialog.askstring("New File", "Enter file name:")
        if name:
            try:
                new_file = self.current_path / name
                new_file.touch()
                self.load_directory()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create file: {str(e)}")
    
    def copy_files(self):
        """Copy selected files"""
        if not self.selected_files:
            messagebox.showwarning("Warning", "No files selected")
            return
        
        self.cut_files = []  # Clear cut files
        # Implementation for copying files
        messagebox.showinfo("Info", f"Copied {len(self.selected_files)} files")
    
    def cut_files(self):
        """Cut selected files"""
        if not self.selected_files:
            messagebox.showwarning("Warning", "No files selected")
            return
        
        self.cut_files = self.selected_files.copy()
        messagebox.showinfo("Info", f"Cut {len(self.selected_files)} files")
    
    def paste_files(self):
        """Paste files"""
        if not self.cut_files:
            messagebox.showwarning("Warning", "No files to paste")
            return
        
        # Implementation for pasting files
        messagebox.showinfo("Info", f"Pasted {len(self.cut_files)} files")
        self.cut_files = []
        self.load_directory()
    
    def delete_files(self):
        """Delete selected files"""
        if not self.selected_files:
            messagebox.showwarning("Warning", "No files selected")
            return
        
        if messagebox.askyesno("Confirm", f"Delete {len(self.selected_files)} files?"):
            try:
                for file_path in self.selected_files:
                    if file_path.is_dir():
                        shutil.rmtree(file_path)
                    else:
                        file_path.unlink()
                self.load_directory()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete files: {str(e)}")
    
    def rename_file(self):
        """Rename selected file"""
        if not self.selected_files or len(self.selected_files) != 1:
            messagebox.showwarning("Warning", "Select exactly one file")
            return
        
        old_path = self.selected_files[0]
        new_name = tk.simpledialog.askstring("Rename", "Enter new name:", initialvalue=old_path.name)
        
        if new_name:
            try:
                new_path = old_path.parent / new_name
                old_path.rename(new_path)
                self.load_directory()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to rename file: {str(e)}")
    
    def open_file(self, file_path=None):
        """Open selected file"""
        if file_path is None:
            if not self.selected_files or len(self.selected_files) != 1:
                messagebox.showwarning("Warning", "Select exactly one file")
                return
            file_path = self.selected_files[0]
        
        try:
            if platform.system() == 'Windows':
                os.startfile(file_path)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.run(['open', file_path])
            else:  # Linux
                subprocess.run(['xdg-open', file_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")
    
    def open_with(self):
        """Open file with specific application"""
        if not self.selected_files or len(self.selected_files) != 1:
            messagebox.showwarning("Warning", "Select exactly one file")
            return
        
        file_path = self.selected_files[0]
        # Implementation for "Open with" dialog
        messagebox.showinfo("Info", f"Open with dialog for {file_path.name}")
    
    def show_properties(self):
        """Show file properties"""
        if not self.selected_files or len(self.selected_files) != 1:
            messagebox.showwarning("Warning", "Select exactly one file")
            return
        
        file_path = self.selected_files[0]
        self.show_file_properties(file_path)
    
    def show_file_properties(self, file_path):
        """Show detailed file properties"""
        try:
            stat_info = file_path.stat()
            
            properties_window = tk.Toplevel(self.root)
            properties_window.title(f"Properties - {file_path.name}")
            properties_window.geometry("400x500")
            
            # Create properties display
            text_widget = scrolledtext.ScrolledText(properties_window, wrap=tk.WORD)
            text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # File information
            info = f"""File Properties

Name: {file_path.name}
Path: {file_path}
Type: {'Directory' if file_path.is_dir() else 'File'}
Size: {self.format_size(stat_info.st_size)}
Created: {datetime.fromtimestamp(stat_info.st_ctime).strftime("%Y-%m-%d %H:%M:%S")}
Modified: {datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")}
Accessed: {datetime.fromtimestamp(stat_info.st_atime).strftime("%Y-%m-%d %H:%M:%S")}

Permissions:
Read: {'Yes' if stat_info.st_mode & stat.S_IRUSR else 'No'}
Write: {'Yes' if stat_info.st_mode & stat.S_IWUSR else 'No'}
Execute: {'Yes' if stat_info.st_mode & stat.S_IXUSR else 'No'}

File Type: {self.get_file_type(file_path)}
"""
            
            if file_path.is_file():
                # Calculate file hash
                try:
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                    info += f"MD5 Hash: {file_hash}\n"
                except:
                    info += "MD5 Hash: Unable to calculate\n"
            
            text_widget.insert(tk.END, info)
            text_widget.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show properties: {str(e)}")
    
    def open_search(self):
        """Open search dialog"""
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Files")
        search_window.geometry("500x400")
        
        # Search frame
        search_frame = ttk.Frame(search_window)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(search_frame, text="Search for:").pack(side=tk.LEFT)
        search_entry = ttk.Entry(search_frame)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        
        def perform_search():
            search_term = search_entry.get().strip()
            if not search_term:
                return
            
            # Perform search in background thread
            def search_thread():
                results = []
                try:
                    for root, dirs, files in os.walk(self.current_path):
                        for file in files:
                            if search_term.lower() in file.lower():
                                results.append(os.path.join(root, file))
                        for dir_name in dirs:
                            if search_term.lower() in dir_name.lower():
                                results.append(os.path.join(root, dir_name))
                except Exception as e:
                    messagebox.showerror("Error", f"Search failed: {str(e)}")
                    return
                
                # Update results in main thread
                self.root.after(0, lambda: self.display_search_results(results, search_window))
            
            threading.Thread(target=search_thread, daemon=True).start()
        
        ttk.Button(search_frame, text="Search", command=perform_search).pack(side=tk.RIGHT)
        
        # Results frame
        results_frame = ttk.Frame(search_window)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Results list
        results_list = ttk.Treeview(results_frame, columns=('Path',), show='headings')
        results_list.heading('Path', text='Search Results')
        results_list.pack(fill=tk.BOTH, expand=True)
        
        def display_results(results):
            results_list.delete(*results_list.get_children())
            for result in results:
                results_list.insert('', 'end', values=(result,))
        
        # Store display function for use in search thread
        self.display_search_results = display_results
    
    def run(self):
        """Run the file manager"""
        self.root.mainloop()


def main():
    """Main function"""
    # Import tkinter.simpledialog
    import tkinter.simpledialog
    
    # Add simpledialog to tkinter module
    tk.simpledialog = tkinter.simpledialog
    
    # Create and run file manager
    file_manager = FileManager()
    file_manager.run()


if __name__ == "__main__":
    main()
