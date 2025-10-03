# YouTube View Bot - Complete Setup Guide

This guide will help you set up and run the YouTube View Bot step-by-step.

## Prerequisites

### 1. Python Installation
- **Required:** Python 3.9.0 or higher
- **Download:** https://www.python.org/downloads/
- **Check your version:** Run `python --version` or `python3 --version` in terminal

### 2. Browser Installation
You need at least one of these browsers installed:
- **Firefox** (Recommended - works best)
- Chrome
- Edge
- Opera
- Internet Explorer

### 3. Internet Connection
Required for:
- Installing dependencies
- Downloading browser drivers
- Running the bot

## Quick Setup (Recommended)

### Step 1: Clone/Download the Repository
```bash
# Option A: Using git
git clone https://github.com/gavintranquilino/YouTube-view-bot.git
cd YouTube-view-bot

# Option B: Download ZIP
# Download the ZIP file and extract it, then navigate to the folder
```

### Step 2: Run Setup Script
```bash
python setup.py
```

This automated script will:
- ✅ Check your Python version
- ✅ Install all required dependencies (selenium, webdriver-manager, requests)
- ✅ Create configuration files
- ✅ Guide you through the final steps

### Step 3: Configure Your Video
Edit `config.json` and replace the video URL:

```json
{
    "website": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID",
    "tab_amount": 3,
    "watch_time": 35,
    "view_cycles": 5,
    "browser": "firefox"
}
```

**Example:**
```json
{
    "website": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "tab_amount": 3,
    "watch_time": 35,
    "view_cycles": 5,
    "browser": "firefox"
}
```

### Step 4: Verify Setup
```bash
python verify_setup.py
```

This will check if everything is configured correctly.

### Step 5: Run the Bot
```bash
python main.py
```

## Manual Setup

If you prefer to set up manually:

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install selenium webdriver-manager requests
```

### Step 2: Create Configuration
Copy `default.json` to `config.json`:
```bash
cp default.json config.json
```

Edit `config.json` with your settings.

### Step 3: Run
```bash
python main.py
```

## Configuration Options Explained

### `website`
- **Type:** String (URL)
- **Description:** The YouTube video URL you want to boost views for
- **Example:** `"https://www.youtube.com/watch?v=dQw4w9WgXcQ"`

### `tab_amount`
- **Type:** Integer
- **Description:** Number of browser tabs to open simultaneously
- **Default:** 3
- **Recommended:** 2-5 (too many may slow down your computer)

### `watch_time`
- **Type:** Integer (seconds)
- **Description:** How long to watch the video before refreshing
- **Default:** 35
- **Note:** Longer watch time may count as more legitimate views

### `view_cycles`
- **Type:** Integer
- **Description:** How many times to refresh and watch the video
- **Default:** 5
- **Note:** Total views = tab_amount × view_cycles

### `browser`
- **Type:** String
- **Description:** Which browser to use
- **Options:**
  - `"firefox"` (Recommended)
  - `"chrome"`
  - `"edge"`
  - `"opera"`
  - `"explorer"` (Internet Explorer)
- **Note:** Browser must be installed on your system

## Troubleshooting

### Python Not Found
**Error:** `python: command not found`

**Solution:**
- Try `python3` instead of `python`
- Make sure Python is installed and in your PATH
- Windows: Reinstall Python and check "Add Python to PATH"

### Dependencies Won't Install
**Error:** `pip install` fails

**Solution:**
```bash
# Try with user flag
pip install --user -r requirements.txt

# Or use pip3
pip3 install -r requirements.txt

# Update pip first
python -m pip install --upgrade pip
```

### Browser Driver Issues
**Error:** Browser driver not found or can't download

**Solution:**
- Make sure you have internet connection
- The webdriver-manager will auto-download drivers on first run
- Try a different browser in config.json

### Config File Errors
**Error:** `FileNotFoundError` or JSON errors

**Solution:**
- Make sure `config.json` exists in the same directory as `main.py`
- Verify JSON syntax is correct (use a JSON validator)
- Check that all quotation marks are properly matched

### Video Won't Play
**Error:** Can't find play button or video doesn't start

**Solution:**
- YouTube's HTML structure may have changed
- Try a different video URL
- Update selenium to the latest version: `pip install --upgrade selenium`

## What Happens When You Run the Bot?

1. **Initialization:** Loads configuration and initializes browser
2. **Opens Tabs:** Creates the specified number of browser tabs
3. **Opens Links:** Navigates each tab to the YouTube video
4. **Plays Videos:** Clicks play button in each tab
5. **Watch Cycle:** Watches videos for specified time
6. **Refresh & Repeat:** Refreshes all tabs and repeats for specified cycles
7. **Complete:** Closes browser and finishes

## Best Practices

1. **Start Small:** Begin with low values (3 tabs, 5 cycles) to test
2. **Reasonable Wait Times:** 30-60 seconds watch time is realistic
3. **Monitor System Resources:** Don't overload your computer
4. **Use Firefox:** Generally most reliable for automation
5. **Stable Internet:** Ensure good connection during operation

## Legal and Ethical Notice

⚠️ **Important:** This tool is for educational and personal testing purposes only.

- Not intended for malicious purposes or monetization strategies
- May violate YouTube's Terms of Service
- Use at your own risk
- The authors are not responsible for any consequences of use

## Support

If you encounter issues:

1. **Verify Setup:** Run `python verify_setup.py`
2. **Check README:** Review the main README.md
3. **Check Logs:** Look for error messages in terminal
4. **Update Dependencies:** Try `pip install --upgrade -r requirements.txt`
5. **Try Different Browser:** Change browser in config.json

## Additional Resources

- [Python Documentation](https://docs.python.org/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Project Issues](https://github.com/gavintranquilino/YouTube-view-bot/issues)
- [Contributing Guide](CONTRIBUTING.md)

---

**Last Updated:** 2024
**Version:** 1.0
