import cv2
import math

while 1:
	x = int(input("図示したいポイントの x 座標を指定してください。"))
	y = int(input("図示したいポイントの y 座標を指定してください。"))
	length = int(input("矢印の長さを指定してください。"))

	theta = math.radians(-45)

	src = cv2.imread("source.png")
	color = (0, 0, 255)
	pt2 = (x, y)
	x += length * math.cos(theta)
	y += length * math.sin(theta)
	pt1 = (x, y)

	dst = cv2.arrowedLine(src, pt1, pt2, color)

	cv2.imshow(str(pt2) + str(length))
	key = input("これでよろしいですか？（よろしい：Y | よろしくない：N）>")
	if(key == "y"):
		break

cv2.imwrite("output.png", dst)
