import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

# テキストと表の練習--------------------

df = pd.DataFrame({
  '1列目': [1, 2, 3, 4],
  '2列目': [10, 20, 30, 40],
})

st.dataframe(df, width=100, height=100)

# st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


# チャートの練習--------------------
## 1つ目
df_chart = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a', 'b', 'c']
)
st.line_chart(df_chart)
# st.area_chart(df)
# st.bar_chart(df)


# マップ--------------------
df_map = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon'] # latは緯度、lonは経度の英単語の略。
)
st.map(df_map)

df_map2 = pd.DataFrame({
  'lat': [35.667128],
  'lon': [139.738209],
})
st.dataframe(df_map2)
st.map(df_map2)


# 画像の読み込み--------------------
img = Image.open('./media/top.jpg')
st.image(img, caption='TOP', use_column_width=True) # use_column_width=Trueは、コンテンツの幅に合わせるという意味。

