import time
import pyautogui
import keyboard


def open_settings_your_info():
    try:
        # Step 1: Open Windows Settings
        keyboard.press_and_release("win + i")
        time.sleep(5)  # Wait for Settings to open

        # Step 2: Type 'Your info' in the search bar
        # Adjust coordinates based on your screen to focus on the search bar
        pyautogui.click(50, 50)
        pyautogui.typewrite("Your info")
        time.sleep(5)

        # Step 3: Press Enter to navigate to "Your Info" section
        keyboard.press_and_release("enter")
        time.sleep(5)

        print("Navigated to 'Settings → Accounts → Your Info'")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
open_settings_your_info()
