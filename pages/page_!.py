import streamlit as st

code = '''
import streamlit as st


st.title('哲学アプリ')
'''

st.code(code, language='python')


st.text(f'住所：{address}')