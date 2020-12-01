import cv2
import numpy as np

video = cv2.VideoCapture('Friends.mp4')


if (video.isOpened() == False):
    print('Erro ao abrir o arquivo de vídeo!')

while(video.isOpened()):
    ret, frame = video.read()

    if ret == True:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(33) == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
