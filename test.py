import pytesseract
import cv2
from PIL import Image
import easyocr
import numpy as np
reader = easyocr.Reader(['en'])


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'


# reading an image
image_path = "images/axio.jpg"
img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.resize(img_gray, (img_gray.shape[1]*4, img_gray.shape[0]*4))
img_new = cv2.resize(img, (img.shape[1]*4, img.shape[0]*4))

img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
cv2.imshow("Image", img_blur)
cv2.waitKey(0)
img_med = cv2.medianBlur(img_gray, 5)

cv2.waitKey(0)
img_thres = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
img_thres_med = cv2.threshold(img_med, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
bitwise = cv2.bitwise_and(img_gray, img_thres, mask=None)
cv2.imshow("bitwise", bitwise)
contours, hierarchy = cv2.findContours(bitwise, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(max_contour)
cropped_img = img_new[y:y+h, x:x+w]
cv2.imshow("cropped", cropped_img)
print(reader.readtext(cropped_img))
cv2.waitKey(0)