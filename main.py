from speech import speak, listen
from commands import process_command


# ============================================================
# EVA MAIN PROGRAM
# ============================================================

def main():

    speak(
        "Hello! I am EVA. "
        "How can I help you?"
    )

    while True:

        command = listen()

        if command == "":
            continue

        should_continue = process_command(
            command
        )

        if not should_continue:
            break


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()