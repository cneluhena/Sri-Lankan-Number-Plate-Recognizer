from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import cv2
import easyocr
model = YOLO("Model/best.pt")
image_name = 'pleasure.jpg'
img = cv2.imread(f'images/{image_name}')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.resize(img_gray, (img.shape[1]*3, img.shape[0]*3)) 

img = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3)) 
img_gray = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)[1]
img_gray = cv2.dilate(img_gray, None, iterations=1)
results = model.predict(img)
results = results[0]
reader = easyocr.Reader(['en'])
print(img.size)
boxes = results.boxes
for box in boxes: 
    b = box.xyxy[0].tolist()
    cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0, 255, 0), 2)
    roi = img_gray[int(b[1]):int(b[3]), int(b[0]):int(b[2])]
    print(reader.readtext(roi))
    cv2.imshow('roi', roi)
    cv2.waitKey(0)


cv2.imshow('image', img)
cv2.waitKey(0)
