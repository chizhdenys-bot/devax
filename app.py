import streamlit as st

st.set_page_config(page_title="Devaxx", layout="centered")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stAppDeployDropdown {display: none !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if "text_state" not in st.session_state:
    st.session_state.text_state = "Натисніть кнопку нижче:"

def on_click():
    if st.session_state.text_state == "Натисніть кнопку нижче:":
        st.session_state.text_state = "Кнопку натиснуто!"
    else:
        st.session_state.text_state = "Натисніть кнопку нижче:"

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; font-family: Arial; font-size: 32px;'>{st.session_state.text_state}</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.button("Натисни мене", on_click=on_click, use_container_width=True)
