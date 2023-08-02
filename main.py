import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレぐレスバーの表示')
"Start!!"

latest_iteration =st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!!!"    





left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
      right_column.write("ここは右カラム")


expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1内容を書く")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2内容を書く")
















# text=st.text_input("あなたの趣味を教えて下さい。")
# condition=st.slider("あなたの今の調子は？",0,100,50)

# "あなたの趣味:",text
# "コンディション:",condition















#if st.checkbox("show Image"):
#    img=Image.open("kinopico_A_picture_of_a_giraffe_wrapping_Danish_bread_around_it_b7f20c62-f44d-494d-8869-c4ca82601625.png")
#    st.image(img, caption="kirin",use_column_width=True)














#df = pd.DataFrame(
#
#    np.random.rand(100, 2)/[50,50]+[35.69,139.70],
#    columns= ["lat","lon"]
#)
#st.table(df.style.highlight_max(axis=0))
#st.map(df)

