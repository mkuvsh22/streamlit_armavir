import streamlit as st
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")

def send_prompt(prompt):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    if response.status_code == 200:
        response_json = response.json()
        text = response_json['result']['alternatives'][0]['message']['text']
        return text
    elif response.status_code == 429:
        time.sleep(1)
        
        response = requests.post(url, headers=headers, json=prompt)
        if response.status_code == 200:
            response_json = response.json()
            text = response_json['result']['alternatives'][0]['message']['text']
            return text
        elif response.status_code == 429:
            time.sleep(4)
            response = requests.post(url, headers=headers, json=prompt)
            if response.status_code == 200:
                response_json = response.json()
                text = response_json['result']['alternatives'][0]['message']['text']
                return text
            else:
                return f"Error: {response.status_code}, {response.text}"
        else:
            return f"Error: {response.status_code}, {response.text}"
    else:
        return f"Error: {response.status_code}, {response.text}"

def send_blueprint(prompt: str):
    prompt = {
        "modelUri": "bt14n3vjsod6g6jksd97",
        "completionOptions": {
            "stream": False,
            "temperature": 0.1,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "user",
                "text": f"{prompt}"
            }
        ]
    }
    
    result = send_prompt(prompt)
    
    # delay
    time.sleep(0.05)
    
    return result

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
        response = send_blueprint(f"Напиши рецензию на фильм не менее пяти предложений в котором есть: {user_input}")
        if response.startswith("Error:"):
            st.write(response)
        else:
            st.markdown(
                f'<font face="Fira Mono"><br><br>{response}</font>',
                unsafe_allow_html=True
            )
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

# Таймер для перезагрузки страницы
st.markdown(
    """
    <script>
    let timer;
    function resetTimer() {
        clearTimeout(timer);
        timer = setTimeout(() => {
            window.location.href = 'https://mkuvsh22.github.io/eternalfilmcritic2/';
        }, 30000); // 30 секунд
    }
    window.onload = resetTimer;
    window.onmousemove = resetTimer;
    window.onmousedown = resetTimer; // включите любые события, которые хотите отслеживать
    window.ontouchstart = resetTimer;
    window.onclick = resetTimer;
    window.onkeypress = resetTimer;
    </script>
    """,
    unsafe_allow_html=True
)

st.markdown('<a href="https://mkuvsh22.github.io/eternalfilmcritic2/" target="_blank" style="color: #008080;">Вернуться на интро</a>', unsafe_allow_html=True)




