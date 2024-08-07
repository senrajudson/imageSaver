
import os
import cv2 as cv
from datetime import datetime
import time
import threading

"esse código não é do igor"

"fui eu quem fiz"

def salvar_image_can_ip_rtsp_por_frame(ip, divisivelFrame, ip_save_name):
    while True:
        print(
            "A função (classificar_can_ip_rtsp_usando_cv_com_video) vai salvar todos os arquivos que estiverem com a classificação maior ")
        cap = cv.VideoCapture(ip)
        currentfram = 0
        inicio = time.time()
        if not cap.isOpened():
            print("Cannot opem video")
            print("Tentando reconnectar em 30 s")
            time.sleep(30)
            continue
        while True:
            ret, frame = cap.read()
            if ret == False:
                print("Can't receive frame (stream end?). Exiting ...")
                print("Connecting...")
                cap.release()
                cv.destroyAllWindows()
                time.sleep(30)
                cap = cv.VideoCapture(ip)
            else:
                #frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                cv.imshow('frame', frame)
                current_time = datetime.now()
                diretorio = f'./{ip_save_name}/{current_time.year}_{current_time.month}_{current_time.day}/{current_time.year}_{current_time.month}_{current_time.day}_{current_time.hour}'
                # print(current_time)
                currentfram += 1
                if os.path.exists(diretorio) == True:
                    print(f'Frame: {currentfram} é divisível por {divisivelFrame}: {currentfram%divisivelFrame == 0}')
                    if (currentfram % divisivelFrame == 0):
                        fim = time.time()
                        print(f'Salvando imagem {currentfram}')
                        print(f'Tempo do período entre salvamento: {fim - inicio} segundos')
                        cv.imwrite(
                            f'{diretorio}/frame_{current_time.year}_{current_time.month}_{current_time.day}_{current_time.hour}_{current_time.minute}_{current_time.second}_' + str(
                                currentfram) + '.jpg', frame)
                        inicio = time.time()
                else:
                    os.makedirs(diretorio)
                    cv.imwrite(
                        f'{diretorio}/frame_{current_time.year}_{current_time.month}_{current_time.day}_{current_time.hour}_{current_time.minute}_{current_time.second}_' + str(
                            currentfram) + '.jpg', frame)
                    currentfram = 0
                #cv.imshow('frame', frame)

            if cv.waitKey(1) == ord('q'):
                break
        # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()

ips_nomes = [#"10_247_93_69_554", #interna
#"rtsp://digifort:digi2010@10.247.92.30:554", #interna
#"rtsp://digifort:digi2010@10.247.92.31:554", #interno
#"rtsp://digifort:digi2010@10.247.92.145:554", #interno
#"rtsp://digifort:digi2010@10.247.92.149:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.166:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.146:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.150:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.165:554", #nao funcionou
"emissoes_fugitivas_10_247_220_138_554" #funciona - essa eu irei usar
#"10_247_146_30_554", #teste
#"rtsp://admin:adminlb2@10.247.146.30:554"
# 'rtsp://admin:adminlb2@10.247.146.30:554/cam/realmonitor?channel=1&subtype=0'
]


ips = [#"rtsp://digifort:digi2010@10.247.93.69:554", #interna
#"rtsp://digifort:digi2010@10.247.92.30:554", #interna
#"rtsp://digifort:digi2010@10.247.92.31:554", #interno
#"rtsp://digifort:digi2010@10.247.92.145:554", #interno
#"rtsp://digifort:digi2010@10.247.92.149:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.166:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.146:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.150:554", #nao funcionou
#"rtsp://digifort:digi2010@10.247.92.165:554", #nao funcionou
"rtsp://digifort:digi2010@10.247.220.138:554" #funciona - essa eu irei usar
#"rtsp://admin:adminlb2@10.247.146.30:554", #teste
#"rtsp://admin:adminlb2@10.247.146.30:554"
]

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;tcp'
threads = []
for index, ip in enumerate(ips):
    t = threading.Thread(target=salvar_image_can_ip_rtsp_por_frame, args=(ip,4000,ips_nomes[index]))
    t.start()
    threads.append(t)



