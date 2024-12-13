import pyautogui
import keyboard
import time


def open_settings_accounts_other_users():
    # Open Windows Settings using Win + I
    keyboard.press_and_release('win+i')
    time.sleep(2)  # Wait for Settings to open

    # Maximize the Settings window
    # Simulate Win + Up Arrow to maximize the window
    # keyboard.press_and_release('win+up')
    time.sleep(1)

    search_image = pyautogui.locateOnScreen("image.png")
    center_x, center_y = pyautogui.center(search_image)
    pyautogui.click(center_x, center_y)
    # Navigate to 'Accounts'
    # pyautogui.write('accounts')  # Type 'accounts' in the search bar
    # time.sleep(5)
    # keyboard.press_and_release('enter')  # Open Accounts settings
    # time.sleep(5)

    # # Navigate to 'Other users'
    # # Adjust tab count based on system layout
    # pyautogui.press('tab', presses=5, interval=0.2)
    # # Navigate to 'Other users' in the menu
    # pyautogui.press('down', presses=3, interval=0.5)
    # pyautogui.press('enter')  # Select 'Other users'

    print("Settings > Accounts > Other Users should now be open.")


# Execute the function
open_settings_accounts_other_users()
