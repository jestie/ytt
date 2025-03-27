from flask import Flask, request, jsonify, send_from_directory
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import socket

app = Flask(__name__)

# Configure logging (same as before)
log_dir = 'logs'
if not os.path.exists(log_dir):
    try:
        os.makedirs(log_dir)
    except OSError as e:
        print(f"Error creating log directory: {e}")
        log_dir = None

if log_dir:
    log_file_path = os.path.join(log_dir, 'app.log')
    log_handler = TimedRotatingFileHandler(
        log_file_path,
        when="midnight",
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
    log_handler.setLevel(logging.ERROR)
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_formatter)
    app.logger.addHandler(log_handler)
    app.logger.setLevel(logging.ERROR)

@app.route('/get_transcript')
def get_transcript():
    video_id = request.args.get('video_id')

    if not video_id:
        if log_dir:
            app.logger.error("Video ID is missing in the request.")
        return jsonify({'error': 'Video ID is required'}), 400

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        #modified area
        transcript = [{'text': t['text'], 'start': t['start']} for t in transcript_list]
        return jsonify({'transcript': transcript})

    except TranscriptsDisabled:
        if log_dir:
            app.logger.error(f"Transcripts are disabled for video ID: {video_id}")
        return jsonify({'error': 'Transcripts are disabled for this video.'}), 400
    except VideoUnavailable:
        if log_dir:
            app.logger.error(f"Video unavailable for video ID: {video_id}")
        return jsonify({'error': 'Video is unavailable.'}), 400
    except Exception as e:
        if log_dir:
            app.logger.exception(f"An unexpected error occurred for video ID: {video_id}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

def find_available_port(start_port=4000):
    """Finds an available port starting from start_port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while start_port < 65535:  # Maximum port number
        try:
            sock.bind(('127.0.0.1', start_port))
            sock.close()
            return start_port
        except socket.error:
            start_port += 1
    return None  # No available port found

if __name__ == '__main__':
    port = find_available_port()
    if port:
        print(f"Running Flask app on http://127.0.0.1:{port}")
        app.run(port=port, debug=True)
    else:
        print("Could not find an available port.")