from flask import Flask, render_template, request, jsonify
import os
from parser import parse_resume

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['resume']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    result = parse_resume(file_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)