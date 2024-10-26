# pip install pyautogui pillow

import pyautogui
import time
from datetime import datetime
import os

# Set the folder path where you want to save the screenshots
folder_path = "C:\\Users\\YSingh\\test\\screenshots"

os.makedirs(folder_path, exist_ok=True)

def take_screenshot():
    # Get the current time for the screenshot filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Set the full file path
    file_path = os.path.join(folder_path, f"screenshot_{timestamp}.png")
    # Take screenshot
    screenshot = pyautogui.screenshot()
    # Save the screenshot
    screenshot.save(file_path)
    print(f"Screenshot saved: {file_path}")

# Run the screenshot function every 30 seconds
while True:
    take_screenshot()
    time.sleep(10)

