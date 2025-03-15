# routes.py
import os
import uuid
import yt_dlp
from .funcoes import my_hook, progress_stream, MyLogger
from werkzeug.utils import secure_filename
from flask import render_template, request, send_file, Blueprint, jsonify, Response




auth_bp = Blueprint('auth', __name__)


# Obtém o diretório atual do arquivo
base_dir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(base_dir, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Rota principal
@auth_bp.route('/')
def index():
    return render_template('index.html')
    
    
@auth_bp.route('/termos')
def termos():
    return render_template('termos.html')
    
    
@auth_bp.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')

@auth_bp.route('/progress')
def progress():
    return Response(progress_stream(), mimetype='text/event-stream')



# rota formulário
@auth_bp.route('/upload_youtube', methods=['POST'])
def upload_youtube():
    url = request.form.get('youtube_url')
    
    if not url:
        return jsonify({'success': False, 'error': 'Nenhum URL inserido!'})
    
    try:
        # Usa yt-dlp para baixar o vídeo do YouTube
        unique_id = uuid.uuid4()
        ydl_opts = {
            'cookiefile': os.path.join(base_dir, 'cookies.txt'),
            'proxy': '',
            'progress_hooks': [my_hook],
            'logger': MyLogger(),
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(UPLOAD_FOLDER, f'%(title)s_{unique_id}.%(ext)s'),
                'proxy': '',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': request.form.get('quality', default='128'),
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            base_filename = ydl.prepare_filename(info_dict)
            mp3_filename = os.path.splitext(base_filename)[0]
            
            
            
# Detectando a extensão do arquivo baixado
            for ext in ['.mp4', '.webm', '.mkv','.mp3','.m4a']:
                if os.path.exists(mp3_filename + ext):
                    mp3_filename += ext
                    break
            else:
                print(f" arquivo video não existe: {mp3_filename}")
                return jsonify({'success': False, 'error': 'Ocorreu um erro ao processar '})
                
                
                # Sanitizando o nome do arquivo
        mp3_filename_safe = secure_filename(os.path.basename(mp3_filename))
        mp3_path_safe = os.path.join(UPLOAD_FOLDER, mp3_filename_safe)
        os.rename(mp3_filename, mp3_path_safe)

        print(f" arquivo video existe: {mp3_path_safe}")
        

        return jsonify({'success': True, 'mp3_filename': os.path.basename(mp3_path_safe)})

    except Exception as e:
        return jsonify({'success': False, 'error': f'Erro: {e}'})

@auth_bp.route('/download/<mp3_filename>')
def download_file(mp3_filename):
    try:
        # Sanitizando o nome do arquivo recebido na URL
        mp3_filename_safe = secure_filename(mp3_filename)
        return send_file(os.path.join(UPLOAD_FOLDER, mp3_filename_safe), as_attachment=True)
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        return jsonify({'error': f'O arquivo solicitado não foi encontrado. Erro: {e}'})