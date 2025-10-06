import os
import sys
import threading
import logging
from typing import Callable, Optional
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem, Menu
import io

class SystemTrayApp:
    """System tray application for the Auto Git Backup tool"""

    def __init__(self, 
                 start_callback: Callable, 
                 pause_callback: Callable,
                 exit_callback: Callable,
                 get_status_callback: Callable,
                 logger: logging.Logger):
        self.start_callback = start_callback
        self.pause_callback = pause_callback
        self.exit_callback = exit_callback
        self.get_status_callback = get_status_callback
        self.logger = logger
        self.icon: Optional[pystray.Icon] = None
        self.is_running = False

    def _create_icon_image(self, color: str = "green") -> Image.Image:
        """Create a simple icon image"""
        # Create a 64x64 image
        img = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        # Color mapping
        colors = {
            "green": (0, 255, 0, 255),
            "orange": (255, 165, 0, 255),
            "red": (255, 0, 0, 255),
            "gray": (128, 128, 128, 255)
        }

        fill_color = colors.get(color, colors["gray"])

        # Draw a circle
        draw.ellipse([8, 8, 56, 56], fill=fill_color, outline=(0, 0, 0, 255), width=2)

        # Draw "G" for Git
        draw.text((24, 20), "G", fill=(0, 0, 0, 255))

        return img

    def _get_menu(self) -> Menu:
        """Create the context menu"""
        status = self.get_status_callback()

        # Determine icon color based on status
        if status.get('is_active', False):
            if status.get('last_error'):
                icon_color = "orange"  # Active with errors
            else:
                icon_color = "green"   # Active and healthy
        else:
            icon_color = "red"  # Paused/inactive

        # Update icon color
        if self.icon:
            self.icon.icon = self._create_icon_image(icon_color)

        # Build menu items
        menu_items = []

        # Status information
        if status.get('is_active', False):
            menu_items.append(MenuItem("● Active", None, enabled=False))
        else:
            menu_items.append(MenuItem("○ Paused", None, enabled=False))

        # Last commit info
        if status.get('last_commit'):
            menu_items.append(MenuItem(f"Last: {status['last_commit'][:50]}...", None, enabled=False))

        # Error info
        if status.get('last_error'):
            menu_items.append(MenuItem(f"Error: {status['last_error'][:30]}...", None, enabled=False))

        menu_items.append(MenuItem("---", None))  # Separator

        # Control buttons
        if status.get('is_active', False):
            menu_items.append(MenuItem("Pause", self._on_pause))
        else:
            menu_items.append(MenuItem("Start", self._on_start))

        menu_items.extend([
            MenuItem("---", None),  # Separator
            MenuItem("Exit", self._on_exit)
        ])

        return Menu(*menu_items)

    def _on_start(self, icon, item):
        """Handle start menu click"""
        try:
            self.logger.info("Start requested from system tray")
            self.start_callback()
        except Exception as e:
            self.logger.error(f"Error in start callback: {str(e)}")

    def _on_pause(self, icon, item):
        """Handle pause menu click"""
        try:
            self.logger.info("Pause requested from system tray")
            self.pause_callback()
        except Exception as e:
            self.logger.error(f"Error in pause callback: {str(e)}")

    def _on_exit(self, icon, item):
        """Handle exit menu click"""
        try:
            self.logger.info("Exit requested from system tray")
            self.exit_callback()
        except Exception as e:
            self.logger.error(f"Error in exit callback: {str(e)}")

    def start_tray(self):
        """Start the system tray application"""
        if self.is_running:
            return

        try:
            initial_icon = self._create_icon_image("gray")
            self.icon = pystray.Icon(
                "AutoGitBackup",
                initial_icon,
                "Auto Git Backup",
                menu=self._get_menu()
            )

            self.is_running = True
            self.logger.info("Starting system tray application")

            # Run the icon (this blocks until the icon is stopped)
            self.icon.run()

        except Exception as e:
            self.logger.error(f"Failed to start system tray: {str(e)}")
            self.is_running = False

    def stop_tray(self):
        """Stop the system tray application"""
        if self.icon and self.is_running:
            try:
                self.icon.stop()
                self.is_running = False
                self.logger.info("Stopped system tray application")
            except Exception as e:
                self.logger.error(f"Error stopping system tray: {str(e)}")

    def update_menu(self):
        """Update the context menu (refreshes status)"""
        if self.icon and self.is_running:
            try:
                self.icon.menu = self._get_menu()
            except Exception as e:
                self.logger.error(f"Error updating menu: {str(e)}")

    def run_in_thread(self):
        """Start the system tray in a separate thread"""
        thread = threading.Thread(target=self.start_tray, daemon=True)
        thread.start()
        return thread
