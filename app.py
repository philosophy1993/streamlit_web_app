import streamlit as st
from PIL import Image

ousin_btn = st.button('更新')
st.title('哲学アプリ')
st.caption('これは哲学のテストアプリです。')
st.subheader('自己紹介')
st.text('私はてつがくです。\n'
            'google mapのapiを使いこなしたいと考えています。。')
code = '''
import streamlit as stfdaf


st.title('哲学アプリ')
'''

st.code(code, language='python')

#画像
image = Image.open('picture.jpg')
st.image(image, width=200)

with st.form(key = 'profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')
    
    age_category = st.selectbox(
            '年齢層',
            ('子供(18歳未満)','大人(18歳以上)'))
    
    #複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','映画鑑賞','ゲーム'))
    
    #ボタン
    submit_btn = st.form_submit_button('送信')
    kousin_btn = st.form_submit_button('更新')
        
    if submit_btn == True:
        st.text(f'ようこそ{name}さん\n'
                    f'住んでるところは{address}ですね。\n'
                    f'年齢層は{age_category}ですね。\n'
                    f'趣味は{",".join(hobby)}ですね'
                    )
                    
