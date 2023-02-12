import streamlit as st
import base64
from PIL import Image

phn = Image.open("png/phn.png")
st.set_page_config(page_title="Phonepe_Pulse Visualization", page_icon=phn, layout="wide", )

st.header("Visualization of the data")

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("png/bg_vis.png")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

