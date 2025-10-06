import json
import os
from typing import Dict, Any

class ConfigManager:
    """Manages application configuration from config.json file"""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.default_config = {
            "folder_path": "",
            "git_remote": "",
            "commit_interval": 300,  # 5 minutes default
            "log_level": "INFO",
            "max_log_size": 10485760  # 10MB
        }
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create with defaults"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                # Merge with defaults to ensure all keys exist
                for key, value in self.default_config.items():
                    if key not in config:
                        config[key] = value
                return config
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading config: {e}. Using defaults.")
                return self.default_config.copy()
        else:
            # Create default config file
            self.save_config(self.default_config)
            return self.default_config.copy()

    def save_config(self, config: Dict[str, Any] = None) -> None:
        """Save configuration to file"""
        if config is None:
            config = self.config

        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=4)
        except IOError as e:
            print(f"Error saving config: {e}")

    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)

    def set(self, key: str, value: Any):
        """Set configuration value and save"""
        self.config[key] = value
        self.save_config()

    def validate_config(self) -> tuple[bool, str]:
        """Validate current configuration"""
        if not self.config.get('folder_path'):
            return False, "folder_path is required"

        if not os.path.exists(self.config['folder_path']):
            return False, f"folder_path does not exist: {self.config['folder_path']}"

        if not self.config.get('git_remote'):
            return False, "git_remote is required"

        if self.config.get('commit_interval', 0) < 10:
            return False, "commit_interval must be at least 10 seconds"

        return True, "Configuration is valid"
