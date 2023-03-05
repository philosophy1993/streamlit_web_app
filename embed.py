import streamlit as st
import requests
import pprint
import streamlit.components.v1 as stc
import json
import openai

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

