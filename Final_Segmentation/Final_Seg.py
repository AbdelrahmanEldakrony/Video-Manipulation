
import numpy as np
import cv2
from PIL import Image
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
import  os
import argparse

Ground_Truth=os.listdir(r'/home/abdelrahman/teest')

Ground_Truth.sort()

Colored=os.listdir(r'/home/abdelrahman/PycharmProjects/VideoCapture/Data-AlSeq2')


Colored.sort()


cnt=0

for i in range(600):

    #print(Ground_Truth[i])
    image_path = os.path.join(r'/home/abdelrahman/teest', Ground_Truth[i])
    gt=cv2.imread(image_path)
    gt = cv2.resize(gt, (600, 600))
    gt=np.asanyarray(gt)


    image_path = os.path.join(r'/home/abdelrahman/PycharmProjects/VideoCapture/Data-AlSeq2',Colored[i])
    cld = cv2.imread(image_path)
    cld = cv2.resize(cld, (600, 600))
    #cv2.imshow("oyr", cld)
    cld = np.asanyarray(cld)
    Seg = np.zeros([600, 600, 3], dtype="uint8")

    for i in range(600):
        for j in range(600):
            # print(Colored[i][j][0],Colored[i][j][1],Colored[i][j][2])
            if (cld[i][j][0] == 60 and cld[i][j][1] == 20 and cld[i][j][2] == 220):

                # print("Here")
                Seg[i][j][0] = 30 + (gt[i][j][0] * 0.5)
                Seg[i][j][1] = 10 + (gt[i][j][1] * 0.5)
                Seg[i][j][2] = 110 + (gt[i][j][2] * 0.5)
            else:
                Seg[i][j][0] = gt[i][j][0]
                Seg[i][j][1] = gt[i][j][1]
                Seg[i][j][2] = gt[i][j][2]
                # print(Ground_Truth[i][j][0]-Seg[i][j][0])

    ss = str(cnt)
    sz = len(ss)
    kk = "00"
    for j in range(4 - sz):
        kk = kk + '0'
    cv2.imwrite("/home/abdelrahman/tkvi/" + kk + str(cnt) + ".png", Seg)
    cnt = cnt + 1





'''
Ground_Truth = cv2.imread(r'/home/abdelrahman/000465.png')

Colored = cv2.imread(r'/home/abdelrahman/000465_color.png')


Ground_Truth=cv2.resize(Ground_Truth,(500,500))

Ground_Truth=np.asanyarray(Ground_Truth)

Colored=cv2.resize(Colored,(500,500))

Colored=np.asanyarray(Colored)

#print(Colored.shape)
#cv2.imshow("Out",Colored)
#cv2.waitKey(0)

Seg=np.zeros([500,500,3], dtype = "uint8")

for i in range(500):
    for j in range(500):
        #print(Colored[i][j][0],Colored[i][j][1],Colored[i][j][2])
        if(Colored[i][j][0]==60 and Colored[i][j][1]==20 and Colored[i][j][2]==220):

           # print("Here")
            Seg[i][j][0]=30+(Ground_Truth[i][j][0]*0.5)
            Seg[i][j][1]=10 + (Ground_Truth[i][j][1] * 0.5)
            Seg[i][j][2]=110 + (Ground_Truth[i][j][2] * 0.5)
        else:
            Seg[i][j][0] = Ground_Truth[i][j][0]
            Seg[i][j][1] = Ground_Truth[i][j][1]
            Seg[i][j][2] = Ground_Truth[i][j][2]
            #print(Ground_Truth[i][j][0]-Seg[i][j][0])




print(Seg.shape)
cv2.imshow("Out",Seg)
cv2.waitKey(0)
'''









