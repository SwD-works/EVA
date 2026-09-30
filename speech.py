import speech_recognition as sr
import pyttsx3


# ============================================================
# TEXT-TO-SPEECH ENGINE TTS(engine)
# ============================================================

engine = pyttsx3.init()


# ============================================================
# SELECT FEMALE VOICE - MICROSOFT ZIRA
# ============================================================

voices = engine.getProperty("voices")

for voice in voices:
    if "ZIRA" in voice.id.upper():
        engine.setProperty("voice", voice.id)
        break


# Voice settings
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)


# ============================================================
# SPEAK(speak function)
# ============================================================

def speak(text):
    """
    Converts text into speech.
    """

    print("EVA:", text)

    engine.say(text)
    engine.runAndWait()


# ============================================================
# LISTEN
# ============================================================

def listen():
    """
    Listens to the microphone and converts
    speech into text.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            print("Processing...")

            text = recognizer.recognize_google(audio)

            print("You:", text)

            return text.lower()

        except sr.WaitTimeoutError:

            print("No speech detected.")

            return ""

        except sr.UnknownValueError:

            print("Sorry, I couldn't understand that.")

            speak(
                "Sorry, I couldn't understand that."
            )

            return ""

        except sr.RequestError:

            print(
                "Speech recognition service is unavailable."
            )

            speak(
                "Sorry, the speech recognition service "
                "is unavailable."
            )

            return ""