import streamlit as st
import easyocr
import json
from PIL import Image
import cv2
import numpy as np
import re

# Initialize the OCR reader for Hindi and English
reader = easyocr.Reader(['en', 'hi'])

# Function to preprocess the image to improve OCR accuracy
def preprocess_image(image):
    img = Image.open(image)
    img = img.convert('L')  # Convert to grayscale
    img_np = np.array(img)  # Convert to numpy array for OpenCV processing

    # Apply thresholding to increase contrast
    _, thresh_img = cv2.threshold(img_np, 127, 255, cv2.THRESH_BINARY)
    
    # Convert back to PIL image
    processed_img = Image.fromarray(thresh_img)
    return processed_img

# Function to extract text from the image using OCR
def extract_text(image):
    # Preprocess the image
    preprocessed_img = preprocess_image(image)
    
    # Save temporarily to process with EasyOCR
    preprocessed_img.save("temp_image.jpg")  
    
    # Extract text using EasyOCR
    result = reader.readtext("temp_image.jpg", detail=0)
    
    extracted_text = " ".join(result)
    return json.dumps({"extracted_text": extracted_text}, ensure_ascii=False)

# Function to highlight matches in the text
def highlight_matches(text, keyword):
    # Use re.sub to wrap the keyword with a <span> tag for highlighting
    highlighted_text = re.sub(f"({keyword})", r'<span style="background-color: yellow">\1</span>', text, flags=re.IGNORECASE)
    return highlighted_text

# Streamlit web application
def main():
    st.title("OCR and Keyword Search Web App")
    st.write("This app extracts text from an uploaded image (supports both Hindi and English) and allows you to search for keywords in the extracted text with highlighting.")
    
    # Upload an image file
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
        st.write("Extracting text...")
        
        # Extract text from the uploaded image
        extracted_text_json = extract_text(uploaded_image)
        extracted_text = json.loads(extracted_text_json)["extracted_text"]
        st.write("Extracted Text: ", extracted_text)
        
        # Keyword search functionality
        search_query = st.text_input("Enter a keyword to search:")

        if search_query:
            # Highlight matches if the keyword is found
            highlighted_text = highlight_matches(extracted_text, search_query)

            # Display the highlighted text using st.markdown for HTML rendering
            st.markdown(highlighted_text, unsafe_allow_html=True)

            if search_query.lower() in extracted_text.lower():
                st.success(f"'{search_query}' found in the extracted text!")
            else:
                st.error(f"'{search_query}' not found in the extracted text.")

if __name__ == "__main__":
    main()
