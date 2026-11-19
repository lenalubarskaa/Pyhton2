
import streamlit as st
import os
from PIL import Image
import requests
import urllib.parse
from io import BytesIO
import cv2
import numpy as np

st.set_page_config(page_title="AI Creative Studio", page_icon="🎨", layout="wide")

HF_API_URL = "https://router.huggingface.co/hf-interface/models/black-forest-labs/FLUX.1-schnell"
HF_TOKEN = os.getenv("HF_TOKEN")


def generate_image_hf(promt):
    try:
        encoded_prompt = urllib.parse.quote(promt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed=43"

        responce = requests.get(url, timeout=45)

        if responce.status_code == 200:
            return responce.content, None
        else:
            return None, f"Сервіс тимчасово недоступний ({responce.status_code})"

    except requests.exceptions.Timeout:
        return None, "Timeout"
    except Exception as e:
        return None, f"Помилка: {e}"


st.title("🎨 AI Creative Studio")
st.write("Опиши зображення, яке хочеш отримати")

promt = st.text_area("Опис зображення (промпт)")

if st.button("Згенерувати зображення") and promt:
    with st.spinner("AI створює зображення..."):
        image_bytes, error = generate_image_hf(promt)

    if error:
        st.error(error)

    elif image_bytes:
        st.session_state["image"] = image_bytes


if "image" in st.session_state:

    image = Image.open(BytesIO(st.session_state["image"]))
    img_array = np.array(image.convert("RGB"))

    st.sidebar.header("Налаштування фільтрів")

    filter_option = st.sidebar.selectbox(
        "Оберіть фільтр",
        ["Оригінал", "Чорно-білий", "Розмиття",
         "Налаштування яскравості", "Налаштування контрасту",
         "Інверсія", "Віддзеркалення"]
    )

    processed_img = img_array.copy()

    if filter_option == "Чорно-білий":
        processed_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    elif filter_option == "Розмиття":
        processed_img = cv2.GaussianBlur(img_array, (15, 15), 0)

    elif filter_option == "Налаштування яскравості":
        brightness_val = st.sidebar.slider("Рівень яскравості", -100, 100, 0)
        processed_img = cv2.convertScaleAbs(
            img_array, alpha=1.0, beta=brightness_val
        )

    elif filter_option == "Налаштування контрасту":
        contrast_val = st.sidebar.slider("Рівень контрасту", 0.5, 3.0, 1.0, step=0.1)
        processed_img = cv2.convertScaleAbs(
            img_array, alpha=contrast_val, beta=0
        )

    elif filter_option == "Інверсія":
        processed_img = 255 - img_array

    elif filter_option == "Віддзеркалення":
        processed_img = cv2.flip(img_array, 1)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Зображення від AI")
        st.image(img_array, width="stretch")

    with col2:
        st.subheader("Зображення з фільтром")
        st.image(processed_img, width="stretch")

    st.download_button(
        label="Скачати зображення",
        data=Image.fromarray(processed_img).convert("RGB").tobytes(),
        file_name="my_image.png",
        mime="image/png"
    )
