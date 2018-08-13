import numpy as np
import cv2

cap = cv2.VideoCapture(r'/home/abdelrahman/avidbeam/Sample-Videos/AL_Seq2.mp4')
cnt=0
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    ss = str(cnt)
    sz = len(ss)
    kk = "00"
    for j in range(4 - sz):
        kk = kk + '0'
    cv2.imwrite("sftp://192.168.0.185/media/avidbeam/Workspace/Abdelrahman-Ws/AdaptSegNet/data/Cityscapes/data/leftImg8bit/val/frankfurt/"+ kk + str(cnt)+".png",frame)
    cnt=cnt+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


