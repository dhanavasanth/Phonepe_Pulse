import streamlit as st
from PIL import Image
import base64
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


phn = Image.open("png/phn.png")
st.set_page_config(page_title="Phonepe_Pulse Visualization", page_icon=phn, layout="wide", )

st.title("PHONEPE PULSE -- VISUALIZATION-- SQL DATABASE")

st.write("----")


