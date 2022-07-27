import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc

ousin_btn = st.button('更新')
st.title('哲学アプリ')
st.caption('これは哲学のテストアプリです。')
st.subheader('自己紹介')
st.text('私はてつがくです。\n'
            'google mapのapiを使いこなしたいと考えています。。')

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

    #url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    res = requests.get(url, params= params)
    places = json.loads(res.text)

    url = "https://maps.googleapis.com/maps/api/place/details/json"
    for place in places['results']:
        
        stc.html("""
                <h2><var>{0}<var></h2>
                <iframe src="https://www.google.com/maps/embed/v1/place?q={0}&key=AIzaSyB8f6M1nmXeBlEpc13xvqs_pDb6Y_aVJ1c" 
                width="600" height="450" allowfullscreen="allowfullscreen"></iframe>
        """.format(place['name']),height =450)
        params = {
        "key":"AIzaSyB8f6M1nmXeBlEpc13xvqs_pDb6Y_aVJ1c",
            "place_id":place['place_id'],
            "region" : "jp",
            "language" : "ja",
            }
        res = requests.get(url, params= params)
        place_details = json.loads(res.text)
        #pprint.pprint(place_details['reviews'])
        for place_detail in place_details['result']:
            pprint.pprint(place_detail)
            print("-------------------------------------\n")
        #     pprint.pprint(place_detail)
        
    #st.text(place)
    #pprint.pprint(place[])
    # st.text(f'あなたが望んだのは{place[0]}ですね？')
    
    #places['results',[i]['name']]

stc.html("""
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        * {
        box-sizing: border-box;
        }

        body {
        margin: 0;
        font-family: Arial;
        }

        /* The grid: Four equal columns that floats next to each other */
        .column {
        float: left;
        width: 25%;
        padding: 10px;
        }

        /* Style the images inside the grid */
        .column img {
        opacity: 0.8; 
        cursor: pointer; 
        }

        .column img:hover {
        opacity: 1;
        }

        /* Clear floats after the columns */
        .row:after {
        content: "";
        display: table;
        clear: both;
        }

        /* The expanding image container */
        .container {
        position: relative;
        display: none;
        }

        /* Expanding image text */
        #imgtext {
        position: absolute;
        bottom: 15px;
        left: 15px;
        color: white;
        font-size: 20px;
        }

        /* Closable button inside the expanded image */
        .closebtn {
        position: absolute;
        top: 10px;
        right: 15px;
        color: white;
        font-size: 35px;
        cursor: pointer;
        }
        </style>
        </head>
        <body>

        <div style="text-align:center">
        <h2>Tabbed Image Gallery</h2>
        <p>Click on the images below:</p>
        </div>

        <!-- The four columns -->
        <div class="row">
        <div class="column">
            <img src="https://www.w3schools.com/howto/img_nature.jpg" alt="Nature" style="width:100%" onclick="myFunction(this);">
        </div>
        <div class="column">
            <img src="https://www.w3schools.com/howto/img_snow.jpg" alt="Snow" style="width:100%" onclick="myFunction(this);">
        </div>
        <div class="column">
            <img src="https://www.w3schools.com/howto/img_mountains.jpg" alt="Mountains" style="width:100%" onclick="myFunction(this);">
        </div>
        <div class="column">
            <img src="https://www.w3schools.com/howto/img_lights.jpg" alt="Lights" style="width:100%" onclick="myFunction(this);">
        </div>
        </div>

        <div class="container">
        <span onclick="this.parentElement.style.display='none'" class="closebtn">&times;</span>
        <img id="expandedImg" style="width:100%">
        <div id="imgtext"></div>
        </div>

        <script>
        function myFunction(imgs) {
        var expandImg = document.getElementById("expandedImg");
        var imgText = document.getElementById("imgtext");
        expandImg.src = imgs.src;
        imgText.innerHTML = imgs.alt;
        expandImg.parentElement.style.display = "block";
        }
        </script>

        </body>
        </html>

        """,height =1000)