import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc
from embed import show_store
from OpenAI_ChatBot import app2

def app1():
    opennow = 0
    ousin_btn = st.button('更新')

    st.title('評判の良い店舗検索')
    st.text('以下を入力して、送信ボタンをクリックしてください。\n'
                '検索結果は、評価値の高い順に表示されます。')
    st.text('検索したいジャンル等を入力してください')
    api_key = st.secrets["hide_api_key"] 
    next_page = False
    with st.form(key = 'profile_form'):
        free_word = st.text_input('フリーワード')
        #複数選択
        category = st.multiselect(
            'ジャンル',
            ('焼肉','イタリアン','フレンチ','居酒屋','日本料理',))
        maxprice = st.selectbox(
            '金額',
            ('指定無し','安い','少し安い','少し高い','高い',))
        maxprice = maxprice.replace('指定無し','').replace('安い','1').replace('少し安い','2').replace('少し高い', '3').replace('高い','4')
        evaluation = st.slider(label ='最低評価値:',min_value = 0.0,max_value =  5.0, step = 0.1)
        
        #ボタン
        submit_btn = st.form_submit_button('送信')
        kousin_btn = st.form_submit_button('更新')
        next_btn = st.form_submit_button('次のページ')
        

        if submit_btn == True:
            if next_btn == True:
                next_page = True
            show_store(free_word, category, maxprice, opennow, api_key,next_page,evaluation)
            next_page = False
                        


st.set_page_config(page_title="哲学のWebアプリ")
# サイドバーにナビゲーションを作成する
app_list = ['評判の良い店舗検索', 'ChatBot-OpenAI GPT-3.5']
app = st.sidebar.selectbox('Select an app', app_list)

# 選択されたアプリを表示する
if app == '評判の良い店舗検索':
    app1()
elif app == 'ChatBot-OpenAI GPT-3.5':
    app2()

