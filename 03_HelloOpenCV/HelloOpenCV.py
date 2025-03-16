import cv2

print(cv2.getVersionString())


image = cv2.imread("static/1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("image", gray)
cv2.waitKey()