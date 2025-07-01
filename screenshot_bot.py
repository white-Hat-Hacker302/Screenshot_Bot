import pyautogui
import time
import datetime
import os

# Banner
print("""
============================================================
          ScreenShotBot - Periodic Screenshot Capture
          Coded by Pakistani White Hat Hacker Mr Sabaz Ali Khan
                Contect Number +923409777222
                Email Sabazali236@gmail.com
           Mr Sabaz ali khan Cyber Security Engnier
============================================================
""")

def take_screenshot():
    # Create a folder for screenshots if it doesn't exist
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    # Generate timestamp for filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{screenshot_dir}/screenshot_{timestamp}.png"
    
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved: {filename}")

def main():
    # Configuration
    interval = 1  # Seconds between screenshots
    print(f"Starting ScreenShotBot with {interval}-second interval...")
    
    try:
        while True:
            take_screenshot()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nScreenShotBot stopped by user.")
        print("Thank you for using ScreenShotBot by Mr Sabaz Ali Khan!")

if __name__ == "__main__":
    main()