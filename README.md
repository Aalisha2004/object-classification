# Object Detection App

## 📌 Project Overview
This project is an **Object Detection Web App** built using **Streamlit, OpenCV, PyTorch, and YOLO**. The app allows users to **upload** or **capture** an image, and it detects objects within the image, displaying the objects along with their confidence scores.

## 🚀 Features
- **Upload an image** or **capture using a webcam**.
- **Object detection** using **YOLO (You Only Look Once)** model.
- **Displays detected objects** with **bounding boxes**.
- **Confidence scores** for detected objects.
- **User-friendly UI** with responsive design.
- **Deployed successfully**, making it accessible online.

## 🛠️ Technologies Used
- **Python** (Core programming language)
- **Streamlit** (Frontend framework for web apps)
- **OpenCV** (Image processing)
- **PyTorch** (Deep learning framework)
- **YOLO (Ultralytics)** (Pre-trained object detection model)
- **NumPy** (Array handling)
- **Pillow (PIL)** (Image manipulation)

## 📂 Project Structure
```
├── app.py                # Main application script
├── requirements.txt      # Required dependencies
├── README.md             # Project documentation
└── yolov5s.pt            # Pre-trained YOLO model (loaded dynamically)
```

## 📸 How It Works
1. **Upload an image** or **capture a picture** from the webcam.
2. The app processes the image using the **YOLOv5 model**.
3. Objects in the image are **detected and labeled**.
4. The detected objects and their **confidence scores** are displayed.
5. Users can **view** the processed image with **bounding boxes**.

## 🔧 Installation & Setup
To run the project locally, follow these steps:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repository/object-detection-app.git
cd object-detection-app
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

## 🌐 Deployment
This app has been **successfully deployed** online. Users can access it without needing to install anything locally.

👉 [https://object-classification-4zyvxubtc6zpifs5wjjqqn.streamlit.app/]


## ✨ Acknowledgments
- **Ultralytics YOLO** for pre-trained models.
- **Streamlit** for easy web app development.
- **OpenCV** for image processing capabilities.

---

🎯 **Enjoy using the Object Detection App!** 🚀

