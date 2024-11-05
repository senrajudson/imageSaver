import cv2
import time
import os
from datetime import datetime

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

"rtsp://digifort:digi2010@10.247.229.204:554"
"rtsp://admin:digi2010@10.247.229.204:554"
"""

dir_name = "projeto_pelotas"
root_dir = os.path.abspath(os.sep)
print(root_dir)
camera = "rtsp://digifort:digi2010@10.247.220.79:554"
tentativas = 32256


def gravar_video(cam, tentativas):
    attempts = 1
    count = 0
    while attempts < tentativas:
        print(f"Connecting attempt {attempts}")
        cv2.setUseOptimized(True)
        # cv2.setNumThreads(4)  # Opcional: Configurar o número de threads
        cv2.ocl.setUseOpenCL(True)  # Ativar suporte a OpenCL
        cap = cv2.VideoCapture(cam)

        if not cap.isOpened():
            print("Camera not opened...")
            attempts += 1
            time.sleep(1)
            continue

        while cap.isOpened():
            # Lê o frame atual do streaming
            ret, frame = cap.read()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if not ret:
                print("Error: missing frame. Reconnecting...")
                cap.release()
                break

            # Obtém o tempo atual
            data_formatada = datetime.fromtimestamp(time.time()).strftime('%Y-%d-%m_%H.%M.%S')
            nome_dir = f"{dir_name}_{datetime.fromtimestamp(time.time()).strftime('%Y-%d-%m_%H')}"
            # print(data_formatada)

            if count == 500:
                print(f"count {count}")

                if os.path.exists(nome_dir):
                    if not os.path.exists(f'./{dir_name}/{nome_dir}/{data_formatada}.png'):
                        cv2.imwrite(f'./{dir_name}/{nome_dir}/{data_formatada}.png', frame)
                        print(data_formatada)
                
                else:
                    if not os.path.exists(f'./{dir_name}/{nome_dir}/{data_formatada}.png'):
                        os.makedirs(f'./{dir_name}/{nome_dir}', exist_ok=True)
                        cv2.imwrite(f'./{dir_name}/{nome_dir}/{data_formatada}.png', frame)
                        print(data_formatada)

                count = 0
                continue

            print(f"count {count}")
            count += 1
        # Libera os recursos
        print("Cannot open camera")
        cv2.destroyAllWindows()
        cap.release()


gravar_video(camera, tentativas)

# f'D:\\Pelotas_videos\\pelotas_{data_formatada}.mp4'