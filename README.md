# Jarvis: Voice Command Based Bot

## Overview

Jarvis is a voice-command-based bot designed to assist with various tasks using Python. It leverages speech recognition, text-to-speech, and online search functionalities to provide an interactive experience. Currently under development, Jarvis can perform Google searches, YouTube searches, and respond to various commands.

---

## Features

1. **Voice-Activated Commands:**

   * Recognizes and executes voice commands using the SpeechRecognition library.
2. **Greetings:**

   * Randomized greetings to start the session with a personalized touch.
3. **Online Search:**

   * Search the web using Google.
   * Play videos or search content on YouTube.
4. **System Commands:**

   * Stop the system.
   * Pause for a specified duration (e.g., 30 seconds).
   * Enter a sleep mode for extended breaks (e.g., 5 minutes).
5. **Text-to-Speech:**

   * Jarvis communicates with the user through a speech engine, making interactions more engaging.

---

## Prerequisites

Before running the code, ensure you have the following libraries installed:

1. **Python 3.x**
2. Required Libraries:

   * `pyttsx3`: Text-to-speech conversion.
   * `speech_recognition`: Recognizes voice commands.
   * `pyaudio`: Audio stream handling.
   * `pywhatkit`: Enables Google and YouTube searches.

Install these libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition pyaudio pywhatkit
```

---

## How It Works

1. Jarvis starts with a greeting selected randomly from a predefined list.
2. It listens for user commands through the microphone.
3. Based on the recognized command, Jarvis performs the appropriate action.
4. The system responds with text-to-speech output for better interactivity.

---

## Supported Commands

| Command             | Action                                                    |
| ------------------- | --------------------------------------------------------- |
| "stop system core"  | Terminates the Jarvis bot.                                |
| "wait for sometime" | Pauses the bot for 30 seconds.                            |
| "go to sleep"       | Puts the bot into a sleep mode for 5 minutes.             |
| "search on Google"  | Prompts the user to specify a query to search on Google.  |
| "search on YouTube" | Prompts the user to specify a query to search on YouTube. |

---

## Usage

1. Clone or download the code to your local machine.
2. Ensure all prerequisites are installed.
3. Run the script using:

   ```bash
   python jarvis.py
   ```
4. Interact with Jarvis using voice commands.

---

## Example Interaction

1. Jarvis: "Hello master Tanmay, today is 20 May 2025. Listening for command..."
2. User: "Search on Google"
3. Jarvis: "Got it sir, what do you want to search?"
4. User: "Python tutorials"
5. Jarvis: (Opens a browser with the search results for "Python tutorials")

---

## Future Enhancements

* Add support for more commands and integrations.
* Enable task scheduling and reminders.
* Improve error handling and robustness.

---

## Troubleshooting

1. **"Could not understand audio":** Ensure the microphone is working properly and the environment is quiet.
2. **Library not found error:** Verify that all required libraries are installed using pip.
3. **Speech engine not working:** Check if `pyttsx3` is configured properly on your system.

---

## License

This project is for educational purposes and is currently under development.

---

Enjoy using Jarvis and feel free to contribute!
