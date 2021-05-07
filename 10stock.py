import pandas as pd
# import matplotlib as plt ←代わりにaltairを使う。
import yfinance as yf
import altair as alt
import streamlit as st

# %matplotlib inline
# ↑これはjupyter上で必要だったコード

st.title('米国株化可視化アプリ')


# 第一段階。作っていく。
st.sidebar.write("""
    # GAFA
    こちらは株価可視化ツールです。以下のオプションから表示日数を指定できます。
""")

st.sidebar.write("""
    ## 表示日数選択
""")

days = st.sidebar.slider('日数',1,50,20)

# エフストリングを使う場合は冒頭にf。{days}で、上の行の数字を使うため。
st.write(f""" 
    ### 過去 **{days}日間** のGADA株価
""")


@st.cache # キャッシュ。下のデータを毎回取得せずにキャッシュに為ておける。
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df,hist])
    return df


# 第二段階。作っていく。※tryについては最後に記載。
try:
    st.sidebar.write("""
        ## 株価の範囲指定
    """)
    ymin, ymax = st.sidebar.slider(
        '範囲を指定してください。', 0.0, 3500.0, (0.0, 3500.0) # ()は初期値。その中は、初期値のminと初期値のmaxになる。また、2つの値が返ることになる。
    )

    tickers = {
        'apple': 'AAPL',
        'facebook': 'FB',
        'google': 'GOOGL',
        'microsoft': 'MSFT',
        'netflix': 'NFLX',
        'amazon': 'AMZN'
    }
    df = get_data(days,tickers)
    companies = st.multiselect(
        '会社名を選択してください',
        list(df.index), # dfが表を示す。jupyterで確認すると、df.indexが会社名一覧になる。それをlist()でくくると、リスト形式で渡せる。
        ['google', 'amazon', 'facebook', 'apple'] # デフォルト値の設定。これもリスト。
    )

    # companiesが0社のときに、エラー表示をさせたい。
    if not companies:
        st.error('最低1社は選んでください')
    else:
        data = df.loc[companies] # エラーじゃない場合はデータを表示する、という「定義」をする。
        st.write("### 株価 (USD)", data.sort_index()) # 「,」以降、上で定義したデータを表示したくて記載。なお、更にindexでソートもしておくと見やすいので続けて記載。
        # 一旦ここまで、問題なく表示できた。続いて、以下データの整形。
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)
        # ↑stの中にaltairのchartを表示するメソッドがある。
        # そのメソッドの中にこの上で定義したchartを入れる。
        # use~~~~では、枠に収まる範囲で表示の意味。コンテナサイズと同じで表示する。
except:
    st.error("おっと！何かエラーです")
# tryとexceptで

