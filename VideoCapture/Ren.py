import os

os.getcwd()
collection = "/home/abdelrahman/res"
cnt = 1
for i, filename in enumerate(os.listdir(collection)):
    ss = str(cnt)
    sz = len(ss)
    kk = "00"
    for j in range(4 - sz):
        kk = kk + '0'
    os.rename("/home/abdelrahman/res/" + filename, "/home/abdelrahman/res/" + kk + str(cnt) + ".png")
    cnt=cnt+1



