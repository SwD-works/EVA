import re

from speech import speak

from actions import (
    open_website,
    search_google,
    tell_time,
    open_notepad,
    open_calculator,
    open_file_explorer
)


# ============================================================
# COMMAND PROCESSOR
# ============================================================

def process_command(command):

    """
    Processes the user's command using Regex.
    """

    command = command.strip()


    # ========================================================
    # EXIT
    # ========================================================

    exit_pattern = (
        r"\b(exit|quit|stop|goodbye)\b"
    )

    if re.search(exit_pattern, command):

        speak(
            "Goodbye! Have a nice day."
        )

        return False


    # ========================================================
    # TIME
    # ========================================================

    time_pattern = (
        r"\b("
        r"what(?:'s| is)? the time"
        r"|tell me the time"
        r"|current time"
        r"|time"
        r")\b"
    )

    if re.search(time_pattern, command):

        tell_time()

        return True


    # ========================================================
    # OPEN YOUTUBE
    # ========================================================

    youtube_pattern = (
        r"\b(open|launch|start)\b.*\byoutube\b"
    )

    if re.search(
        youtube_pattern,
        command
    ):

        open_website(
            "YouTube",
            "https://www.youtube.com"
        )

        return True


    # ========================================================
    # OPEN GOOGLE
    # ========================================================

    google_pattern = (
        r"\b(open|launch|start)\b.*\bgoogle\b"
    )

    if re.search(
        google_pattern,
        command
    ):

        open_website(
            "Google",
            "https://www.google.com"
        )

        return True


    # ========================================================
    # OPEN GMAIL
    # ========================================================

    gmail_pattern = (
        r"\b(open|launch|start)\b.*"
        r"\b(gmail|mail)\b"
    )

    if re.search(
        gmail_pattern,
        command
    ):

        open_website(
            "Gmail",
            "https://mail.google.com"
        )

        return True


    # ========================================================
    # OPEN NOTEPAD
    # ========================================================

    notepad_pattern = (
        r"\b(open|launch|start)\b.*"
        r"\bnotepad\b"
    )

    if re.search(
        notepad_pattern,
        command
    ):

        open_notepad()

        return True


    # ========================================================
    # OPEN CALCULATOR
    # ========================================================

    calculator_pattern = (
        r"\b(open|launch|start)\b.*"
        r"\b(calculator|calc)\b"
    )

    if re.search(
        calculator_pattern,
        command
    ):

        open_calculator()

        return True


    # ========================================================
    # OPEN FILE EXPLORER
    # ========================================================

    explorer_pattern = (
        r"\b(open|launch|start)\b.*"
        r"\b(file explorer|explorer|files)\b"
    )

    if re.search(
        explorer_pattern,
        command
    ):

        open_file_explorer()

        return True


    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    search_pattern = (
        r"\b(search|google)\b"
        r"(?:\s+for)?\s+(.+)"
    )

    search_match = re.search(
        search_pattern,
        command
    )

    if search_match:

        query = search_match.group(1).strip()

        search_google(query)

        return True


    # ========================================================
    # UNKNOWN COMMAND
    # ========================================================

    speak(
        "Sorry, I don't know how to perform "
        "that command yet."
    )

    return True