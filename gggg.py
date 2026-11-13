
import streamlit as B

B.set_page_config(page_title="Каламбур", page_icon="🐬", layout="wide")

B.title("Ласкаво просимо до мого додатку!")

tab1, tab2 = B.tabs(["About me", "My instrument"])

with tab1:
    B.header("Знайомство з автором")

    C1, C2 = B.columns([1, 2])

    with C1:
        B.image("https://itstepedu.sharepoint.com/:i:/s/221415.15-18.05/IQCubomfgP3AQZynmXsJt-eGAaJGBSE_6cOuRfDHEydSGeU?e=JmoDPN")

    with C2:
        B.subheader("Привіт, я майбутній розробник ігор!")
        B.write("Я навчаюсь в МКА IT Step і проходив курси Roblox Studio і Kodu.")

        with B.container():
            B.info("Контакти для зв'язку")
            B.markdown("- GitHub: [Мій профіль](https://github.com)")
            B.markdown("- E-mail: rosrobnykrosrobnykiv@itstep.org")

with tab2:
    B.info("У процесі розробки")
