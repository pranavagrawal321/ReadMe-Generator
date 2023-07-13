import streamlit as st
from screeninfo import get_monitors

st.set_page_config(layout="wide")

st.markdown("<u><h1 style='text-align: center;'>ReadMe Generator</h1><u>", unsafe_allow_html=True)


def run():
    with right_column:
        st.write(input_text)


left_column, right_column = st.columns(2)

with left_column:
    st.header("ReadMe Generator")

    screen_height = get_monitors()[0].height
    input_text = st.text_area("", value='', key=None, height=screen_height - 500, max_chars=None)
    
    with right_column:
        st.header("Output")
        
    if st.button("Submit") or input_text:
        run()
