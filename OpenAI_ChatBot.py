import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc
from embed import generate_text


def app2():
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

            

                        
