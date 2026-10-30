import streamlit as st

st.title("Мій конвертер величин")
st.write("Привіт! За допомогою цього сайту можна переводити різні величини.")


conversion = st.sidebar.radio(
    "Оберіть тип конвертації:",
    ["Довжина (Метри в Кілометри)", "Температура (Цельсій у Фаренгейт)"]
)


if conversion == "Довжина (Метри в Кілометри)":

    st.subheader("Метри в кілометри")

    number = st.number_input("Введіть кількість метрів:")

    if st.button("Конвертувати"):
        result = number / 1000
        st.metric("Результат", f"{result} км")


else:

    st.subheader("Цельсій у Фаренгейт")

    number = st.number_input("Введіть температуру в градусах Цельсія:")

    if st.button("Конвертувати"):
        result = number * 1.8 + 32
        st.metric("Результат", f"{result} °F")