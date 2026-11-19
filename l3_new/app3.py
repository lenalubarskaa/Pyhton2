import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Smart Photo Editor", page_icon="📷", layout="wide")

st.title("📷 Smart Photo Editor")
st.write("Завантажте фото та застосуйте до нього фільтри!")

st.sidebar.header("Налаштування фільтрів")

uploaded_file = st.sidebar.file_uploader("Оберіть зображення...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Оригінальне фото")
        st.image(img_array, width="stretch")

    filter_option = st.sidebar.selectbox("Оберіть фільтр", ["Оригінал", "Чорно-білий", 
                                                            "Розмиття", "Налаштування яскравості",
                                                            "Налаштування контрасту", "Інверсія",
                                                            "Віддзеркалення"])

    processed_img = img_array.copy()

    if filter_option == "Чорно-білий":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    elif filter_option == "Розмиття":
        processed_img = cv2.GaussianBlur(img_array, (15, 15), 0)

    elif filter_option == "Налаштування яскравості":
        brightness_val = st.sidebar.slider("Рівень яскравості", -100, 100, 0)
        processed_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=brightness_val)

    elif filter_option == "Налаштування контрасту":
        contrast_val = st.sidebar.slider("Рівень контрасту", 0.5, 3.0, 1.0, step=0.1)
        processed_img = cv2.convertScaleAbs(img_array, alpha=contrast_val, beta=0)

    elif filter_option == "Інверсія":
        processed_img = 255 - img_array

    elif filter_option == "Віддзеркалення":
        processed_img = cv2.flip(img_array, 1)

    with col2:
        st.subheader("Оброблена фотографія")
        st.image(processed_img, width="stretch")
