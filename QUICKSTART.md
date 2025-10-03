# Quick Start Guide

Get the YouTube View Bot running in 3 simple steps!

## Step 1: Run Setup
```bash
python setup.py
```

## Step 2: Configure Video
Edit `config.json` and add your YouTube video URL:
```json
{
    "website": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
}
```

## Step 3: Run Bot
```bash
python main.py
```

---

## Need Help?

- 📚 [Complete Setup Guide](SETUP_GUIDE.md) - Detailed instructions
- ✅ Run `python verify_setup.py` to check your setup
- 📖 See [README.md](README.md) for full documentation

## What This Does

The bot will:
1. Open browser tabs (default: 3)
2. Play your YouTube video in each tab
3. Watch for specified time (default: 35 seconds)
4. Refresh and repeat (default: 5 cycles)

**Total views generated:** tabs × cycles = 3 × 5 = 15 views

---

## Requirements

- Python 3.9.0+
- One of: Firefox (recommended), Chrome, Edge, Opera
- Internet connection

---

**⚠️ Disclaimer:** For educational and testing purposes only. Use responsibly.
