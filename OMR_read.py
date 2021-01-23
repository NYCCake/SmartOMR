from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import matplotlib.pyplot as plt
import imutils
import cv2

ANSWER = {0:4, 1:3, 2:2, 3:1, 4:4, 5:5 }

omr= cv2.imread('C:/Users/wch/Documents/GitHub/SmartOMR/omr3.png')
gray = cv2.cvtColor(omr, cv2.COLOR_BGR2GRAY) #gray로 이미지 처리
blurred = cv2.GaussianBlur(gray, (1, 1), 0) #가우시안 필터(노이즈캔슬링)을 약하게만 적용
edged = cv2.Canny(blurred, 10, 100)
#cv2.imshow('model',edged)
#cv2.waitKey(0)

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

cv2.drawContours(omr,[cnts[0]],0,(0,0,255),2)
cv2.imshow("omr",omr)
cv2.waitKey(0)

if len(cnts) > 0: 
	for c in cnts:
		peri = cv2.arcLength(c, True) #Contours 둘레 길이
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)#다각형에서 직사각형으로 꼭짓점을 줄여나감(근사계산)
		if len(approx) == 4: #근사값이 4각형일때 for문 멈춤
			docCnt = approx 
			break



x, y, w, h = cv2.boundingRect(cnts[0])
print(x, y, w, h)

roi = gray[y:y+h, x:x+w]
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.show()