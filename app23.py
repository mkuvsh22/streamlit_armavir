import streamlit as st
import requests

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
                "text": f"Напиши рецензию на фильм не менее трех предложений в котором есть: {user_input}"
            }
        ]
    }
    headers = {
        "Authorization": "Bearer " + 't1.9euelZrIlZPNz4vHzIqXiYuRyMeQi-3rnpWajs-YlY-Zm4mNzZCemo2Zzczl9PdjVz1M-e94f0vL3fT3IwY7TPnveH9Ly83n9euelZqbksaNzs-Wl83GlI2KmIuJie_8xeuelZqbksaNzs-Wl83GlI2KmIuJiQ.sdExRB3nlwFHSOX56YFszxCxKCoetLwGp5zvvjiPoSP7DaEuWbI3y18GNaBfr5IfgTdWhi08FdJc-TFwZWXnAA',
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

user_input = st.text_input("")

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
        instruction = response["result"]["alternatives"][0]["message"]["text"]
        st.markdown(
            f'<font face="Fira Mono"><br><br>{instruction}</font>',
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
    </style>
    """,
    unsafe_allow_html=True
)