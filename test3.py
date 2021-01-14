from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
#
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

#정확도를 올리기 위해 image를 resize할 필요성이 있는가?
image = cv2.imread('C:/Users/wch/Documents/GitHub/SmartOMR/omr.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #gray로 이미지 처리
blurred = cv2.GaussianBlur(gray, (5, 5), 0) #가우시안 필터(노이즈캔슬링)
edged = cv2.Canny(blurred, 75, 200) #경계선 찾기

#Contours는 검은배경에 흰 물체를 찾는것과 비슷하므로 무조건 이미지를 변경후 Contour를 찾는다.
#Contours(폐곡선,윤곽선)는 이미지를 변형하기 때문에 copy사용

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None

if len(cnts) > 0: #Contours가 1개 이상이면
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True) #Contour가 큰것부터 작은것 까지 
    #Contour중에 가장 큰 4각형인 것을 찾기위해 for문 사용
	for c in cnts:
		peri = cv2.arcLength(c, True) #Contours 둘레 길이
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)#다각형에서 직사각형으로 꼭짓점을 줄여나감(근사계산)
		if len(approx) == 4: #근사값이 4각형일때 for문 멈춤
			docCnt = approx
			break

#와핑 변환수행. four point transform 은 헤비 리프팅을 처리하는 함수
paper = four_point_transform ( image, docCnt.reshape ( 4 , 2 ))
#두 번째 인자 = 문서를 나타내는 윤곽선이라함
#cv2.imshow('model',paper)
#cv2.waitKey(0)
warped = four_point_transform ( gray, docCnt.reshape ( 4 , 2 ))
#cv2.imshow('model',warped)
#cv2.waitKey(0)

#threshold를 통해 배경과 물체 분리(이미지전역을 이진화 함)
thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow('model',thresh)
cv2.waitKey(0)
#왜 그냥 threshold사용? 광원없다는 가정인가?
#왜 adaptive_threshold나 Otsu's Binarization사용안함?

cnts = cv2. findContours ( thresh.copy () , cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE )
cnts = imutils. grab_contours ( cnts )
questionCnts = []

for c in cnts:
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)
	if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
		questionCnts.append(c)

questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
correct = 0

for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
	cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
	bubbled = None

for (j, c) in enumerate(cnts):
	mask = np.zeros(thresh.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
	mask = cv2.bitwise_and(thresh, thresh, mask=mask)
	total = cv2.countNonZero(mask)
	if bubbled is None or total > bubbled[0]:
		bubbled = (total, j)

	color = (0, 0, 255)
	k = ANSWER_KEY[q]
	if k == bubbled[1]:
		color = (0, 255, 0)
		correct += 1
	cv2.drawContours(paper, [cnts[k]], -1, color, 3)

score = (correct / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper, "{:.2f}%".format(score), (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", paper)
cv2.waitKey(0)





