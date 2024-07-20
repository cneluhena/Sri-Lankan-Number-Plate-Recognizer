from ultralytics import YOLO
import cv2
import easyocr

class PlateReader:

    #initializing the plate segmenting model
    def __init__(self):
        self.plate_seg_model = YOLO("Model/platesegmentsdetection.pt")
        self.reader = easyocr.Reader(['en'])
        self.plate_det_model = YOLO('Model/slnumberplate.pt')


    # reading the image
    def read_image(self, image_name):
        img = cv2.imread(f'{image_name}')
        return img


    # processing image before passing it to the model
    def extract_segment_coordinates(self, img):
        img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2)) 
        results = self.plate_seg_model.predict(img)
        boxes = results[0].boxes
        boxes_copy = []
        index = -1
     
        boxes_with_areas = []

        #getting the area of each box
        for box in boxes:
            index += 1
            b = box.xyxy[0].tolist()
            area = (b[2] - b[0]) * (b[3] - b[1])
            boxes_with_areas.append([index, area])

        #sorting the boxes based on the area
        sorted_boxes = sorted(boxes_with_areas, key=lambda x: x[1], reverse=True)

        #getting the two most largest boxes
        largest_boxes = sorted_boxes[:2]
        largest_boxes.reverse()  #reversing the list to get the boxes in the order they appear in the image
        
        #choosing the two largest boxes original boxes array
        for box in largest_boxes:
            boxes_copy.append(boxes[box[0]])
        return boxes_copy


    #preprocessing image before reading text
    def process_image(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #converting image to gray scale
        img_gray = cv2.resize(img_gray, (img.shape[1]*2, img.shape[0]*2))  #resize image
        blur = cv2.GaussianBlur(img_gray, (5,5), 0)  #applying gaussian blur
        binary_img = cv2.threshold(blur, 110, 255, cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)[1]
        return binary_img


    #reading text from the image
    def read_text(self, boxes, img):
        text = []
        for box in boxes: 
            try:
                b = box.xyxy[0].tolist()
                roi = img[int(b[1]):int(b[3]), int(b[0]):int(b[2])]
                # self.anotate_image(b, img)  # only for testing purposes
                text.append(self.reader.readtext(roi)[0][1])
                
            except:
                continue
        # self.view_image(img)             #only for testing purposes
        return text
    
    #running the plate reader
    def run(self, image_name):
        # img = self.read_image(image_name)
        img = self.getting_roi(image_name)
        boxes = self.extract_segment_coordinates(img)
        img = self.process_image(img)
        output = self.read_text(boxes, img)
        return output

    #annotating the regions of the image
    def anotate_image(self, coordinates, img):
        cv2.rectangle(img, (int(coordinates[0]), int(coordinates[1])), (int(coordinates[2]), int(coordinates[3])), (0, 255, 0), 2)
    

    def getting_roi(self, img_name):
        img = self.read_image(img_name)
        prediction = self.plate_det_model.predict(img)
        box = prediction[0].boxes[0]
        b = box.xyxy[0].tolist()
        roi = img[int(b[1]):int(b[3]), int(b[0]):int(b[2])]
        return roi

    #viewing the image
    def view_image(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
