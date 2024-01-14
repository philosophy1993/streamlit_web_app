import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc
from Store_search import  app1
from OpenAI_ChatBot import app21
from Cocktail_Generator import app3
from OpenAI_ChatBot_copy import app2 

st.set_page_config(page_title="評判の良い店舗検索", page_icon="🍸")

# サイドバーにナビゲーションを作成する
app_list = ['評判の良い店舗検索', 'ChatBot-OpenAI GPT-3.5', 'Cocktail_Generator']
app = st.sidebar.selectbox('Select an app', app_list)

# 選択されたアプリを表示する
if app == '評判の良い店舗検索':
    app1()

