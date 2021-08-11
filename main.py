import cv2          #importing cv2
import winsound
cam=cv2.VideoCapture(0) #to capture video...have 0 unless u have multiple cameras
while cam.isOpened(): #when camera is open
    ret,frame1 = cam.read()# read the camera ret--retrieve and frame of the camera
    ret,frame2 = cam.read()# now make 2 frames  one static and one moving to compare..if this two is identical there is no movement if movement there
    #will be movemt in frames
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)#to make gray form
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)#to getting rid of unwanted things noises
    #dialtion is opposite of threshold ..now remaining thing are intresteing thing
    dialted=cv2.dilate(thresh,None,iterations=3)
    controus,_=cv2.findContours(dialted,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#boundary of the things detacted static and moving
    # cv2.drawContours(frame1,controus,-1,(0,255,0),2)
    for c in controus:
        if cv2.contourArea(c)<5000: # to removing smaller contours
            continue
        x,y,w,h=cv2.boundingRect(c) #to form the width  in X and height in Y
        winsound.PlaySound('so.wav', winsound.SND_LOOP)

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)





    if cv2.waitKey(10)==ord(' '): #if u want to turn off the window and assign some button
        break
    cv2.imshow('Rahul',frame1)#show the camera  in the computer and given camera some name and pass the frame



