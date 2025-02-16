import streamlit as st
import cv2
import numpy as np
import torch
from PIL import Image
from ultralytics import YOLO

def load_model():
    return YOLO("yolov5s.pt")

def detect_objects(image, model):
    results = model(image)
    detections = results[0].boxes.data.cpu().numpy()
    detected_objects = []
    
    for det in detections:
        x1, y1, x2, y2, conf, class_id = det
        label = model.names[int(class_id)]
        confidence = round(float(conf) * 100, 2)  # Convert to percentage
        detected_objects.append((label, confidence))
        
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        cv2.putText(image, f"{label} ({confidence}%)", (int(x1), int(y1) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return image, detected_objects

def main():
    st.set_page_config(page_title="Image Object Detection", page_icon="📷", layout="wide")
    
    
    st.markdown("<h1 class='title'>🖼️ Image Object Detection App</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>Upload or capture an image, and the app will detect objects with confidence scores.</h3>", unsafe_allow_html=True)
    
    model = load_model()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📤 Upload an Image")
        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], help="Upload an image from your device.")
    
    with col2:
        st.markdown("### 📸 Take a Picture")
        captured_image = st.camera_input("Capture an image using your webcam")
    
    if uploaded_file or captured_image:
        image = Image.open(uploaded_file or captured_image)
        image = np.array(image)
        
        #st.markdown("### 📷 Uploaded Image")
        #st.image(image, caption="Uploaded Image", use_column_width=True)
        
        st.markdown("### 🔍 Detecting objects...")
        processed_image, detected_objects = detect_objects(image, model)
        
        #st.markdown("### 🎯 Detected Objects")
        st.image(processed_image, caption="Detected Objects", use_column_width=True)
        
        if detected_objects:
            st.markdown("### 📋 Detection Results")
            st.table({"Object": [obj[0] for obj in detected_objects], "Confidence (%)": [obj[1] for obj in detected_objects]})
        else:
            st.markdown("### ❌ No objects detected.")

if __name__ == "__main__":
    main()
