#note.nkmk.me のサンプルコード
#参考：https://note.nkmk.me/python-opencv-draw-function/

import numpy as np
import cv2

img = np.full((210, 425, 3), 128, dtype=np.uint8)

cv2.line(img, (50, 10), (125, 60), (255, 0, 0))
cv2.line(img, (50, 60), (125, 10), (0, 255, 255), thickness=4, lineType=cv2.LINE_AA)

cv2.arrowedLine(img, (50, 80), (125, 130), (0, 255, 0), thickness=4)
cv2.arrowedLine(img, (50, 130), (125, 80), (255, 0, 255), tipLength=0.3)

cv2.rectangle(img, (50, 150), (125, 200), (255, 255, 0))

cv2.circle(img, (190, 35), 15, (255, 255, 255), thickness=-1)
cv2.circle(img, (240, 35), 20, (0, 0, 0), thickness=3, lineType=cv2.LINE_AA)

cv2.ellipse(img, ((190, 105), (20, 50), 0), (255, 255, 255))
cv2.ellipse(img, ((240, 105), (20, 50), 30), (0, 0, 0), thickness=-1)

cv2.ellipse(img, (190, 175), (10, 25), 0, 0, 270, (255, 255, 255))
cv2.ellipse(img, (240, 175), (10, 25), 30, 0, 270, (0, 0, 0), thickness=-1)

cv2.drawMarker(img, (300, 20), (255, 0, 0))
cv2.drawMarker(img, (337, 20), (0, 255, 0), markerType=cv2.MARKER_TILTED_CROSS, markerSize=15)
cv2.drawMarker(img, (375, 20), (0, 0, 255), markerType=cv2.MARKER_STAR, markerSize=10)

cv2.drawMarker(img, (300, 50), (0, 255, 255), markerType=cv2.MARKER_DIAMOND)
cv2.drawMarker(img, (337, 50), (255, 0, 255), markerType=cv2.MARKER_SQUARE, markerSize=15)
cv2.drawMarker(img, (375, 50), (255, 255, 0), markerType=cv2.MARKER_TRIANGLE_UP, markerSize=10)

pts = np.array(((300, 80), (300, 130), (335, 130)))
cv2.polylines(img, [pts], True, (255, 255, 255), thickness=2)

pts = np.array(((335, 80), (375, 80), (375, 130)))
cv2.fillPoly(img, [pts], (0, 0, 0))

cv2.putText(img, 'nkmk', (300, 170), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2)
cv2.putText(img, 'nkmk', (300, 195), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), lineType=cv2.LINE_AA)

cv2.imshow('Result', img)
cv2.waitKey(0)
