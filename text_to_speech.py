from gtts import gTTS
import argparse


def text_to_speech(text, lang, output):
    tts = gTTS(text=text, lang=lang)
    tts.save(output)
    print(f"Saved synthesized speech to {output}")


def main():
    parser = argparse.ArgumentParser(description="Simple text to speech using gTTS")
    parser.add_argument('text', help='Text to convert or path to a text file')
    parser.add_argument('-l', '--lang', default='en', help='Language code (default: en)')
    parser.add_argument('-o', '--output', default='output.mp3', help='Output MP3 file name')
    args = parser.parse_args()

    # If the text argument is a file, read from file
    try:
        with open(args.text, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        text = args.text

    text_to_speech(text, args.lang, args.output)


if __name__ == '__main__':
    main()
