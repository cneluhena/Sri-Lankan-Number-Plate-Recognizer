import pytesseract
import cv2
from PIL import Image
import easyocr
import numpy as np
reader = easyocr.Reader(['en'])
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract"

# reading an image
image_path = "images/fitted.jpg"
img = cv2.imread(image_path)
img = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3))
kernel = np.ones((5, 5), np.uint8)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_thres = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)[1]
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(img_thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("img", img)
cv2.waitKey(0)
for contour in contours:
   
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
        letter = img_thres[y+5:y+h+5, x-5:x+w+5]
        letter = cv2.resize(letter,(letter.shape[0]*2, letter.shape[1]*2))
        
        cv2.imshow("img", letter)
        cv2.waitKey(0)
        print(reader.readtext(letter))
    
        
cv2.imshow("img", img_gray)
cv2.waitKey(0)