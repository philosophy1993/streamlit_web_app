import streamlit as st
import requests
import pprint
import streamlit.components.v1 as stc
import json
import openai

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
            


def show_store(free_word, category, maxprice, opennow, api_key, next_page,evaluation):
    st.text(f'{free_word}駅で\n'
                    f'ジャンルは{",".join(category)}ですね'
                    )

    category.extend(free_word.split())
    params = {
        "query":  {",".join(category)},
        "key":api_key["key"],
        "maxprice": maxprice,
        # "opennow": opennow,
        "region" : "jp",
        "language" : "ja",
        # "pagetoken" : next_page,
        }

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    res = requests.get(url, params= params)
    places = json.loads(res.text)

    if places['status'] == 'ZERO_RESULTS':
        stc.html(f"""
                <h2>{places['status']}</h2>
        """,height =450)
    no_store =  True
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    
    for place in places['results'] :
    
        params = {
            "key": api_key["key"],
            "place_id":place['place_id'],
            "region" : "jp",
            "language" : "ja",
            }
        res = requests.get(url, params= params)
        place_details = json.loads(res.text)
        #pprint.pprint(place_details['reviews'])
        reviews = place_details['result']['reviews']
        
        if place_details['result']['rating'] >= evaluation:
            stc.html("""
                    <h2><var>{0}<var></h2>
                    <iframe src="https://www.google.com/maps/embed/v1/place?q={0}&key=AIzaSyB8f6M1nmXeBlEpc13xvqs_pDb6Y_aVJ1c" 
                    width="300" height="300" allowfullscreen="allowfullscreen"></iframe>
            """.format(place['name']),height =500, width = 500)
            st.text(f"このお店の評価は：{place_details['result']['rating']}")
            st.text('このお店の口コミ')
            for review in reviews:
                st.markdown(review['text'])
            no_store = False
            
    if no_store:
        st.text('指定した条件に合うお店はありませんでした。')

