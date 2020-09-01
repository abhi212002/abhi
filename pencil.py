import cv2
import numpy as np

pic = cv2.imread("C:/Users/hp/Pictures/Saved Pictures/0328c10756921df64521e0adbc34316d.png")

sp = 0.60

w = int(pic.shape[1]*sp)
h = int(pic.shape[0]*sp)

dim = (w,h)
resized = cv2.resize(pic,dim,interpolation = cv2.INTER_AREA)

sharp = np.array([[-1,-1,-1], 
                 [-1, 9,-1],
                 [-1,-1,-1]])
sharpened = cv2.filter2D(resized,-1,sharp)



gray = cv2.cvtColor(sharpened , cv2.COLOR_BGR2GRAY)
inv = 230-gray
gauss = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)

def dodgeV2(image,mask):
    return cv2.divide(image,255-mask,scale=256)

pencil_pic = dodgeV2(gray,gauss)



cv2.imshow('resized',resized)
cv2.imshow('sharp',sharpened)
cv2.imshow('gray',gray)
cv2.imshow('inv',inv)
cv2.imshow('gauss',gauss)
cv2.imshow('pencil sketch',pencil_pic)
cv2.imwrite('C:/Users/hp/Desktop/pencil/output.png', pencil_pic)
cv2.imwrite('C:/Users/hp/Desktop/pencil/out.png', gray)
