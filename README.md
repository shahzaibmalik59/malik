# malik

This repository contains a simple website and a Python script for text-to-speech (TTS).

## Text to Speech

`text_to_speech.py` is a command-line utility that converts text to speech using the [gTTS](https://pypi.org/project/gTTS/) library. It can read text directly from the command line or from a file and save the output as an MP3 file.

### Usage

```bash
pip install gTTS --user
python3 text_to_speech.py "Hello world" -o hello.mp3
# or from a file
python3 text_to_speech.py input.txt -o output.mp3
```

The `--lang` option allows setting the language (default is English).

## Web Interface

A small Flask server provides a web-based text-to-speech interface.
Install the dependencies and run the server:

```bash
pip install flask gTTS --user
python3 tts_server.py
```

Then open `http://localhost:5000` in your browser. Enter text, choose a language,
and click **Speak** to hear the synthesized audio.

