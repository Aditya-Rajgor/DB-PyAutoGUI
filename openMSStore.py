import pyautogui
import keyboard
import time


def open_microsoft_store():
    """
    Open the Microsoft Store application
    """
    # Windows key + S to open search
    keyboard.press_and_release('win + s')
    time.sleep(1)

    # Type "Microsoft Store"
    pyautogui.typewrite("Microsoft Store")
    time.sleep(1)

    # Press Enter to open
    keyboard.press_and_release('enter')
    time.sleep(3)  # Give time for the app to open


def search_in_store(search_term):
    """
    Search for a specific term in Microsoft Store using Ctrl+F
    
    :param search_term: The term to search for
    """
    # Use Ctrl+F to focus on search
    time.sleep(3)
    keyboard.press_and_release('ctrl + f')
    time.sleep(1)

    # Clear any existing text
    keyboard.press_and_release('ctrl + a')
    keyboard.press_and_release('backspace')

    # Type search term
    pyautogui.typewrite(search_term)
    time.sleep(2)

    # Press Enter to search
    keyboard.press_and_release('enter')

def click_on_search_result():
    """
    Click on the first search result in Microsoft Store
    """
    # Press Tab to focus on the first search result
    DB_location = pyautogui.locateOnScreen("imageDBLogo.png", confidence=0.8)
    center_x, center_y = pyautogui.center(DB_location)
    # pyautogui.moveTo(center_x, center_y)
    pyautogui.click(center_x, center_y)
    # pyautogui.click(center_x, center_y)

    # Press Enter to open the app
    # keyboard.press_and_release('enter')
    time.sleep(4)

def install_app():
    """
    Install the app from the Microsoft Store
    """
    # Press Alt + I to install the app
    # keyboard.press_and_release('alt + i')
    time.sleep(3)
    pyautogui.locateOnScreen("imageGet.png", confidence=0.8)
    time.sleep(1)

    # Press Enter to confirm installation
    keyboard.press_and_release('enter')
    time.sleep(1)



def main():
    # try:
    # Open Microsoft Store
    open_microsoft_store()

    # Search for Drawboard PDF
    search_in_store("Drawboard PDF")

    time.sleep(5)# print("Search completed successfully!")
    click_on_search_result()

    # Install the app
    # install_app()

    # except Exception as e:
    #     print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Add a small delay to allow you to switch to the correct window if needed
    print("Script will run in 3 seconds. Switch to the correct window.")
    time.sleep(3)

    main()
