import cv2
img = cv2.imread("pythong/task.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
blurred = cv2.GaussianBlur(hsv, (11,11), 0)
edges = cv2.Canny(blurred, 50, 115)
contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
min_area = 0
max_area = 20
for contour in contours:
    area = cv2.contourArea(contour)
    if min_area <= area <= max_area:
        cv2.drawContours(img, [contour],-1, (0,0, 255), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()