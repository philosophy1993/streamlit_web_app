import streamlit as st
from PIL import Image
import requests
import json
import pprint
import streamlit.components.v1 as stc
from Store_search import  app1
from OpenAI_ChatBot import app2
from Cocktail_Generator import app3

st.set_page_config(page_title="Cocktail_Generator", page_icon="🍸")
app3()

