import webbrowser
import subprocess
from datetime import datetime
from speech import speak


# ============================================================
# WEBSITE ACTIONS
# ============================================================

def open_website(name, url):

    """
    Opens a website in the default browser.
    """

    speak("Opening " + name)

    webbrowser.open(url)


# ============================================================
# GOOGLE SEARCH
# ============================================================

def search_google(query):

    """
    Searches Google for a query.
    """

    speak("Searching for " + query)

    search_url = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
    )

    webbrowser.open(search_url)


# ============================================================
# SHOW CURRENT TIME
# ============================================================

def tell_time():

    """
    Gets and announces the current time.
    """

    current_time = datetime.now().strftime(
        "%I:%M %p"
    )

    speak(
        "The current time is "
        + current_time
    )


# ============================================================
# WINDOWS APPLICATIONS
# ============================================================

def open_notepad():

    """
    Opens Windows Notepad.
    """

    speak("Opening Notepad")

    subprocess.Popen("notepad.exe")


def open_calculator():

    """
    Opens Windows Calculator.
    """

    speak("Opening Calculator")

    subprocess.Popen("calc.exe")


def open_file_explorer():

    """
    Opens Windows File Explorer.
    """

    speak("Opening File Explorer")

    subprocess.Popen("explorer.exe")