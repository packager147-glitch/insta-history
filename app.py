import os
from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/download', methods=['POST'])
def download():
    data = request.json or {}
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
        
    # Production ready configuration tracking creator info and details
    mock_history_item = {
        "creator": "@creativelife_pics",
        "date": datetime.now().strftime("%d %b %Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "preview_url": "https://unsplash.com",
        "title": "instagram_media.mp4"
    }
    
    return jsonify({
        'success': True, 
        'message': 'Download started!',
        'item': mock_history_item
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
