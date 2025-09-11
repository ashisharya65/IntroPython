# Creating Virtual Environments in VS Code on Windows - PowerShell Guide

## What is a Virtual Environment?
A virtual environment is an isolated Python workspace that keeps your project dependencies separate from your system Python installation. This prevents conflicts between different projects and makes your code more portable.

Think of it like having separate toolboxes for different projects - your web development tools don't mix with your data science tools!

---

## Prerequisites Checklist
Before we start, make sure you have:
- [ ] Python installed on Windows (check by typing `python --version` in PowerShell)
- [ ] VS Code installed
- [ ] Python extension for VS Code installed

---

## Setting Up PowerShell in VS Code

### Step 1: Configure VS Code to Use PowerShell
1. Open VS Code
2. Press **Ctrl + Shift + P** to open Command Palette
3. Type "Terminal: Select Default Profile"
4. Select **"PowerShell"** from the list
5. This ensures VS Code will use PowerShell for all terminal sessions

### Step 2: Open Your Project Folder
1. Click **File > Open Folder**
2. Create a new folder for your project (e.g., "my_python_project")
3. Select and open this folder in VS Code

---

## Creating Virtual Environment with PowerShell

### Step 1: Open PowerShell Terminal in VS Code
- Press **Ctrl + `** (backtick) to open the integrated terminal
- You should see something like: `PS C:\Users\YourName\my_python_project>`
- The `PS` indicates you're using PowerShell

### Step 2: Check Python Installation
First, verify Python is working:
```powershell
python --version
```
You should see something like `Python 3.11.5`

### Step 3: Create the Virtual Environment
In the PowerShell terminal, type:
```powershell
python -m venv .venv
```

**What this does:**
- `python -m venv` runs Python's virtual environment module
- `.venv` creates a hidden folder containing your isolated Python environment

**You'll see output like:**
```
Creating virtual environment...
```

### Step 4: Set Execution Policy (If Needed)
If you get an execution policy error, run this command:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Type `Y` when prompted to confirm.

### Step 5: Activate the Virtual Environment
In PowerShell, type:
```powershell
.\.venv\Scripts\Activate.ps1
```

**Alternative activation command (if the above doesn't work):**
```powershell
& .\.venv\Scripts\Activate.ps1
```

**You'll know it worked when:**
- Your PowerShell prompt shows `(.venv)` at the beginning
- Like this: `(.venv) PS C:\Users\YourName\my_python_project>`

### Step 6: Configure VS Code to Use the Virtual Environment
1. Press **Ctrl + Shift + P**
2. Type "Python: Select Interpreter"
3. Choose the interpreter showing: `.\\.venv\\Scripts\\python.exe`
4. You should see this path selected in the bottom-left of VS Code

---

## Verifying Your Setup

### Test 1: Check Python Location
In your activated PowerShell terminal:
```powershell
where.exe python
```
This should show a path containing `.venv`, like:
`C:\Users\YourName\my_python_project\.venv\Scripts\python.exe`

### Test 2: Create and Run a Test File
1. Create a new file called `test.py`
2. Add this code:
```python
import sys
print("Python executable:", sys.executable)
print("Virtual environment active:", hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
```
3. In PowerShell terminal, run:
```powershell
python test.py
```
4. You should see the `.venv` path in the output

---

## Working with Packages in Your Virtual Environment

### Installing Packages
With your virtual environment activated:
```powershell
# Install a single package
pip install requests

# Install multiple packages
pip install pandas numpy matplotlib

# Install a specific version
pip install flask==2.3.0
```

### Checking Installed Packages
```powershell
pip list
```

### Upgrading Packages
```powershell
# Upgrade a specific package
pip install --upgrade requests

# Upgrade pip itself
python -m pip install --upgrade pip
```

### Creating Requirements File
Save your project dependencies:
```powershell
pip freeze > requirements.txt
```

### Installing from Requirements
If you have a `requirements.txt` file:
```powershell
pip install -r requirements.txt
```

---

## PowerShell-Specific Commands and Tips

### Deactivating the Environment
```powershell
deactivate
```
Your prompt will return to normal: `PS C:\Users\YourName\my_python_project>`

### Reactivating Later
When you reopen VS Code or start a new session:
```powershell
.\.venv\Scripts\Activate.ps1
```

### Checking if Virtual Environment is Active
```powershell
# This command shows environment variables
$env:VIRTUAL_ENV
```
If active, it will show the path to your `.venv` folder.

### Clearing the Terminal
```powershell
Clear-Host
```
Or just: `cls`

---

## Troubleshooting PowerShell Issues

### Problem: Execution Policy Error
**Error:** "cannot be loaded because running scripts is disabled on this system"

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem: Virtual Environment Won't Activate
**Solutions:**
1. Try the alternative activation:
   ```powershell
   & .\.venv\Scripts\Activate.ps1
   ```

2. Use the full path:
   ```powershell
   & "C:\full\path\to\your\project\.venv\Scripts\Activate.ps1"
   ```

3. Check if the folder exists:
   ```powershell
   Test-Path .\.venv\Scripts\Activate.ps1
   ```

### Problem: "python" Command Not Found
**Check Python installation:**
```powershell
Get-Command python
```

**If not found, add Python to PATH or use:**
```powershell
py -m venv .venv
```

### Problem: VS Code Terminal Opens Wrong Shell
1. Press **Ctrl + Shift + P**
2. Type "Terminal: Select Default Profile"
3. Choose "PowerShell"
4. Close and reopen terminal

---

## Complete Workflow Example

### Exercise: Create a Web Scraping Project

Let's practice the complete workflow:

**Step 1: Project Setup**
```powershell
# Create and navigate to project folder (do this in File Explorer, then open in VS Code)
# Open VS Code terminal (Ctrl + `)
```

**Step 2: Virtual Environment**
```powershell
# Create virtual environment
python -m venv .venv

# Activate it
.\.venv\Scripts\Activate.ps1

# Verify activation
$env:VIRTUAL_ENV
```

**Step 3: Install Dependencies**
```powershell
# Install packages for web scraping
pip install requests beautifulsoup4 pandas

# Check what's installed
pip list

# Save dependencies
pip freeze > requirements.txt
```

**Step 4: Create Your Script**
Create `scraper.py`:
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

print("All packages imported successfully!")
print("Virtual environment is working!")
```

**Step 5: Run and Test**
```powershell
python scraper.py
```

**Step 6: When Done Working**
```powershell
deactivate
```

---

## Best Practices

1. **Always activate your virtual environment** before working on your project
2. **Use descriptive project folder names** without spaces
3. **Keep your requirements.txt updated** with `pip freeze > requirements.txt`
4. **Don't commit the .venv folder** to version control (add it to .gitignore)
5. **Use PowerShell consistently** for all your terminal work in VS Code

---

## Quick Reference Commands

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Check if active
$env:VIRTUAL_ENV

# Install package
pip install package_name

# List packages
pip list

# Save requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate

# Clear terminal
Clear-Host
```