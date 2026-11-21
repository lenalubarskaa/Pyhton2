import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "openrouter/free"


def generate_recipe(products, category):

    if not OPENROUTER_API_KEY:
        raise Exception("Не знайдено API-ключ!")

    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}",
               "Content-Type": "application/json"}

    prompt = f"""
    Ти розумний помічник із приготування їжі.

    Користувач має такі продукти: {products}
    Категорія страви: {category}

    Створи реалістичний та смачний рецепт.

    ВАЖЛИВО ПРО ПРОДУКТИ:
    - Намагайся використати всі продукти користувача.
    - Не ігноруй продукти без пояснення.
    - Якщо якийсь продукт не підходить до страви, поясни чому.
    - Не додавай багато продуктів, яких немає у списку.
    - Дозволено додавати базові спеції та олію.

    Напиши короткий рецепт у такому форматі:

    **Назва страви:** назва рецепта

    **Інгредієнти:**
    - список продуктів із кількістю

    **Спосіб приготування:**
    1. Перший крок.
    2. Другий крок.
    3. Третій крок.

    **Час приготування:** приблизний час у хвилинах.

    ВАЖЛИВО:
    - Не нумеруй назву страви та інгредієнти.
    - Нумеруй лише 3 кроки приготування.
    - Не додавай зайвих пунктів.

    ВАЖЛИВО ПРО МОВУ:
    - Відповідай виключно українською мовою.
    - Не використовуй інші мови.
    - Пиши грамотно, без помилок.
    - Пиши коротко та зрозуміло.
    - Назва страви повинна відповідати інгредієнтам і способу приготування.
- Перевіряй правильність української мови та не повторюй слова помилково.
    """

    data = {"model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4000}

    response = requests.post(API_URL,
                            headers=headers,
                            json=data,
                            timeout=60)                   

    response.raise_for_status()

    result = response.json()

    print("Повна відповідь:", result)

    recipe = result["choices"][0]["message"].get("content")
    finish_reason = result["choices"][0].get("finish_reason")

    if not recipe:
        raise Exception("Модель не повернула текст. Причина: " + str(finish_reason))

    return recipe, finish_reason


if __name__ == "__main__":

    try:
        print("Перевірка створення рецепта...")

        test_recipe = generate_recipe("яйця, молоко, борошно","Сніданок")

        print("\nРезультат:")
        print(test_recipe)

    except Exception as error:
        print("Помилка:", error)
