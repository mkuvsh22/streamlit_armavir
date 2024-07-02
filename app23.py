import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

IAM_TOKEN = os.getenv("IAM_TOKEN")

# Функция для отправки запроса к модели YandexGPT
def get_response(user_input):
    req = {
        "modelUri": "ds://bt14n3vjsod6g6jksd97",
        "completionOptions": {
            "stream": False,
            "temperature": 0.1,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "user",
                "text": f"Напиши рецензию на фильм не менее пяти предложений в котором есть: {user_input}"
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}",
        "x-folder-id": "b1gik8r0od91a5kkg895",
    }
    response = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                             headers=headers, json=req)
    return response.json()

# Интерфейс Streamlit
st.markdown(
    '<font face="Fira Mono" size="5"><b>Электрический кинокритик</b></font>', 
    unsafe_allow_html=True
)

st.markdown(
    '<font face="Fira Mono" size="3" color="gray">Напишите три слова (<i>Например: Кристен Стюарт, слон, Россия</i>):</font>', 
    unsafe_allow_html=True
)

user_input = st.text_input("Введите описание фильма:")

button_style = (
    "background-color: #008080;"
    "color: black;"
    "border-radius: 4px;"
    "padding: 10px 20px;"
    "font-size: 16px;"
    "border: none;"
    "cursor: pointer;"
)

if st.button('Рецензия', key='review_button', help='Нажмите, чтобы получить рецензию'):
    if user_input:
        response = get_response(user_input)
        if 'result' in response and 'alternatives' in response['result'] and len(response['result']['alternatives']) > 0:
            instruction = response["result"]["alternatives"][0]["message"]["text"]
            st.markdown(
                f'<font face="Fira Mono"><br><br>{instruction}</font>',
                unsafe_allow_html=True
            )
        else:
            st.write("Ошибка: Некорректный ответ от API.")
    else:
        st.write("Пожалуйста, введите описание фильма.")

# Изменение цвета кнопки
st.markdown(
    """
    <style>
    .css-14ex4b2-buttonBase {
        background-color: #008080 !important;
    }
    .element-container {
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<a href="https://mkuvsh22.github.io/eternalfilmcritic2/" target="_blank" style="color: #008080;">Вернуться на интро</a>', unsafe_allow_html=True)

st.markdown("""
    <script>
    var timeout;
    var redirectUrl = "https://mkuvsh22.github.io/eternalfilmcritic2/";

    function resetTimer() {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            window.location.href = redirectUrl;
        }, 30000);  // 30 секунд
    }

    document.body.addEventListener("mousemove", resetTimer);
    document.body.addEventListener("keydown", resetTimer);

    resetTimer();  // Инициализация таймера при загрузке страницы
    </script>
    """, unsafe_allow_html=True)


