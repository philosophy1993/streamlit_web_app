import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc
from embed import show_store

opennow = 0
ousin_btn = st.button('更新')
st.title('哲学アプリ')
st.caption('これは哲学のテストアプリです。')
st.subheader('自己紹介')
st.text('私はてつがくです。\n'
            'google mapのapiを使いこなしたいと考えています。。')
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
    # opennow = st.selectbox(
    #     '現在開店してるかどうか(使用不可)',
    #     ('開店','閉店',))
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
                    
