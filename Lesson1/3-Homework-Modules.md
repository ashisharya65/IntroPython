# Exercise: Using Third-Party Modules with Virtual Environments

## Overview
In this exercise, you'll learn how to:
1. Set up a virtual environment in VS Code
2. Install a third-party module using pip
3. Import and use functions from that module
4. Print results to the screen

We'll use the `requests` module to fetch data from the internet - a very common real-world task!

---

## Part 1: Project Setup and Virtual Environment

### Step 1: Create Your Project Folder
1. Open VS Code
2. Click **File > Open Folder**
3. Create a new folder called `weather_app`
4. Open this folder in VS Code

### Step 2: Ensure PowerShell is Your Default Terminal
1. Press **Ctrl + Shift + P**
2. Type "Terminal: Select Default Profile"
3. Select **PowerShell**

### Step 3: Open Terminal and Check Your Location
1. Press **Ctrl + `** to open the integrated terminal
2. You should see: `PS C:\Users\YourName\weather_app>`
3. If you're not in the weather_app folder, navigate there

### Step 4: Create Virtual Environment
In the PowerShell terminal, type:
```powershell
python -m venv .venv
```

### Step 5: Activate Virtual Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

**✅ Verify it's working:** Your prompt should now show `(.venv)` at the beginning:
```
(.venv) PS C:\Users\YourName\weather_app>
```

### Step 6: Configure VS Code to Use the Virtual Environment
1. Press **Ctrl + Shift + P**
2. Type "Python: Select Interpreter"
3. Choose the one that shows: `.\\.venv\\Scripts\\python.exe`

---

## Part 2: Installing and Using a Third-Party Module

### Step 7: Install the Requests Module
In your activated PowerShell terminal:
```powershell
pip install requests
```

**What you'll see:**
```
Collecting requests
Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Installing collected packages: requests
Successfully installed requests-2.31.0
```

### Step 8: Verify Installation
Check that the module was installed:
```powershell
pip list
```

You should see `requests` in the list along with its dependencies.

---

## Part 3: Create Your First Script Using the Module

### Step 9: Create Your Python File
1. In VS Code, create a new file called `weather_checker.py`
2. Add the following code:

```python
# Import the requests module we just installed
import requests

# Function to get a random fact from an API
def get_random_fact():
    """Fetch a random fun fact from the internet"""
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Use requests to get data from the internet
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON (dictionary)
        data = response.json()
        return data['text']
    else:
        return "Sorry, couldn't fetch a fact right now!"

# Function to get current time from an API
def get_current_time():
    """Get current UTC time from an API"""
    url = "http://worldtimeapi.org/api/timezone/UTC"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['datetime'][:19]  # Get just the date and time part
    else:
        return "Couldn't get current time"

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("WELCOME TO THE INFO FETCHER!")
    print("=" * 50)
    
    # Test 1: Get a random fact
    print("\n🎯 Here's a random fun fact:")
    fact = get_random_fact()
    print(f"📝 {fact}")
    
    # Test 2: Get current time
    print("\n⏰ Current UTC time:")
    current_time = get_current_time()
    print(f"🕐 {current_time}")
    
    # Test 3: Show that requests module is working
    print("\n✅ Successfully used the 'requests' module!")
    print(f"📦 Requests module location: {requests.__file__}")
    
    print("\n" + "=" * 50)
    print("EXERCISE COMPLETED SUCCESSFULLY!")
    print("=" * 50)
```

### Step 10: Run Your Script
In the PowerShell terminal (make sure (.venv) is still showing):
```powershell
python weather_checker.py
```

**Expected Output:**
```
==================================================
WELCOME TO THE INFO FETCHER!
==================================================

🎯 Here's a random fun fact:
📝 [Some random fact will appear here]

⏰ Current UTC time:
🕐 2025-09-11T14:23:45

✅ Successfully used the 'requests' module!
📦 Requests module location: C:\Users\YourName\weather_app\.venv\lib\site-packages\requests\__init__.py

==================================================
EXERCISE COMPLETED SUCCESSFULLY!
==================================================
```

---

## Part 4: Understanding What Happened

### What Did We Accomplish?
1. **Created an isolated environment** - Our `requests` module is only installed in this project
2. **Used a third-party module** - `requests` is not built into Python
3. **Made HTTP requests** - We fetched data from real websites
4. **Processed JSON data** - We converted web responses into Python dictionaries
5. **Handled errors** - We checked if our requests were successful

### Key Concepts Demonstrated:
- **Virtual environments** keep projects separate
- **pip install** downloads modules from the internet
- **import** brings external code into your script
- **API calls** let you get data from web services
- **JSON** is a common format for web data

---

## Part 5: Extended Practice

### Challenge 1: Add Another API Call
Add this function to your script and call it:

```python
def get_random_joke():
    """Get a random programming joke"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "No jokes available right now!"
```

### Challenge 2: Check Your Virtual Environment
Add these lines to verify you're using the virtual environment:

```python
import sys
print(f"\n🐍 Python executable: {sys.executable}")
print(f"📁 Virtual environment active: {'.venv' in sys.executable}")
```

### Challenge 3: Save Your Dependencies
In PowerShell, create a requirements file:
```powershell
pip freeze > requirements.txt
```

Open `requirements.txt` to see what was saved.

---

## Troubleshooting Common Issues

### Problem: ModuleNotFoundError
**Error:** `ModuleNotFoundError: No module named 'requests'`

**Solutions:**
1. Check if virtual environment is activated (look for `(.venv)`)
2. If not activated, run: `.\.venv\Scripts\Activate.ps1`
3. Reinstall the module: `pip install requests`
4. Make sure VS Code is using the right interpreter

### Problem: Internet Connection Errors
**Error:** Connection timeouts or network errors

**Solutions:**
1. Check your internet connection
2. Try a different API endpoint
3. Add error handling to your code

### Problem: Virtual Environment Not Working
**Check these:**
```powershell
# Is it activated?
$env:VIRTUAL_ENV

# Are you in the right folder?
Get-Location

# Is the .venv folder there?
Test-Path .\.venv
```

---

## What You've Learned

By completing this exercise, you now understand:

✅ **Virtual Environment Management**
- How to create and activate virtual environments
- Why they're important for project isolation

✅ **Third-Party Module Usage**
- How to install modules with pip
- How to import and use external libraries

✅ **API Integration**
- How to make HTTP requests to web services
- How to process JSON responses

✅ **Error Handling**
- How to check if requests were successful
- How to provide fallback messages

✅ **Real-World Skills**
- These are the exact skills used in professional Python development!

---

## Next Steps

Now that you understand requirements files and module management, try:
1. **Create requirements files for different project types** - web scraping, data analysis, game development
2. **Explore module documentation** - Read about what other functions requests and BeautifulSoup offer
3. **Try collaborative development** - Share your requirements.txt with a classmate and have them recreate your environment
4. **Learn about version conflicts** - Try installing incompatible versions and see what happens
5. **Explore virtual environment best practices** - Learn when to create new environments vs. reusing existing ones

Remember: Always use requirements.txt files for your projects - it's the professional standard!