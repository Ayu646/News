# Groq News Summarizer Flask API
import os
from flask import Flask, request, jsonify
from summarizer.summarizer import summarize_text
from transcribe.audio_transcriber import transcribe_audio
from transcribe.video_transcriber import transcribe_video
from feeds.feed_listener import process_text_feed
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

@app.route("/summarize/text", methods=["POST"])
def summarize_from_text():
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"error": "Missing 'text' field"}), 400
    summary = summarize_text(text, api_key=GROQ_API_KEY)
    return jsonify({"summary": summary})

@app.route("/summarize/audio", methods=["POST"])
def summarize_from_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    audio_file = request.files['file']
    text = transcribe_audio(audio_file)
    summary = summarize_text(text, api_key=GROQ_API_KEY)
    return jsonify({"transcription": text, "summary": summary})

@app.route("/summarize/video", methods=["POST"])
def summarize_from_video():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    video_file = request.files['file']
    text = transcribe_video(video_file)
    summary = summarize_text(text, api_key=GROQ_API_KEY)
    return jsonify({"transcription": text, "summary": summary})

@app.route("/summarize/feed", methods=["POST"])
def summarize_from_feed():
    data = request.json
    feed_text = data.get("text")
    if not feed_text:
        return jsonify({"error": "Missing 'text' field"}), 400
    processed_text = process_text_feed(feed_text)
    summary = summarize_text(processed_text, api_key=GROQ_API_KEY)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
