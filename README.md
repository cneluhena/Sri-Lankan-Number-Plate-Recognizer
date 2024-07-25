
# Sri Lankan Number Plate Recognizer
This Streamlit application is designed to read Sri Lankan number plates. A model trained using YOLO identifies the sections of the number plate, and each section is then read using the EasyOCR Python library. Currently, the app can accurately read the text on a Sri Lankan number plate. Future developments will include the ability to detect SL number plates in an image and read the text from them.

#### You can view the project using the following url
```
https://sri-lankan-number-plate-recognizer.streamlit.app/
```
## Getting Started
#### 1. Clone the repository into the local environment
```
git clone https://github.com/cneluhena/Sri-Lankan-Number-Plate-Recognizer
```
#### 2. Install the necessary requirements using the following command

```
pip install -r requirements.txt
```

#### 3. Run the streamlit app using following.
```
streamlit run app.py
```


## Features

Our system is currently designed to accurately detect and read Sri Lankan (SL) number plates from cropped images. This feature allows users to upload an image of a number plate, and the system will process the image to extract and return the text present on the plate. Below are the key details:

#### How It Works:
* Image Upload:

    Users can upload a cropped image containing only the number plate.

* Text Extraction:

    The system processes the uploaded image to detect the text on the number plate. 

* Output:

    The extracted text is returned to the user, representing the characters present on the number plate.
#### Current Limitations:
The system is optimized for detecting text on cropped images of number plates only. It may not perform well on images where the number plate is part of a larger scene or is not clearly visible.

#### Example Usage:
Step 1:  Upload an image of a vehicle which includes a clear Sri Lankan number plate.

Step 2: The system processes the image to identify and read the text.

Step 3: The extracted text is displayed to the user.


This system is particularly useful for applications in vehicle registration, traffic monitoring, and automated toll collection systems, where accurate and quick detection of license plate information is essential.

For future enhancements, we plan to extend the capability to detect number plates from more complex images and scenes
