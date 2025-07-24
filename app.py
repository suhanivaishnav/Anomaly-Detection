import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from keras.layers import TFSMLayer

st.title("🔍 Anomaly Detection System")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Preprocess image
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 224, 224, 3)

    # Load model

    model = TFSMLayer("C:/Users/pc/Downloads/converted_savedmodel/model.savedmodel/", call_endpoint="serving_default")
    prediction_dict = model(img_array)
    confidence = list(prediction_dict.values())[0].numpy()[0]

    # Show prediction scores
    st.write(f"Confidence → Normal: {confidence[0]:.2f}, Anomaly: {confidence[1]:.2f}")

    # Manual threshold logic
    anomaly_score = confidence[1]  # index 1 = anomaly class

    if anomaly_score > 0.5:
        st.error("❌ Anomaly Detected!")
    else:
        st.success("✅ Normal Product")


