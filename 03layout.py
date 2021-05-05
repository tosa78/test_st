import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')


# サイドバー------------------------------------
# st.sidebar.write('サイドバー')

# text = st.sidebar.text_input('趣味を教えてください')
# 'あなたの趣味：', text


# condition = st.sidebar.slider('いまの調子は？', 0, 100, 50)
# '調子：', condition

# condition = st.slider('調子の再確認をさせて！', 0, 100, 50)
# st.sidebar.write('再確認の調子：', condition)


# 2カラムレイアウト------------------------------------
left_column, right_column = st.beta_columns(2)
btn = left_column.button('右カラムに文字を表示')
if btn:
  right_column.write('ここは右カラムです')


# エキスパンダー------------------------------------
expander = st.beta_expander('よくある質問：？？')
expander.write('回答B')
expander2 = st.beta_expander('よくある質問：？？？？')
expander2.write('回答B')