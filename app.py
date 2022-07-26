import streamlit as st
from PIL import Image
import requests
import json
import pprint

ousin_btn = st.button('更新')
st.title('哲学アプリ')
st.caption('これは哲学のテストアプリです。')
st.subheader('自己紹介')
st.text('私はてつがくです。\n'
            'google mapのapiを使いこなしたいと考えています。。')
# code = '''
# import streamlit as stfdaf


# st.title('哲学アプリ')
# '''

# st.code(code, language='python')

#画像
image = Image.open('picture.jpg')
st.image(image, width=200)
st.text('検索したいジャンル等を入力してください')
with st.form(key = 'profile_form'):
    station = st.text_input('駅名')
    #address = st.text_input('住所')
    
    # age_category = st.selectbox(
    #         '',
    #         ('子供(18歳未満)','大人(18歳以上)'))
    
    #複数選択
    category = st.multiselect(
        'ジャンル',
        ('焼肉','イタリアン','フレンチ','六町','居酒屋'))
    
    #ボタン
    submit_btn = st.form_submit_button('送信')
    kousin_btn = st.form_submit_button('更新')
        
    if submit_btn == True:
        st.text(f'{station}駅で\n'
                    f'ジャンルは{",".join(category)}ですね'
                    )

    
    params = {
         "query":  {",".join(category)},
        #"query": 'うなぎ',
        "key":"AIzaSyB8f6M1nmXeBlEpc13xvqs_pDb6Y_aVJ1c",
        "region" : "jp",
        "language" : "ja",
        }
    print(params)
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    res = requests.get(url, params= params)
    places = json.loads(res.text)
    print("-------------------------------------\n")
    #pprint.pprint(places)
    for place in places['results']:
        st.text(place['name'])
        print(place['name'])
    #st.text(place)
    #pprint.pprint(place[])
    # st.text(f'あなたが望んだのは{place[0]}ですね？')
    
    #places['results',[i]['name']]