from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

#정확도를 올리기 위해 image를 resize할 필요성이 있는가?
image = cv2.imread('C:/Users/wch/Documents/GitHub/SmartOMR/omr.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #gray로 이미지 처리
blurred = cv2.GaussianBlur(gray, (5, 5), 0) #가우시안 필터(노이즈캔슬링)
edged = cv2.Canny(blurred, 75, 200) #경계선 찾기

#Contours는 검은배경에 흰 물체를 찾는것과 비슷하므로 무조건 이미지를 변경후 Contour를 찾는다.
#Contours(폐곡선)는 이미지를 변형하기 때문에 copy사용

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None

if len(cnts) > 0: #Contours가 1개 이상이면
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True) #Contour가 큰것부터 작은것 까지 
	for c in cnts:
		peri = cv2.arcLength(c, True) #Contours 둘레 길이
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)#다각형에서 직사각형으로 꼭짓점을 줄여나감(근사계산)
		if len(approx) == 4: #근사값이 4각형일때 for문 멈춤
			docCnt = approx
			break

paper = four_point_transform ( image, docCnt. reshape ( 4 , 2 ))
#cv2.imshow('model',paper)
#cv2.waitKey(0)
warped = four_point_transform ( gray, docCnt. reshape ( 4 , 2 ))
#cv2.imshow('model',warped)
#cv2.waitKey(0)

thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow('model',thresh)
cv2.waitKey(0)