from turtle import clone
import cv2 as cv2
import numpy as np
path = ("E:/python/Water_watch_Recognition/unchanged.png")
m = cv2.imread(path)
gray = cv2.cvtColor(m,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5),0) #高斯模糊
edged = cv2.Canny(blurred, 200,250) #邊緣萃取
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
clone = m.copy()
if clone is None:
    print("null")
n = cv2.drawContours(clone,contours,-1, (0,255,0),2)
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(m,(x,y),(x+w,y+h),(153,153,0),5)
newimage = m[y+2:y+h-2, x+2:x+w-2]
if newimage is None:
    print("null")
reimg = cv2.resize(clone, (467,601))
hsv =cv2.cvtColor(reimg, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,43,46])
upper_red = np.array([10,255,255])
mask = cv2.inRange(hsv, lower_red, upper_red)
output = cv2.bitwise_and(hsv,hsv,mask = mask)
coordinate = mask[375,233]
a = np.array(coordinate)
print(coordinate)
b = np.array(output)
print(b)
#cv2.imshow(reimg)
if ((a==b).all()):
    print("It is moistened")
else:
    print("it is not moistened")
cv2.waitKey(0)
cv2.destroyAllWindows()
