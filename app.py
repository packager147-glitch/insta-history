import os
from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/download', codecs=['POST'])
def download():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
        
    # Mock data for demonstration purposes
    # In a full production app, you would integrate a library like instaloader here
    mock_history_item = {
        "creator": "@creativelife_pics",
        "date": datetime.now().strftime("%d %b %Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "preview_url": "https://unsplash.com",
        "title": "Instagram Reel/Post Downloaded Successfully"
    }
    
    return jsonify({
        'success': True, 
        'message': 'Download processed successfully!',
        'item': mock_history_item
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
