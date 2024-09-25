# OCR and Document Search Web Application Prototype 

This project is a web-based application designed to perform Optical Character Recognition (OCR) on uploaded images that contain text in both Hindi and English. The extracted text can then be searched using a keyword search feature, with matching sections highlighted. This application is built using Python, EasyOCR, Streamlit, and other supporting libraries.

## Features
- **Image Upload**: Users can upload images in various formats such as JPG, PNG, or JPEG.
- **OCR Functionality**: Text is extracted from the uploaded image using EasyOCR, which supports both Hindi and English text.
- **Keyword Search**: Users can input keywords to search within the extracted text, and the application highlights matching sections.
- **Preprocessing**: The image is preprocessed (converted to grayscale, thresholded) to improve OCR accuracy.
- **Live Deployment**: The application is deployed online for easy access via a live URL.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
   EasyOCR for OCR functionality.
   Streamlit for building the web interface.
   OpenCV for image preprocessing.
   PIL (Pillow) for image handling.
   NumPy for image manipulation.
- **Deployment**: Streamlit Sharing or any other online platform like Huggingface Spaces.

## Project Structure
- **app.py**: The main file containing the code for the Streamlit app and the OCR processing.
- **requirements.txt**: A list of all required Python libraries to run the application.
- **temp_image.jpg**: Temporary image file generated during OCR processing.
- **README.md**: Documentation explaining the project setup, usage, and deployment.

## Installation

Follow these steps to get a local copy up and running:

1.**Clone the Repository**:
   ```sh
       git clone <https://github.com/vaishnavi-643/OCR_IITR_Project.git>
  ```

2.**Create and Activate Virtual Environment**:
   ```sh
     python -m venv venv
     source venv/bin/activate  # For MacOS/Linux
     venv\Scripts\activate  # For Windows
  ```

3.**Install Dependencies**:
   ```sh
     pip install -r requirements.txt
   ```

4.**Run the Application**:
   ```sh
     streamlit run app.py
   ```
This will launch the application in your browser, where you can upload images and test the OCR functionality.

5.**Testing**: Upload an image containing both Hindi and English text to test the OCR and search functionality. Input a keyword to search within the extracted text, and the matching sections will be highlighted.

## Usage

Once the servers are running, you can access the application at `http://localhost:8501/`.

## Example
Here’s an example of how the application works:

- User uploads an image containing text in both Hindi and English.
- The OCR processes the image, extracts the text, and displays it on the page.
- User enters a keyword (e.g., “search”) in the search box.
- If the keyword is found, the matching section is highlighted.

## Contributing

 welcome contributions from the community! To contribute, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a pull request

Please make sure to update tests as appropriate and follow the code of conduct outlined in the repository.

## Deployment
The app is deployed at [Live URL](https://ocriitr-vaishnaviverma.streamlit.app/).

## License

This project is licensed under the MIT License. See the [LICENSE](`MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.`
) file for more information.

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Author**: VAISHNAVI VERMA

Happy coding! 🎉

---

Thank you for checking out the project. I hope you find it valuable and enjoyable to use. Contributions are always welcome, and we look forward to your feedback!


