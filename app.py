import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc

def show_store(free_word, category, maxprice, opennow, api_key, next_page):
    st.text(f'{free_word}駅で\n'
                    f'ジャンルは{",".join(category)}ですね'
                    )

    category.extend(free_word.split())
    params = {
        "query":  {",".join(category)},
        "key":api_key,
        "maxprice": maxprice,
        # "opennow": opennow,
        "region" : "jp",
        "language" : "ja",
        # "pagetoken" : next_page,
        }
    pprint.pprint(params)
    print("-------------")

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    res = requests.get(url, params= params)
    places = json.loads(res.text)
    if places['status'] == 'ZERO_RESULTS':
        print(places['status'])
        stc.html("""
                <h2>{0}</h2>
        """.format(places['status']),height =450)
        
    print(places)
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    for place in places['results'] :
        
        stc.html("""
                <h2><var>{0}<var></h2>
                <iframe src="https://www.google.com/maps/embed/v1/place?q={0}&key=AIzaSyB8f6M1nmXeBlEpc13xvqs_pDb6Y_aVJ1c" 
                width="600" height="450" allowfullscreen="allowfullscreen"></iframe>
        """.format(place['name']),height =450)
        # params = {
        # "key": api_key,
        #     "place_id":place['place_id'],
        #     "region" : "jp",
        #     "language" : "ja",
        #     }
        # res = requests.get(url, params= params)
        # place_details = json.loads(res.text)
        # #pprint.pprint(place_details['reviews'])
        # reviews = place_details['result']['reviews']
        # for review in reviews:
        #     pprint.pprint(review)
        #     st.text(review['text'])
            

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
        '金額(4だと高い)',
        ('0','1','2','3','4',))
    opennow = st.selectbox(
        '現在開店してるかどうか(使用不可)',
        ('開店','閉店',))
    
    opennow = opennow.replace('開店', 'True').replace('閉店','False')

    #ボタン
    submit_btn = st.form_submit_button('送信')
    kousin_btn = st.form_submit_button('更新')
    next_btn = st.form_submit_button('次のページ')
    

    if submit_btn == True:
        if next_btn == True:
            next_page = True
        show_store(free_word, category, maxprice, opennow, api_key,next_page)
        next_page = False
        st.text(f'{free_word}駅で\n'
                    f'ジャンルは{",".join(category)}ですね'
                    )

    # category.extend(free_word.split())
    # params = {
    #     "query":  {",".join(category)},
    #     "key":api_key,
    #     "maxprice": maxprice,
    #     #"opennow": {",".join(opennow)},
    #     "region" : "jp",
    #     "language" : "ja",
    #     # "pagetoken" : pagetoken,
    #     }
    # pprint.pprint(params)
    # print("-------------")

    # url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    # res = requests.get(url, params= params)
    # places = json.loads(res.text)
    # if places['status'] == 'ZERO_RESULTS':
    #     print(places['status'])
    #     stc.html("""
    #             <h2>{0}</h2>
    #     """.format(places['status']),height =450)
        
    # #print(places)
    # url = "https://maps.googleapis.com/maps/api/place/details/json"
    # for place in places['results'] :
        
    #     stc.html("""
    #             <h2><var>{0}<var></h2>
    #             <iframe src="https://www.google.com/maps/embed/v1/place?q={0}&key=AIzaSyB8f6M1nmXeBlEpc13xvqs_pDb6Y_aVJ1c" 
    #             width="600" height="450" allowfullscreen="allowfullscreen"></iframe>
    #     """.format(place['name']),height =450)
    #     params = {
    #     "key": api_key,
    #         "place_id":place['place_id'],
    #         "region" : "jp",
    #         "language" : "ja",
    #         }
    #     res = requests.get(url, params= params)
    #     place_details = json.loads(res.text)
    #     #pprint.pprint(place_details['reviews'])
    #     reviews = place_details['result']['reviews']
    #     for review in reviews:
    #         pprint.pprint(review)
    #         st.text(review['text'])
