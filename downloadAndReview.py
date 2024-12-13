import pyautogui
import keyboard
import time


def open_microsoft_store():
    """
    Open the Microsoft Store application.
    """
    keyboard.press_and_release('win + s')  # Open search
    time.sleep(1)
    pyautogui.typewrite("Microsoft Store")  # Type "Microsoft Store"
    time.sleep(1)
    keyboard.press_and_release('enter')  # Open Microsoft Store
    time.sleep(5)  # Wait for the app to open


def sign_in_with_username_and_pass(username, password):
    """
    Sign in to Microsoft Store using a username and password.
    
    :param username: The username for sign-in
    :param password: The password for sign-in
    """
    try:
        # Open search menu
        keyboard.press_and_release('ctrl + f')
        time.sleep(1)

        # Tab to profile menu
        keyboard.press_and_release('tab')
        time.sleep(1)

        # Enter to open profile menu
        keyboard.press_and_release('enter')
        time.sleep(2)

        # Check for sign-out button
        try:
            sign_out_location = pyautogui.locateOnScreen("imageSignOut.png",
                                                         confidence=0.8)
        except Exception as e:
            print(f"Error locating sign-out button: {e}")
            sign_out_location = None

        if sign_out_location:
            # Click on sign-out button
            center_x, center_y = pyautogui.center(sign_out_location)
            pyautogui.move(center_x, center_y)
            keyboard.press_and_release('enter')
            print("Signed out successfully.")

            # Click on sign-in button after signing out
            time.sleep(2)  # Wait for UI to refresh

            sign_in_location = pyautogui.locateOnScreen("imageSignIn.png",
                                                        confidence=0.8)
            if sign_in_location:
                center_x, center_y = pyautogui.center(sign_in_location)
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                keyboard.press_and_release('enter')
                print("Sign-in button clicked...")
            else:
                print("Sign-in button not found.")
        else:
            # Click on sign-in button
            sign_in_location = pyautogui.locateOnScreen("imageSignIn.png",
                                                        confidence=0.8)
            if sign_in_location:
                center_x, center_y = pyautogui.center(sign_in_location)
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                keyboard.press_and_release('enter')
                print("Sign-in button clicked...")
            else:
                print("Sign-in button not found.")
        time.sleep(4)
        try:
            microsoft_icon = pyautogui.locateOnScreen("image.png",
                                                      confidence=0.8)

            if microsoft_icon:
                center_x, center_y = pyautogui.center(microsoft_icon)
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                keyboard.press_and_release('tab')
                keyboard.press_and_release('enter')
                time.sleep(2)
                print("Microsoft icon clicked.")
                pyautogui.typewrite(username)
                keyboard.press_and_release('tab')
                keyboard.press_and_release('tab')
                keyboard.press_and_release('enter')
                time.sleep(4)
                pyautogui.typewrite(password)
                keyboard.press_and_release('tab')
                keyboard.press_and_release('tab')
                keyboard.press_and_release('enter')
                time.sleep(3)
            else:
                print("Microsoft icon not found.")
        except Exception as e:
            print(f"Error finding ms icon: {e}")

    except Exception as e:
        print(f"Error signing in: {e}")


def search_in_store(search_term):
    """
    Search for a specific term in Microsoft Store using the search bar.
    
    :param search_term: The term to search for.
    """
    time.sleep(3)  # Wait for search bar to load
    keyboard.press_and_release('ctrl + f')  # Focus on search
    time.sleep(1)
    keyboard.press_and_release('ctrl + a')  # Select existing text
    keyboard.press_and_release('backspace')  # Clear text
    pyautogui.typewrite(search_term)  # Type the search term
    time.sleep(2)
    keyboard.press_and_release('enter')  # Start search


def click_on_search_result():
    """
    Click on the first search result in Microsoft Store.
    """
    try:
        # Locate the app logo and click it
        db_location = pyautogui.locateOnScreen(
            "imagePDFConvertor.png", confidence=0.8)
        if db_location:
            center_x, center_y = pyautogui.center(db_location)
            pyautogui.click(center_x, center_y)
            time.sleep(4)
        else:
            print("App logo not found.")
    except Exception as e:
        print(f"Error clicking on search result: {e}")

def install_app():
    """
    Install the app by clicking on the 'Install' button.
    """
    try:
        # Locate the 'Install' button
        install_button = pyautogui.locateOnScreen(
            "install.png", confidence=0.8)
        if install_button:
            center_x, center_y = pyautogui.center(install_button)
            pyautogui.click(center_x, center_y)
            print("App installation started.")
        else:
            print("Install button not found.")
    except Exception as e:
        print(f"Error installing app: {e}")

def scroll_and_click_review():
    """
    Scroll down and find the 'Write a Review' button, then click it.
    """
    try:
        # Scroll the page down
        for _ in range(5):
            pyautogui.scroll(-300)
            time.sleep(1)

        # Locate the 'Write a Review' button and click it
        review_button = pyautogui.locateOnScreen(
            "imageWriteRV.png", confidence=0.8)
        if review_button:
            center_x, center_y = pyautogui.center(review_button)
            pyautogui.click(center_x, center_y)
        else:
            print("Write a Review button not found.")
    except Exception as e:
        print(f"Error finding or clicking the 'Write a Review' button: {e}")


def give_five_star_review():
    """
    Locate all stars on the review section and click on the last one for a 5-star review.
    """
    try:
        # Find all star icons on the screen
        star_locations = list(pyautogui.locateAllOnScreen(
            "imageStar.png", confidence=0.8))

        if not star_locations:
            print("No stars found. Ensure the image is accurate and visible.")
            return

        # Get the location of the last (5th) star
        last_star = star_locations[-1]
        center_x, center_y = pyautogui.center(last_star)

        # Click on the last star
        pyautogui.click(center_x, center_y)
        print("5-star rating given successfully.")
    except Exception as e:
        print(f"Error giving a 5-star review: {e}")


def write_rating(title, description):
    """
    Write a review title and description.

    :param title: The review title
    :param description: The review description
    """
    try:
        # Click on the title field
        # Replace with actual coordinates of the title field
        # pyautogui.click(100, 200)
        keyboard.press_and_release('tab')
        time.sleep(1)

        # Type the title
        pyautogui.typewrite(title)
        time.sleep(1)

        # Press Tab to move to the description field
        keyboard.press_and_release('tab')
        time.sleep(1)

        # Type the description
        pyautogui.typewrite(description)
        time.sleep(1)
    except Exception as e:
        print(f"Error writing rating: {e}")


def submit_rating():
    """
    Submit the review by clicking Tab twice and pressing Enter.
    """
    try:
        # Press Tab twice to move focus to the submit button
        keyboard.press_and_release('tab')
        time.sleep(0.5)
        keyboard.press_and_release('tab')
        time.sleep(0.5)

        # Press Enter to submit
        keyboard.press_and_release('enter')
        print("Review submitted successfully.")
    except Exception as e:
        print(f"Error submitting rating: {e}")


def main():
    pyautogui.FAILSAFE = False
    try:
        print("Starting automation...")
        open_microsoft_store()
        # sign_in_with_username_and_pass(
        #     "", "password")
        search_in_store("pdf converter x pro")
        time.sleep(5)
        click_on_search_result()
        time.sleep(5)
        install_app()
        time.sleep(120) # Wait for installation to complete
        scroll_and_click_review()
        time.sleep(3)
        give_five_star_review()
        time.sleep(3)
        write_rating("Great app!", "Awesome features and functionality.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print("Script will run in 3 seconds. Switch to the correct window.")
    time.sleep(3)
    main()
