import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

st.markdown("[Section 1](#section-1)")


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

file = st.file_uploader("Upload a file", type="")

import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)



