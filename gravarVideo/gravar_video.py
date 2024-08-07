import cv2
import time
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import os
from datetime import datetime

root_dir = os.path.abspath(os.sep)
print(root_dir)
# Define a duração da gravação em segundos
"""
câmeras pelotas
"http://root:digi2010@10.247.229.204/axis-cgi/mjpg/video.cgi"
#"rtsp://digifort:digi2010@10.247.220.79:554"
#"http://digifort:digi2010@10.247.220.79/axis-cgi/mjpg/video.cgi"
#"rtsp://digifort:digi2010@10.247.220.79:554/cam/realmonitor?channel=1&subtype=0"
#"rtsp://digifort:digi2010@10.247.220.138:554" emissões
#"rtsp://digifort:digi2010@10.247.220.79:554/cam/realmonitor?channel=1&subtype=0"
#"http://digifort:digi2010@10.247.220.79:80/cgi-bin/snapshot.cgi?"
#rtsp://digifort:digi2010@10.247.220.79:554/cam/realmonitor?channel=1&subtype=0
"""
duracao_gravacao = 30
camera = "rtsp://digifort:digi2010@10.247.229.204:554"
tentativas = 32256

def gravar_video(cam, tentativas):
    attempts = 0
    while attempts < tentativas:
        print(f"Connecting attempt {attempts + 1}")
        cap = cv2.VideoCapture(cam)
        # Loop para ler os frames do streaming e adicioná-los à lista
        if not cap.isOpened():
            print("Cannot open camera")
        else:
            # Inicializa a lista de frames
            frames = []
            # Obtém o tempo inicial
            tempo_inicial = time.time()
            while cap.isOpened():
                # Lê o frame atual do streaming
                ret, frame = cap.read()
                if ret:
                    # Convertendo o frame para escala de cores cinza
                    color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    frames.append(color_frame)  # Adiciona o frame convertido à lista
                    # Exibe o frame capturado
                    cv2.imshow('Streaming', frame)
                    # Verifica se a tecla 'q' foi pressionada para interromper a gravação
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    # # Obtém o tempo atual
                    # tempo_atual = time.time()
                    # data_formatada = datetime.fromtimestamp(time.time()).strftime('%Y-%d-%m_%H.%M.%S')
                    # print(data_formatada)
                    # cv2.imwrite(f'./carvao_{data_formatada}.mp4', frame)

                    # Verifica se a duração da gravação foi atingida
                    if len(frames) > duracao_gravacao * 24:
                        # Verifica se existem frames na lista
                        #if len(frames) > 0:
                        # Obter o timestamp atual e formatá-lo em uma representação de data e hora
                        data_formatada = datetime.fromtimestamp(time.time()).strftime('%Y-%d-%m_%H.%M.%S')
                        print(data_formatada)
                        clip = ImageSequenceClip(frames, fps=24)
                        clip.write_videofile(f'./carvao_{data_formatada}.mp4')
                        frames.clear()
                        continue

                else:
                    break

        # Libera os recursos
        cap.release()
        cv2.destroyAllWindows()
        time.sleep(1)
        attempts += 1

    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

gravar_video(camera, tentativas)

# f'D:\\Pelotas_videos\\pelotas_{data_formatada}.mp4'