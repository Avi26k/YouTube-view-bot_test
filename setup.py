#!/usr/bin/env python3
"""
Setup script for YouTube View Bot
This script helps users set up the project by:
1. Installing required dependencies
2. Creating configuration files
3. Verifying the setup
"""

import sys
import subprocess
import json
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def check_python_version():
    """Check if Python version is 3.9.0 or higher"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    print(f"Current Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ ERROR: Python 3.9.0 or higher is required!")
        print("Please install Python 3.9.0+ from https://www.python.org/downloads/")
        return False
    
    print("✅ Python version is compatible")
    return True

def install_dependencies():
    """Install required Python packages"""
    print_header("Installing Dependencies")
    
    try:
        print("Installing packages from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR: Failed to install dependencies: {e}")
        return False

def verify_dependencies():
    """Verify all required packages are installed"""
    print_header("Verifying Dependencies")
    
    required_packages = {
        "selenium": "selenium",
        "webdriver_manager": "webdriver-manager",
        "requests": "requests"
    }
    
    all_installed = True
    
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✅ {package_name} is installed")
        except ImportError:
            # Try pip show as a fallback
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "show", package_name],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print(f"✅ {package_name} is installed")
                else:
                    print(f"❌ {package_name} is NOT installed")
                    all_installed = False
            except Exception:
                print(f"❌ {package_name} is NOT installed")
                all_installed = False
    
    return all_installed

def create_config():
    """Create or update config.json"""
    print_header("Setting Up Configuration")
    
    config_file = "config.json"
    default_file = "default.json"
    
    # Check if config.json exists
    if os.path.exists(config_file):
        print(f"ℹ️  {config_file} already exists")
        
        # Load and check if it needs updating
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        if config.get('website') == 'YOUR VIDEO':
            print("⚠️  Warning: config.json still has placeholder values!")
            print("   Please update the 'website' field with your YouTube video URL")
            return False
        else:
            print("✅ config.json is configured")
            return True
    else:
        # Create config.json from default.json
        if os.path.exists(default_file):
            with open(default_file, 'r') as f:
                default_config = json.load(f)
            
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=4)
            
            print(f"✅ Created {config_file} from {default_file}")
            print("⚠️  Please update the 'website' field with your YouTube video URL")
            return False
        else:
            print(f"❌ ERROR: {default_file} not found!")
            return False

def show_next_steps():
    """Display next steps for the user"""
    print_header("Setup Complete! Next Steps:")
    
    print("1. Edit config.json and set your YouTube video URL:")
    print('   "website": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"')
    print()
    print("2. Adjust other settings if needed:")
    print("   - tab_amount: Number of browser tabs to open")
    print("   - watch_time: Time to watch video in seconds")
    print("   - view_cycles: Number of view cycles to perform")
    print("   - browser: Browser to use (firefox, chrome, edge, etc.)")
    print()
    print("3. Run the bot:")
    print("   python main.py")
    print()
    print("Note: Make sure you have the selected browser installed on your system!")
    print()

def main():
    """Main setup function"""
    print_header("YouTube View Bot - Setup")
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Step 1: Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed during dependency installation")
        sys.exit(1)
    
    # Step 3: Verify dependencies
    if not verify_dependencies():
        print("\n❌ Setup failed: Some dependencies are not installed properly")
        sys.exit(1)
    
    # Step 4: Create configuration
    config_ready = create_config()
    
    # Show next steps
    show_next_steps()
    
    if config_ready:
        print("✅ Setup is complete and ready to run!")
    else:
        print("⚠️  Setup is almost complete - please configure your video URL in config.json")
    
    print()

if __name__ == "__main__":
    main()
