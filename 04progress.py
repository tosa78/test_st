import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'iteration {i+1} ')
  bar.progress(i+1)
  time.sleep(0.01)

'どね!！'
