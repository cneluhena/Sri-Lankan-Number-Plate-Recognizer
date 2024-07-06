from ultralytics import YOLO
import cv2
import easyocr

class PlateReader:

    #initializing the plate segmenting model
    def __init__(self):
        self.model = YOLO("Model/platesegmentsdetection.pt")
        self.reader = easyocr.Reader(['en'])


    # reading the image
    def read_image(self, image_name):
        img = cv2.imread(f'images/Plate Only/{image_name}')
        return img


    # processing image before passing it to the model
    def extract_segment_coordinates(self, img):
        img = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3)) 
        results = self.model.predict(img)
        boxes = results[0].boxes
        boxes_copy = []
        index = -1
        min_area = float('inf')
        smallest_index = -1

        # finding smallest box(province box)
        for box in boxes:
            index += 1
            b = box.xyxy[0].tolist()
            area = (b[2] - b[0]) * (b[3] - b[1])
            if area < min_area:
                min_area = area
                smallest_index = index

        boxes_copy = list(boxes)
        del boxes_copy[smallest_index]
        return boxes_copy

    #preprocessing image before reading text
    def process_image(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #converting image to gray scale
        img_gray = cv2.resize(img_gray, (img.shape[1]*3, img.shape[0]*3))  #resize image

        img = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3))
        binary_img = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)[1]
        binary_img = cv2.dilate(img_gray, None, iterations=1)
        return binary_img

    #reading text from the image
    def read_text(self, boxes, img):
        for box in boxes: 
            try:
                b = box.xyxy[0].tolist()
                roi = img[int(b[1]):int(b[3]), int(b[0]):int(b[2])]
                print(self.reader.readtext(roi)[0][1])
            except:
                continue
    
    def run(self, image_name):
        img = self.read_image(image_name)
        boxes = self.extract_segment_coordinates(img)
        img = self.process_image(img)
        self.read_text(boxes, img)
