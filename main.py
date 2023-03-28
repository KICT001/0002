import streamlit as st
st.title('한국건설기술연구원, Google GIS')

agree = st.checkbox('위성지도')
agree = st.checkbox('하천지도')
agree = st.checkbox('지표')

col1, col2 = st.columns(2)

with col2:
    text_input = st.text_input("검색 👇")
    if text_input:
        st.write("검색 지역: ", text_input)

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [36.558663, 128.557559],
    columns=['lat', 'lon'])
st.map(df)

<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>