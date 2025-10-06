# Python Installation Guide 🛠️

> Complete step-by-step guide to installing Python on any operating system

This guide will help you install Python on your computer and verify that everything is working correctly. Python is currently at version **3.13.7** as the latest stable release [attached_file:1].

## 📋 Prerequisites

Before installing Python, ensure you have:
- **Administrator privileges** on your computer
- **Stable internet connection** for downloading
- **At least 100MB** of free disk space

---

## 💻 Windows Installation

### Step 1: Download Python

1. **Visit the official Python website**: [https://python.org](https://python.org) [attached_file:1]
2. **Locate the download section**: The homepage displays "**Download Python 3.13.7**" prominently
3. **Click the download button**: This automatically detects your Windows version
4. **Save the installer**: The file will be named `python-3.13.7-amd64.exe` (or similar)

> **💡 Pro Tip**: Always download from the official Python.org website to ensure security and authenticity.

### Step 2: Run the Installation

1. **Launch the installer**: Double-click the downloaded `.exe` file
2. **⚠️ CRITICAL**: Check **"Add Python 3.13 to PATH"** at the bottom of the installer window
   - This allows you to run Python from any Command Prompt location
   - **Without this, Python won't work from the command line**
3. **Choose installation type**:
   - **Recommended**: Click "**Install Now**" for default settings
   - **Advanced**: Click "**Customize installation**" for custom directory
4. **Wait for completion**: The installer will show progress and confirm when finished

### Step 3: Verify Installation

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, press Enter
   - Or search "Command Prompt" in Start menu
2. **Check Python version**:
python --version

text
Expected output: `Python 3.13.7`
3. **Check pip (package manager)**:
pip --version

text
Expected output: `pip 24.x.x from ...`

---
# Python Installation Guide 🛠️

> Complete step-by-step guide to installing Python on any operating system

This guide will help you install Python on your computer and verify that everything is working correctly. Python is currently at version **3.13.7** as the latest stable release [attached_file:1].

## 📋 Prerequisites

Before installing Python, ensure you have:
- **Administrator privileges** on your computer
- **Stable internet connection** for downloading
- **At least 100MB** of free disk space

---

## 💻 Windows Installation

### Step 1: Download Python

1. **Visit the official Python website**: [https://python.org](https://python.org) [attached_file:1]
2. **Locate the download section**: The homepage displays "**Download Python 3.13.7**" prominently
3. **Click the download button**: This automatically detects your Windows version
4. **Save the installer**: The file will be named `python-3.13.7-amd64.exe` (or similar)

> **💡 Pro Tip**: Always download from the official Python.org website to ensure security and authenticity.

### Step 2: Run the Installation

1. **Launch the installer**: Double-click the downloaded `.exe` file
2. **⚠️ CRITICAL**: Check **"Add Python 3.13 to PATH"** at the bottom of the installer window
   - This allows you to run Python from any Command Prompt location
   - **Without this, Python won't work from the command line**
3. **Choose installation type**:
   - **Recommended**: Click "**Install Now**" for default settings
   - **Advanced**: Click "**Customize installation**" for custom directory
4. **Wait for completion**: The installer will show progress and confirm when finished

### Step 3: Verify Installation

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, press Enter
   - Or search "Command Prompt" in Start menu
2. **Check Python version**:
```
python --version
```

Expected output: `Python 3.13.7`
3. **Check pip (package manager)**:
```
pip --version
```

Expected output: `pip 24.x.x from ...`

---

## 🍎 macOS Installation

### Method 1: Official Installer (Recommended)

1. **Visit Python.org**: Navigate to [https://python.org](https://python.org) [attached_file:1]
2. **Download for macOS**: Click "Download Python 3.13.7" 
3. **Run the installer**: Double-click the downloaded `.pkg` file
4. **Follow the wizard**: Accept license agreements and choose installation location
5. **Complete installation**: The installer will handle all dependencies

### Method 2: Using Homebrew (Advanced Users)

If you have Homebrew installed:
Update Homebrew first
```
brew update
```

Install Python
```
brew install python
```

Verify installation
```
python3 --version
```

### Method 3: Using pyenv (Version Management)

For managing multiple Python versions:
Install pyenv
```
brew install pyenv
```

Install Python 3.13.7
```
pyenv install 3.13.7
```

Set as global version
```
pyenv global 3.13.7
```

---

## 🐧 Linux Installation

### Ubuntu/Debian Systems

Update package list
```
sudo apt update
```

Install Python 3 and pip
```
sudo apt install python3 python3-pip python3-venv
```

Verify installation
```
python3 --version
pip3 --version
```

### CentOS/RHEL/Fedora Systems

CentOS/RHEL 8+
```
sudo dnf install python3 python3-pip
```

Older CentOS/RHEL versions
```
sudo yum install python3 python3-pip
```

Verify installation
```
python3 --version
pip3 --version
```

### Arch Linux

Install Python
```
sudo pacman -S python python-pip
```

Verify installation
```
python --version
pip --version
```

---

## ✅ Installation Verification

### Create Your First Python File

1. **Create a test directory**:
```
mkdir python-test
cd python-test
```

2. **Create a Python file**: Create `hello.py` with this content:

```python
print("🎉 Python Installation Successful!")
print("Welcome to Python programming!")

import sys
print(f"Python version: {sys.version}")

result = 2 + 3
print(f"2 + 3 = {result}")
```

3. **Run your program**:
Windows
```
python hello.py
```

macOS/Linux
```
python3 hello.py
```

### Expected Output
```
🎉 Python Installation Successful!
Welcome to Python programming!
Python version: 3.13.7 (main, ...)
2 + 3 = 5
```

---

## 🛠️ Setting Up Development Environment

### Install Essential Packages

Upgrade pip to latest version
```
python -m pip install --upgrade pip
```

Install useful packages for beginners
```
pip install requests beautifulsoup4 matplotlib pandas
```

### Choose a Code Editor

**For Beginners:**
- **IDLE**: Built-in with Python (simple and lightweight)
- **Thonny**: Beginner-friendly with debugging tools

**For Development:**
- **Visual Studio Code**: Free, powerful, with Python extensions
- **PyCharm Community**: Feature-rich IDE specifically for Python

---

## 🚨 Troubleshooting Common Issues

### Windows Issues

**Problem**: `'python' is not recognized as an internal or external command`
**Solution**: 
1. Reinstall Python with "Add to PATH" checked
2. Or manually add Python to PATH in System Environment Variables

**Problem**: Microsoft Store Python opens instead
**Solution**: 
1. Open Settings → Apps → App execution aliases
2. Turn off Python aliases for Microsoft Store

### macOS Issues

**Problem**: `command not found: python`
**Solution**: Use `python3` instead of `python` on macOS

### Linux Issues

**Problem**: `python3-distutils` missing
**Solution**: Install additional packages:
```
sudo apt install python3-distutils python3-dev
```

---

## 🎯 Quick Reference Commands

| Task | Windows | macOS/Linux |
|------|---------|-------------|
| Check version | `python --version` | `python3 --version` |
| Run Python | `python` | `python3` |
| Install package | `pip install package` | `pip3 install package` |
| Run script | `python script.py` | `python3 script.py` |

---

## 🔗 What's Next?

✅ **Python is now installed and ready!**

**Continue your journey:**
1. **Next Guide**: `your-first-program.md` - Write your first real Python program
2. **Learn Basics**: `../02-Core-Concepts/` - Variables, data types, and operators
3. **Practice**: `../06-Practice-Projects/` - Hands-on coding projects

**Additional Resources:**
- [Python.org Documentation](https://docs.python.org/3/) [attached_file:1]
- [Python Package Index (PyPI)](https://pypi.org/) - Thousands of packages
- [Python Community](https://www.python.org/community/) - Get help and connect [attached_file:1]

---

**🎉 Congratulations! You're ready to start coding in Python!**