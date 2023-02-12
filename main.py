import streamlit as st
import base64
from PIL import Image
import os
import json
import subprocess
import pandas
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import sqlite3
import requests

phn = Image.open("images/phn.png")
st.set_page_config(page_title="Phonepe_Pulse", page_icon=phn, layout="wide", )


def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("images/pe.png")

#page_bg_img = f"""
#<style>
#[data-testid="stSidebar"]> div:first-child{{
#background-image: url("data:image/jpg;base64,{img}");
#background-position:cover;
#background-repeat: no-repeat;
#background-attachment: absolute;
#}}
#</style>
#"""
#st.markdown(page_bg_img, unsafe_allow_html=True)

#st.sidebar.markdown("<h1 style='text-align: center;'>Streamlit App</h1>", unsafe_allow_html=True)

#CLONING TH PHONEPE--PULSE GITHUB REPOSITORY

response = requests.get('https://api.github.com/repos/PhonePe/pulse')
repo = response.json()
clone_url = repo['clone_url']

#DIRECTING THE REPOSITORY TO THE LOCAL DIRECTORY

repo_name = "pulse"
clone_dir = os.path.join(os.getcwd(), repo_name)

#subprocess.run(["git", "clone", clone_url, clone_dir], check=True)

# TO GET THE DATA-FRAME OF AGGREGATED <--> TRANSACTION

path1 = "/home/vazanth/PycharmProjects/phonepe/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path1)

col1 = {'State': [], 'Year': [], 'Quater': [], 'Transaction_type': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in Agg_state_list:
    p_i = path1 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            A = json.load(Data)
            for z in A['data']['transactionData']:
                Name = z['name']
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']
                col1['Transaction_type'].append(Name)
                col1['Transaction_count'].append(count)
                col1['Transaction_amount'].append(amount)
                col1['State'].append(i)
                col1['Year'].append(j)
                col1['Quater'].append(int(k.strip('.json')))
df_aggregated_transaction = pd.DataFrame(col1)
# df_aggregated_transaction

# TO GET THE DATA-FRAME OF AGGREGATED <--> USER

path2 = "/home/vazanth/PycharmProjects/phonepe/pulse/data/aggregated/user/country/india/state/"
user_list = os.listdir(path2)

col2 = {'State': [], 'Year': [], 'Quater': [], 'brands': [], 'Count': [],
        'Percentage': []}
for i in user_list:
    p_i = path2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            B = json.load(Data)
            try:
                for w in B["data"]["usersByDevice"]:
                    brand_name = w["brand"]
                    count_ = w["count"]
                    ALL_percentage = w["percentage"]
                    col2["brands"].append(brand_name)
                    col2["Count"].append(count_)
                    col2["Percentage"].append(ALL_percentage)
                    col2["State"].append(i)
                    col2["Year"].append(j)
                    col2["Quater"].append(int(k.strip('.json')))
            except:
                pass
df_aggregated_user = pd.DataFrame(col2)
# df_aggregated_user

# TO GET THE DATA-FRAME OF MAP <--> TRANSACTION

path3 = "/home/vazanth/PycharmProjects/phonepe/pulse/data/map/transaction/hover/country/india/state/"
hover_list = os.listdir(path3)

col3 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'count': [],
        'amount': []}
for i in hover_list:
    p_i = path3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            C = json.load(Data)
            for x in C["data"]["hoverDataList"]:
                District = x["name"]
                count = x["metric"][0]["count"]
                amount = x["metric"][0]["amount"]
                col3["District"].append(District)
                col3["count"].append(count)
                col3["amount"].append(amount)
                col3['State'].append(i)
                col3['Year'].append(j)
                col3['Quater'].append(int(k.strip('.json')))
df_map_transaction = pd.DataFrame(col3)
# df_map_transaction

# TO GET THE DATA-FRAME OF MAP <--> USER

path4 = "/home/vazanth/PycharmProjects/phonepe/pulse/data/map/user/hover/country/india/state/"
map_list = os.listdir(path4)

col4 = {"State": [], "Year": [], "Quater": [], "District": [],
        "RegisteredUser": []}
for i in map_list:
    p_i = path4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            D = json.load(Data)

            for u in D["data"]["hoverData"].items():
                district = u[0]
                registereduser = u[1]["registeredUsers"]
                col4["District"].append(district)
                col4["RegisteredUser"].append(registereduser)
                col4['State'].append(i)
                col4['Year'].append(j)
                col4['Quater'].append(int(k.strip('.json')))
df_map_user = pd.DataFrame(col4)
# df_map_user

# TO GET THE DATA-FRAME OF TOP <--> TRANSACTION

path5 = "/home/vazanth/PycharmProjects/phonepe/pulse/data/top/transaction/country/india/state/"
TOP_list = os.listdir(path5)

col5 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in TOP_list:
    p_i = path5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            E = json.load(Data)
            for z in E['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                col5['District'].append(Name)
                col5['Transaction_count'].append(count)
                col5['Transaction_amount'].append(amount)
                col5['State'].append(i)
                col5['Year'].append(j)
                col5['Quater'].append(int(k.strip('.json')))
df_top_transaction = pd.DataFrame(col5)
# df_top_transaction

# TO GET THE DATA-FRAME OF TOP <--> USER

path6 = "/home/vazanth/PycharmProjects/phonepe/pulse/data/top/user/country/india/state/"
USER_list = os.listdir(path6)

col6 = {'State': [], 'Year': [], 'Quater': [], 'District': [],
        'RegisteredUser': []}
for i in USER_list:
    p_i = path6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            F = json.load(Data)
            for t in F['data']['pincodes']:
                Name = t['name']
                registeredUser = t['registeredUsers']
                col6['District'].append(Name)
                col6['RegisteredUser'].append(registeredUser)
                col6['State'].append(i)
                col6['Year'].append(j)
                col6['Quater'].append(int(k.strip('.json')))
df_top_user = pd.DataFrame(col6)
# df_top_user

#CREATING CONNECTION WITH SQL SERVER
connection = sqlite3.connect("phonepe pulse.db")
cursor = connection.cursor()
df_aggregated_transaction.to_sql('aggregated_transaction', connection, if_exists='replace')
df_aggregated_user.to_sql('aggregated_user', connection, if_exists='replace')
df_map_transaction.to_sql('map_transaction', connection, if_exists='replace')
df_map_user.to_sql('map_user', connection, if_exists='replace')
df_top_transaction.to_sql('top_transaction', connection, if_exists='replace')
df_top_user.to_sql('top_user', connection, if_exists='replace')



cursor.execute("SELECT Transaction_amount,State,Year,Quater FROM top_transaction ORDER BY Transaction_amount DESC LIMIT 10");
df = pd.DataFrame(cursor.fetchall(),columns=['Transaction_amount','State','Year','Quater'])
#year_option = df_top_transaction['Year'].unique().tolist()
#year = st.selectbox("which year would you like to see?",year_option,0)

st.sidebar.success("STOP ASKING START SEARCHING")
option = ["--SELECT OPTION--","BASIC INSIGHTS","CUSTOMIZED INSIGHTS"]
SELECT = st.sidebar.selectbox("SELECT",option,0)
if SELECT=="BASIC INSIGHTS":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--","Top 5 States by transaction amount","Highest  type of transaction","Top 5 Districts by transaction amount",
               "Top mobile brands used for transactions","Top 5 Lowest transaction States","Top registerd user in 5 states","Top 5 highest transaction amount",
               "Top 5 lowest transaction amount","Top 5 highest transaction count","Top 5 lowest transaction count"]
    select = st.sidebar.selectbox("SELECT",options,0)

