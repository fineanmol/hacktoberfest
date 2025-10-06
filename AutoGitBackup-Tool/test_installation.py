#!/usr/bin/env python3
"""
Test script for Auto Git Backup Tool
Verifies that all dependencies are installed and basic functionality works
"""

import sys
import os
import importlib
import tempfile
import shutil
from pathlib import Path

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")

    required_modules = [
        ('watchdog', 'watchdog.observers'),
        ('git', 'git'),
        ('pystray', 'pystray'),
        ('PIL', 'PIL.Image'),
        ('tkinter', 'tkinter')
    ]

    failed_imports = []

    for module_name, import_path in required_modules:
        try:
            importlib.import_module(import_path)
            print(f"  ✓ {module_name}")
        except ImportError as e:
            print(f"  ✗ {module_name} - {str(e)}")
            failed_imports.append(module_name)

    return failed_imports

def test_config_manager():
    """Test configuration management"""
    print("\nTesting configuration manager...")

    try:
        from config_manager import ConfigManager

        # Test with temporary config
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            config_path = f.name

        # Create config manager
        config = ConfigManager(config_path)

        # Test setting and getting values
        config.set('test_key', 'test_value')
        assert config.get('test_key') == 'test_value'

        # Clean up
        os.unlink(config_path)

        print("  ✓ Configuration manager works")
        return True

    except Exception as e:
        print(f"  ✗ Configuration manager failed - {str(e)}")
        return False

def main():
    """Run all tests"""
    print("Auto Git Backup Tool - Installation Test")
    print("=" * 40)

    # Test imports first
    failed_imports = test_imports()

    if failed_imports:
        print(f"\n❌ Missing dependencies: {', '.join(failed_imports)}")
        print("\nPlease install missing dependencies:")
        print("  pip install -r requirements.txt")
        return 1

    # Test basic config
    if not test_config_manager():
        print("\n❌ Configuration manager test failed")
        return 1

    print("\n" + "=" * 40)
    print("✅ All tests passed!")
    print("\nThe Auto Git Backup Tool should work correctly.")
    print("Run 'python main.py' to start the application.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
