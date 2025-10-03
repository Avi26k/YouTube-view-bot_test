# YouTube View Bot

This is a tool to boost viewer count on a YouTube video. This is not intended for malicious purposes or monetization strategies. This was intended for personal use and testing purposes.

📚 **[Complete Setup Guide](SETUP_GUIDE.md)** - Detailed step-by-step instructions for setup and troubleshooting

# Installation

## Quick Setup (Recommended)

Run the automated setup script:

```bash
python setup.py
```

This will:
- Check your Python version (3.9.0+ required)
- Install all required dependencies
- Create configuration files
- Guide you through the final setup steps

## Manual Installation

### Python Version
Download the latest [Python](https://www.python.org/downloads/) release.

This program was built in Python 3.9.0, but should work in Python 3.9.0+

### Downloading/Cloning the GitHub repository
Use [git](https://git-scm.com/) to install the repository.

In the folder you want to install the YouTube-view-bot, run the following command to clone this repository to your local system.

```bash
git clone https://github.com/gavintranquilino/YouTube-view-bot.git .
```

Alternatively, download this project as a **.zip** file, and extract into your device.

### Downloading the dependencies

#### Using requirements.txt (Recommended)
```bash
pip install -r requirements.txt
```

#### Manual installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install webdriver-manager selenium requests
```

### Browser Installation
Make sure you have at least one of the supported browsers installed:
- **Firefox** (Recommended)
- Chrome
- Edge
- Opera
- Internet Explorer

The webdriver will be automatically downloaded when you run the program.

# Configuration

### config.json
1. The setup script will create a `config.json` file from `default.json` template
2. Edit the `config.json` file with your settings:

```json
{
    "website": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID", 
    "tab_amount": 3,
    "watch_time": 35,
    "view_cycles": 5,
    "browser": "firefox"
}
```

**Configuration Options:**
- `website`: Your YouTube video URL (replace YOUR_VIDEO_ID with actual video ID)
- `tab_amount`: Number of browser tabs to open (default: 3)
- `watch_time`: Time to watch video in seconds (default: 35)
- `view_cycles`: Number of view cycles to perform (default: 5)
- `browser`: Browser to use - options: `firefox`, `chrome`, `edge`, `opera`, `explorer`

# Usage

### Verify Setup
Before running the bot, you can verify your setup is correct:

```bash
python verify_setup.py
```

This will check:
- All dependencies are installed
- Configuration file is properly set up
- Video URL is configured

### How do I run this program?
If you have completed the setup and configuration listed above, open a terminal in this directory and run using this command.

```bash
python main.py
```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

See [CONTRIBUTING.md](https://github.com/gavintranquilino/YouTube-view-bot/blob/master/CONTRIBUTING.md) file.

## License
See [LICENSE](https://github.com/gavintranquilino/YouTube-view-bot/blob/master/LICENSE) file.

