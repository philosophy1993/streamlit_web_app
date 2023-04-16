import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc
import openai


def app21():
    opennow = 0

    st.title('ChatBot-OpenAI GPT-3.5')
    st.text('OpenAI GPT-3.5を使ったチャットボットです。')

    st.text('前提条件とAIへの入力フォームに入力してください。')
    api_key = st.secrets["OpenAI_api_key"] 


    #OpenAI GPT-3.5を使ったチャットボット
    #OpenAIへのリクエスト
    with st.form(key = 'profile_form'):
        #AIへの前提をインプット
        AI_input = st.text_area('前提のインプット', value="")

        #AIへの入力
        user_input = st.text_area('AIへのインプット', value="")


        #ボタン
        submit_btn = st.form_submit_button('送信')
        
        #OpenAIへのリクエスト
        if submit_btn == True:
            generate_text(AI_input, user_input, api_key)


#OpenAIのAPIにアクセスし、回答をStreamlitに出力する。
def generate_text(AI_input, user_input, api_key):
    openai.api_key = api_key["key"]
    messages = [] # 新しくリストを定義する
    max_messages = 10 # 最大メッセージ数を定義する
    #print("AIの性格を決めて下さい")
    #I_input = AI_input
    #AI_input = "以下の動物の豆知識について、冗談を交えながら、二人の成人女性が会話しているように解説してください。解説は400文字程度で、以下の特性以外にも知っていることがあったら補足してください。また、二人の成人女性の会話以外の解説はいりません。"
    # ユーザーからの入力を取得する
    #user_input = input("User: ")
    #user_input  = user_input

    # APIにユーザーからの入力を送信し、AIからの応答を取得する
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": f"{AI_input}"},
        {"role": "user", "content": f"{user_input}"}
        ]
    )
    # AIからの応答を取得する
    ai_response = response['choices'][0]['message']['content']
    # 応答を表示する
    st.write(f'AI: {ai_response}')
            

    # メッセージを追加する
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "assistant", "content": ai_response})

    # messagesリストの中身がmax_messagesを超えた場合、最初のuserとassistantの会話を削除する
    if len(messages) > max_messages * 2:
        messages.pop(0)
        messages.pop(0)

    # !が入力された場合、messagesリストの中身を表示する
    if user_input == "!":

        print("messages:", messages)
    #endと打ったらメッセージの中身が全て排出されます。会話は10ターンのみを保持するようにして超えた場合は、最初の会話が削除されます。


                        
