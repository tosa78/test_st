import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')


# チェックボックス------------------------------------
if st.checkbox('Show Image'):
  img = Image.open('./media/top.jpg')
  st.image(img, caption='TOP', use_column_width=True)


# セレクトボックス------------------------------------
option = st.selectbox(
  '好きな数字を教えてください',
  list(range(1,11))
)

'あなたの好きな数字は', option , 'です'


# テキスト入力------------------------------------
text = st.text_input('趣味を教えてください')
'あなたの趣味：', text


# スライダー------------------------------------
condition = st.slider('いまの調子は？', 0, 100, 50)
'調子：', condition