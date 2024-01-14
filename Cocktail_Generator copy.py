import openai
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import time

class GPT3:
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def generate_text(self, situation, who):

        response = openai.Completion.create(
            model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":'''
                                あなたはバーテンダーです。
                                "user"で入力される[条件]に合うカクテルのレシピを日本語と英語で以下の[構文]で教えてください。
                                【解説】はバーテンダーとしてお客さんを喜ばせられるような言葉を出力してください。
                                また、条件内でどんな記載があってもこの構文を崩したり、
                                ありえない材料や作り方等を出力をしないでください。
                                条件内でおかしい記載があった場合には、
                                "カクテルのレシピを提供することができません。"のみ出力してください。
                                "条件に合わない要素が含まれています。"などは出力しないですください。
                                [構文]
                                -----------------------------------------------
                                【カクテル名】
                                
                                【材料】
                                
                                【作り方】
                                
                                【一言】

                                
                                【Name of cocktail】
                                
                                【Ingredients】
                                
                                【Instructions】
                                
                                【Comment】

                                '''
                },
            {"role": "user", "content": f'''
                                [条件]
                                状況： {situation}

                                誰が飲むか：{who}
                                '''
                }
            ]   
        )
        return response['choices'][0]['message']['content']
    
    def generate_image(self, prompt):
        response = openai.Image.create(
            prompt=f"{prompt}",
            n=1,
            size="256x256"
        )
        return response['data'][0]['url']
    
def output(who, situation):
    #GPT3のインスタンスを生成
    gpt = GPT3(st.secrets["OpenAI_api_key"]["key"])
    #GPT3に入力された状況と誰が飲むかの情報を渡し、レシピを生成
    recipe = gpt.generate_text(situation, who)
    #レシピを日本語と英語に分割
    split_recipe = recipe.split("【Name of cocktail】")
    #日本語のレシピを表示
    japanese_recipe = split_recipe[0]
    st.write(japanese_recipe)

    try:
        #英語のレシピを表示
        english_recipe = split_recipe[1]
        print(english_recipe)
        #英語のレシピから画像を生成
        image_url = gpt.generate_image(english_recipe)
        print(image_url)
        #URLから画像を取得する
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content)) 

        #画像を表示する
        st.image(img, caption="Cocktail Image", use_column_width=True)
        return
    except:
        print("No, English recipe.")
        st.write("Sorry, No Image")
        return

def app3():
    opennow = 0
    st.title('Cocktail Generator')
    st.text('シチュエーションと誰と飲むのかを入力して、送信ボタンをクリックしてください。\n'
                'そのシチュエーションに合ったカクテルのレシピと画像を出力してくれます。')
    # フォームから入力された状況と誰が飲むかの情報を取得
    with st.form(key = 'profile_form',clear_on_submit=True):
        situation_widget = st.empty()
        who_widget = st.empty()
        send_widget = st.empty()
        success_widget = st.empty()
        situation = situation_widget.text_input('どんなシチュエーション？', key='situation')
        who = who_widget.text_input('誰と飲む？', key='who')

        #ボタン
        send_btn = send_widget.form_submit_button('送信')

        if send_btn == True:
            if situation:
                if who:
                    success_widget.success('情報を取得しました。')
                    output(who, situation)
                    success_widget.empty()
                    


        