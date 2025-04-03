# Smart Handwriting Recognition App

## 📌 Description

The **Smart Handwriting Recognition App** is a web-based application that enables users to upload images of handwritten text and extract the text using **Optical Character Recognition (OCR)** technology. Powered by the **Tesseract OCR engine**, this tool seamlessly converts images into editable text, enhancing productivity and streamlining workflows.

## 🚀 Features

- 📂 **Upload Support**: Accepts images in **JPG, PNG, and JPEG** formats.
- 🔍 **OCR Extraction**: Extracts text from uploaded handwritten images.
- 🎨 **User-Friendly UI**: Built with **Bootstrap** for a clean and responsive interface.
- 🌐 **Gradio Interface**: Alternative web-based interface for easier interaction.

---

## 🛠️ Installation

Follow these steps to set up and run the application:

### 1️⃣ Clone the Repository:

```bash
git clone <my-repository-url>
```

### 2️⃣ Navigate to the Project Directory:

```bash
cd Smart-Handwriting-Recognition-App
```

### 3️⃣ Set Up a Virtual Environment (Recommended):

```bash
python -m venv venv
```

#### Activate Virtual Environment:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies:

```bash
pip install -r requirements.txt
```

### 5️⃣ Ensure **Tesseract OCR** is Installed:

Make sure Tesseract OCR is installed on your system and the correct path is set in `model.py`.

---

## ▶️ Running the Application

### Flask Web App:

```bash
python app.py
```

Access the application in your browser at: **`http://127.0.0.1:5000/`**

### Gradio Interface:

To run the Gradio-based UI, execute:

```bash
python gradio_app.py
```

This will launch a browser-based interactive interface for uploading and extracting text from images.

---

## 🔮 Future Works

- ✅ Improve OCR accuracy using deep learning models.
- ✅ Enhance UI/UX for a more intuitive user experience.
- ✅ Extend support for more languages and handwriting styles.
- ✅ Further optimize **Gradio Interface** for better performance and usability.




