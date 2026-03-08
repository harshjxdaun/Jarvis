# 🤖 Jarvis — Voice Assistant

A Python-based voice assistant that listens for a wake word and responds to spoken commands. Jarvis can open websites, play music, and more — all hands-free.

---

## Features

-  **Wake word activation** — Say `"Jarvis"` to activate
-  **Open websites** — YouTube, Google, Facebook, Twitter, Instagram
-  **Play music** — Looks up songs from your music library and opens them in the browser
-  **Text-to-speech responses** — Jarvis talks back using `pyttsx3`
-  **Voice shutdown** — Say `"stop"` to exit gracefully

---

##  Requirements

- Python 3.7+
- A working microphone
- Internet connection (for Google Speech Recognition)

### Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

> **Note on PyAudio:** On some systems you may need to install it differently:
> - **macOS:** `brew install portaudio && pip install pyaudio`
> - **Linux:** `sudo apt-get install python3-pyaudio`
> - **Windows:** Download the appropriate `.whl` from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with `pip install <file>.whl`

---

## Project Structure

```
music-chatbot
 ├ main.py                  # Main Assistant Script
 ├ musiclibrary.py          # Music Library Dictionary
 ├ requirements.txt
 ├ README.md
 └ .gitignore               # Removing Cache Files
```

### Adding Songs to the Music Library

The `musicLibrary.py` file contains a dictionary of song names mapped to URLs:

```python
music = {
    "can't tell me nothing" : "https://www.youtube.com/watch?v=E58qLXBfLrs",
    "flashing lights" : "https://www.youtube.com/watch?v=ZAz3rnLGthg",
    "heartless" : "https://www.youtube.com/watch?v=Co0tTeuUVhU",
    "homecoming" : "https://www.youtube.com/watch?v=LQ488QrqGE4",
    "power" : "https://www.youtube.com/watch?v=Dw8B1q1tKgs",
    "big brother" : "https://www.youtube.com/watch?v=HInIGGXhJHs",
    "runaway" : "https://www.youtube.com/watch?v=cv1naUa3_3g",
    "devil in a new dress" : "https://www.youtube.com/watch?v=sk3rpYkiHe8",
    "touch the sky" : "https://www.youtube.com/watch?v=B95OUKk7alM",

    "careless whisper" : "https://www.youtube.com/watch?v=izGwDsrQ1eQ",

    "blinding lights" : "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "starboy" : "https://www.youtube.com/watch?v=34Na4j8AVgA",
    "timelesss" : "https://www.youtube.com/watch?v=5EpyN_6dqyk",

    "united in grief" : "hhttps://www.youtube.com/watch?v=tvNSXS4x9nc",
    "pride" : "https://www.youtube.com/watch?v=J87pJrxvJ5E",
    
    "angel" : "https://www.youtube.com/watch?v=66A_3uwuZ_I"
}
```

To add a new song, just add a new entry to the `music` dictionary and say `"play <song name>"` to Jarvis.

---

## Usage

Run the assistant:

```bash
python main.py
```

### How It Works

1. Jarvis greets you on startup
2. It continuously listens for the wake word **"Jarvis"**
3. Once activated, it listens for your command
4. Supported commands:

| Command | Action |
|---|---|
| `"open youtube"` | Opens YouTube in browser |
| `"open google"` | Opens Google in browser |
| `"open facebook"` | Opens Facebook in browser |
| `"open twitter"` | Opens Twitter in browser |
| `"open instagram"` | Opens Instagram in browser |
| `"play <song name>"` | Plays the song from your music library |
| `"stop"` | Shuts down Jarvis |

---

## Configuration

You can tweak the following values in `main.py`:

| Parameter | Default | Description |
|---|---|---|
| `phrase_time_limit` (wake word) | `5` seconds | Max listening time for wake word |
| `timeout` (wake word) | `5` seconds | How long to wait before giving up |
| `phrase_time_limit` (command) | `10` seconds | Max time to capture a command |
| `timeout` (command) | `10` seconds | Command listen timeout |

---

## Known Limitations

- Requires an active internet connection for speech recognition (uses Google's API)
- Music playback opens songs in a browser window rather than a native player

---

## License

This project is open source and available under the [MIT License].
 