import streamlit as st

st.set_page_config(page_title="Мій сайт", page_icon="🐬", layout="wide")

st.title("Ласкаво просимо до мого сайту!")

tab1, tab2, tab3 = st.tabs(["Вкладка один", "Вкладка два", "Корисні посилання"])

with tab1:
    st.info("У процесі розробки")

with tab2:
    st.info("У процесі розробки")

with tab3:
    st.header("Корисні посилання")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Навчання")
        st.markdown("""
        🌐 [Google](https://www.google.com)
        💻 [W3Schools](https://www.w3schools.com)
        """)

    with col2:
        st.subheader("Ігрі та розваги")
        st.markdown("""
        🎮 [Scratch](https://scratch.mit.edu)
        🧩 [Minecraft](https://www.minecraft.net/en-us)
        """)

