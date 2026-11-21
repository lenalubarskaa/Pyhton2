import streamlit as st
from ai_functions import generate_recipe


st.set_page_config(page_title="WhatToEat",
                   page_icon="🍳",
                   layout="centered")


st.title("🍳WhatToEat")

st.write("Не знаєш, що приготувати? "
         "Введи продукти, які є вдома, "
         "і штучний інтелект підбере для тебе рецепт!")

st.divider()

st.subheader("🥕 Які продукти є у тебе вдома?")

products = st.text_input("Введи продукти через кому:",
                         placeholder="Наприклад: яйця, молоко, борошно")

st.info("💡 Введи продукти, які вже є у тебе вдома.")


st.subheader("🍽️ Що хочеш приготувати?")

category = st.selectbox("Обери категорію страви:",
                        ["Сніданок", "Обід", "Вечеря", "Десерт"])

st.divider()


if st.button("🔍 Знайти рецепт", use_container_width=True):

    if products.strip() == "":
        st.warning("Ти ще не вказав продукти! "
                   "Введи хоча б два продукта.")

    else:
        try:
            with st.spinner("🍳 ШІ підбирає рецепт..."):

                recipe, finish_reason = generate_recipe(products, category)

                st.success("🎉 Рецепт готовий! Смачного!")

                st.subheader("Твій рецепт:")
                st.markdown(recipe)
            

        except Exception as error:
            st.error("Помилка: " + str(error))
            print("Помилка:", error)

st.divider()

