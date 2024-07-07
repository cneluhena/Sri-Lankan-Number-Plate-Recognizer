import streamlit as st
from PlateReader import PlateReader
from PIL import Image
st.title('Sri Lankan License Plate Recognizer') 


st.markdown('<p style="font-size:18px;"><b>Choose an image of a number plate...</b></p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type="jpg")
plate_reader = PlateReader()

temp_image = "temp.jpg"
if uploaded_file is not None:
    with open(temp_image, "wb") as f:
        f.write(uploaded_file.getbuffer())
    image = Image.open(uploaded_file)
    
    st.image(image, caption='Uploaded Image.', use_column_width=True)


if st.button('Process'):
    if uploaded_file is not None:
        license_plate_text = ''
        with st.spinner('Processing...'):
            plate_text = plate_reader.run(temp_image)  #plate_text is an array
            for data in plate_text:
                license_plate_text += data + ' '
        st.write(f'<p style="font-size:32px;">License Plate is: <b>{license_plate_text}</b></p>', unsafe_allow_html=True)
    else:
        st.write('Please upload an image')
