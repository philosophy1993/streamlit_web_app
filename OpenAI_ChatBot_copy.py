import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc
import openai

messages = []  # メッセージを格納するリストを定義する
max_messages = 10  # 最大メッセージ数を定義する

def app2():
    opennow = 0

    st.title('ChatBot-OpenAI GPT-3.5')
    st.text('OpenAI GPT-3.5を使ったチャットボットです。')

    st.text('前提条件とAIへの入力フォームに入力してください。')
    api_key = st.secrets["OpenAI_api_key"] 

    generate_text(api_key)

def generate_text(api_key):
    openai.api_key = api_key["key"]

    # 過去の会話を表示する
    st.write("過去の会話:")
    for message in messages:
        st.write(f"{message['role'].capitalize()}: {message['content']}")

    with st.form(key = 'profile_form'):
        AI_input = st.text_area('前提のインプット', value="")
        user_input = st.text_area('AIへのインプット', value="")
        submit_btn = st.form_submit_button('送信')
        
        if submit_btn == True:
            send_message(api_key, AI_input, user_input)

def send_message(api_key, AI_input, user_input):
    openai.api_key = api_key["key"]

    # メッセージを追加する
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{AI_input}"},
        ] + messages,
    )

    ai_response = response['choices'][0]['message']['content']

    # 応答を表示する
    st.write(f'AI: {ai_response}')

    # メッセージを追加する
    messages.append({"role": "assistant", "content": ai_response})

    # messagesリストの中身がmax_messagesを超えた場合、最初のuserとassistantの会話を削除する
    if len(messages) > max_messages * 2:
        messages.pop(0)
        messages.pop(0)

app2()
