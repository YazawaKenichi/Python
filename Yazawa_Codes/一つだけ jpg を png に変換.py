import cv2

src = cv2.imread("1.jpg")

cv2.imshow("src", src)
cv2.waitKey(0)

cv2.imwrite("1.png", src)

dst = cv2.imread("1.png")

cv2.imshow("dst", dst)
cv2.waitKey(0)
