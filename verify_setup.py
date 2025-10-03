#!/usr/bin/env python3
"""
Verify YouTube View Bot Setup
Quick script to check if everything is configured correctly
"""

import sys
import json
import os

def check_dependencies():
    """Check if all dependencies are installed"""
    print("Checking dependencies...")
    
    missing = []
    
    try:
        import selenium
        print("  ✅ selenium")
    except ImportError:
        print("  ❌ selenium")
        missing.append("selenium")
    
    try:
        import webdriver_manager
        print("  ✅ webdriver-manager")
    except ImportError:
        print("  ❌ webdriver-manager")
        missing.append("webdriver-manager")
    
    try:
        import requests
        print("  ✅ requests")
    except ImportError:
        print("  ❌ requests")
        missing.append("requests")
    
    return missing

def check_config():
    """Check if config.json is properly configured"""
    print("\nChecking configuration...")
    
    if not os.path.exists('config.json'):
        print("  ❌ config.json not found")
        return False
    
    print("  ✅ config.json exists")
    
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        # Check required fields
        required_fields = ['website', 'tab_amount', 'watch_time', 'view_cycles', 'browser']
        
        for field in required_fields:
            if field not in config:
                print(f"  ❌ Missing field: {field}")
                return False
        
        print("  ✅ All required fields present")
        
        # Check if website is configured
        if config['website'] in ['YOUR VIDEO', 'YOUR_VIDEO', '']:
            print("  ⚠️  Warning: 'website' field has placeholder value")
            print("     Please set it to your YouTube video URL")
            return False
        
        if not config['website'].startswith('http'):
            print("  ⚠️  Warning: 'website' should be a full URL")
            return False
        
        print(f"  ✅ Video URL: {config['website']}")
        print(f"  ✅ Browser: {config['browser']}")
        print(f"  ✅ Tabs: {config['tab_amount']}")
        print(f"  ✅ Watch time: {config['watch_time']}s")
        print(f"  ✅ View cycles: {config['view_cycles']}")
        
        return True
        
    except json.JSONDecodeError:
        print("  ❌ config.json is not valid JSON")
        return False
    except Exception as e:
        print(f"  ❌ Error reading config.json: {e}")
        return False

def main():
    """Main verification function"""
    print("="*60)
    print("  YouTube View Bot - Setup Verification")
    print("="*60 + "\n")
    
    # Check dependencies
    missing_deps = check_dependencies()
    
    # Check configuration
    config_ok = check_config()
    
    # Summary
    print("\n" + "="*60)
    print("  Summary")
    print("="*60)
    
    if missing_deps:
        print("\n❌ Setup incomplete!")
        print(f"\nMissing dependencies: {', '.join(missing_deps)}")
        print("\nTo install missing dependencies, run:")
        print("  pip install -r requirements.txt")
        print("\nOr run the setup script:")
        print("  python setup.py")
        sys.exit(1)
    
    if not config_ok:
        print("\n⚠️  Setup almost complete!")
        print("\nPlease configure your video URL in config.json")
        print("Edit config.json and set the 'website' field to your YouTube video URL")
        sys.exit(1)
    
    print("\n✅ Setup complete! Ready to run!")
    print("\nTo start the bot, run:")
    print("  python main.py")
    print()

if __name__ == "__main__":
    main()
