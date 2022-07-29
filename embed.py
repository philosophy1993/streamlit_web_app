import streamlit as st
import requests
import pprint
import streamlit.components.v1 as stc
import json

def show_store(free_word, category, maxprice, opennow, api_key, next_page,evaluation):
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
        "key": api_key,
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
                    width="600" height="450" allowfullscreen="allowfullscreen"></iframe>
            """.format(place['name']),height =450)
            st.text(f"このお店の評価は：{place_details['result']['rating']}")
            st.text('このお店の口コミ')
            for review in reviews:
                st.text(review['text'])
            no_store = False
            
    if no_store:
        st.text('指定した条件に合うお店はありませんでした。')

