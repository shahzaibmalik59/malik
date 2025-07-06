from flask import Flask, request, send_file, send_from_directory
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('templates', 'tts.html')

@app.post('/synthesize')
def synthesize():
    data = request.get_json(force=True)
    text = data.get('text', '')
    lang = data.get('lang', 'en')
    if not text:
        return 'No text provided', 400
    tts = gTTS(text=text, lang=lang)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return send_file(mp3_fp, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)

