from flask import Flask, request, send_file, render_template, redirect, url_for
import os
import subprocess
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 设置文件上传的目标文件夹
UPLOAD_FOLDER = r'C:\photo'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 设置AVIF文件保存路径
AVIF_FOLDER = r'C:\avif'
if not os.path.exists(AVIF_FOLDER):
    os.makedirs(AVIF_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_filename = f"{timestamp}.avif"
    output_path = compress_media(filepath, output_filename)
    if output_path is None:
        return {'success': False}
    
    return {'success': True, 'file_url': url_for('download_file', name=os.path.basename(output_path)), 'filename': os.path.basename(output_path)}

@app.route('/download/<name>')
def download_file(name):
    return send_file(os.path.join(AVIF_FOLDER, name), as_attachment=True)

def compress_media(input_path, output_filename):
    output_path = os.path.join(AVIF_FOLDER, output_filename)
    
    if input_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        command = ['ffmpeg', '-i', input_path, '-vf', 'scale=-2:ih', '-c:v', 'libsvtav1', '-crf', '36', '-pix_fmt', 'yuv420p', output_path]
    else:  
        command = ['ffmpeg', '-i', input_path, '-vf', 'scale=-2:ih', '-c:v', 'libsvtav1', '-crf', '36', '-pix_fmt', 'yuv420p', '-an', output_path]
    
    try:
        result = subprocess.run(command, check=True, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Command output: {e.stderr}")
        return None
    
    return output_path

if __name__ == '__main__':
    app.run(debug=True)
