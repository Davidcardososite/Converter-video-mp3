# funcoes.py
import threading
import time
import json
from tqdm import tqdm
import os



# Obtém o diretório atual do arquivo
base_dir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(base_dir, 'uploads')


progress_bar = None
progress_status = {'status': '', 'downloaded_bytes': 0, 'total_bytes': 0}




class MyLogger:
    def debug(self, msg):
        if msg.startswith('[debug]'):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        print(msg)
        pass

    def warning(self, msg):
        print(msg)
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    global progress_bar, progress_status, start_time

    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        if total is not None:
            if progress_bar is None:
                progress_bar = tqdm(total=total, unit='B', unit_scale=True)
                start_time = time.time()  # Inicia o timer
            progress_bar.update(d['downloaded_bytes'] - progress_bar.n)


            # Calcula a velocidade de download e o tempo restante
            elapsed_time = time.time() - start_time
            downloaded_bytes = d['downloaded_bytes']



            if elapsed_time > 0:
                speed = downloaded_bytes / elapsed_time  # Velocidade em bytes/s
                if speed > 0:
                    remaining_time = (total - downloaded_bytes) / speed  # Tempo restante em segundos
                else:
                    remaining_time = float('inf')  # Valor infinito, caso a velocidade seja zero
            else:
                speed = 0
                remaining_time = float('inf')  # Defina como infinito ou algum valor padrão



            speed_MB = speed / (1024 * 1024)  # Converte para MB/s


            # Formata a mensagem
            progress_status = {
                'status': 'downloading',
                'downloaded_bytes': d['downloaded_bytes'],
                'total_bytes': total,
                'speed': f"{speed_MB:.2f}MB/s",
                'time_remaining': f"{remaining_time:.2f}s",
                'elapsed_time': f"{elapsed_time:.2f}s"
            }

    elif d['status'] == 'finished':
        if progress_bar is not None:
            progress_bar.close()
            progress_bar = None
        progress_status = {'status': 'finished'}







def progress_stream():
    while True:
        progress_data = {
            'status': progress_status.get('status', ''),
            'downloaded_bytes': progress_status.get('downloaded_bytes', 0),
            'total_bytes': progress_status.get('total_bytes', 0),
            'speed': progress_status.get('speed', '0MB/s'),
            'time_remaining': progress_status.get('time_remaining', '0s'),
            'elapsed_time': progress_status.get('elapsed_time', '0s')
        }
        yield f"data: {json.dumps(progress_data)}\n\n"
        time.sleep(1)


# Função para limpar a pasta de uploads
def limpar_uploads():
    try:
        for video_path in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, video_path)
            if os.path.isfile(file_path):
                os.unlink(file_path)
    except Exception as e:
        print(f"Erro ao limpar a pasta de uploads: {e}")
    else:
        print(f'pasta uploads limpa!')

# Agendamento para limpar a pasta de uploads a cada 24 horas
def agendar_limpeza(intervalo=86400):
    limpar_uploads()
    threading.Timer(intervalo, agendar_limpeza, [intervalo]).start()
