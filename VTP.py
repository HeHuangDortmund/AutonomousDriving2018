import cv2
import numpy
import os

cap = cv2.VideoCapture("F:\\Videos\\VideoForProject.avi")

#fps = cap.get(cv2.CAP_PROP_FPS)
#print("总帧数：%d" % fps)
#size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        #int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#flag = True
currentFrame = 0

print("请输入采样周期帧：")
intervalFrame = int(input())
pathstr = "F:\\Videos\\PicForProject" + str(intervalFrame)
os.makedirs(pathstr)

while True:  
    retval, image = cap.read()
    if retval == False:  
        break

    if currentFrame % intervalFrame == 0:  
        cv2.imwrite(pathstr + "\\sop" + str(currentFrame) + ".jpg", image)
    print("正在处理第" + str(currentFrame) + "帧\n")
    # if currentFrame == fps:
        #flag = False
    currentFrame = currentFrame + 1
cap.release()
