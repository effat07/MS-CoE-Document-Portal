
import streamlit as st
import pandas as pd
import base64
import os

 
def get_icon(path):
   if os.path.exists(path):
       with open(path, "rb") as f:
           data = f.read()
       return base64.b64encode(data).decode()
   return ""

st.set_page_config(page_title="Databricks CoE Documents Repository", layout="wide")

st.markdown("""
<style>  

[data-testid="stSidebar"], section[data-testid="stSidebar"] {
    display: none !important;
}
 
[data-testid="stSidebarNav"] {
    display: none !important;
}
 

.main .block-container {
    max-width: 100%;
    padding-left: 5rem;
    padding-right: 5rem;
}  
@font-face {
    font-family: 'Manrope';
    src: url('assets/fonts/Manrope-Regular_2533087712.ttf') format("truetype");
    font-weight: 400;
}
@font-face {
    font-family: 'Manrope';
    src: url('assets/fonts/Manrope-Medium_4078546030.ttf') format('truetype');
    font-weight: 500;
}
@font-face {
    font-family: 'Manrope';
    src: url('assets/fonts/Manrope-SemiBold_1138629278.ttf') format('truetype');
    font-weight: 600;
}
@font-face {
    font-family: 'Manrope';
    src: url('assets/fonts/Manrope-Bold_884097420.ttf') format('truetype');
    font-weight: 700;
}
 
html, body, [class*="css"] {    
    font-family: 'Manrope', sans-serif;    
}   
 
.stApp {    
    background: #FFFFFF;    
}    
 

.portal-title {   
    display: flex;
    align-items: center;
    justify-content: center;
    font-size:50px;   
    font-weight: 700;    
    color: #0045BD; 
    margin-top: 20px;    
    margin-bottom: 20px;    
    gap: 15px;    
}    
 

.card {    
    background: rgba(255, 255, 255, 0.65);    
    backdrop-filter: blur(10px);    
    padding: 14px 10px;    
    border-radius: 14px;    
    text-align: left; 
    width: 95%;    
    margin: 10px;    
    height: 220px;    
    display: flex;    
    flex-direction: column;    
    justify-content: flex-start;    
    align-items: flex-start; 
    border: 1px solid rgba(0,0,0,0.08);    
    box-shadow: 0px 2px 8px rgba(0,0,0,0.06);    
    transition: all 0.35s ease;    
    cursor: pointer;    
}    
 
.card:hover {    
    transform: translateY(-6px);    
    box-shadow: 0px 10px 25px rgba(79, 70, 229, 0.18);    
}    
 

.card img {    
    display: block;
    width: 65px; 
    height: 65px;      
    margin-top: 6px;    
    margin-bottom: 6px;    
}    
    
.title {    
    text-align: left;    
    width: 100%;    
    font-size: 16px;    
    font-weight: 700;    
    color: #000000; 
    margin-bottom: 4px;    
}    
 
.desc {    
    font-size: 12px;    
    color: #2A0D5D; 
    margin-top: 4px;    
    line-height: 1.3;    
    text-align: left;    
    max-width: 100%;    
    overflow: hidden;    
    display: -webkit-box;    
    -webkit-line-clamp: 3;    
    -webkit-box-orient: vertical;    
}    
 
.stSelectbox label {    
    font-weight: 600;    
}    
 
.block-container {    
    padding-top:2rem;    
}    
</style>
""", unsafe_allow_html=True)

logo_data = get_icon("icons/databricks.png")
st.markdown(
    f"""
    <div class='portal-title'>    
        <img src="data:image/png;base64,{logo_data}" style="height:50px; width:50px;">    
        <span>Databricks CoE Documents Repository</span>    
    </div>    
    """,
    unsafe_allow_html=True
)

df = pd.read_excel("Databricks.xlsx", engine="openpyxl")
df.columns = df.columns.str.strip()

category = st.selectbox(
   "Category",
   ["All"] + list(df["Category"].dropna().unique())
)
if category != "All":
   df = df[df["Category"] == category]
st.write("")
cards_per_row = 5

for i in range(0, len(df), cards_per_row):
   cols = st.columns(cards_per_row, gap="small")
   for col, (_, row) in zip(cols, df.iloc[i:i+cards_per_row].iterrows()):
       with col:
           icon_html = ""
           if "Icon" in row and pd.notna(row["Icon"]):
               icon_data = get_icon(f"icons/{row['Icon']}.png")
               if icon_data:
                   icon_html = f'<img src="data:image/png;base64,{icon_data}"/>'
           desc_text = ""
           if "Description" in row and pd.notna(row["Description"]):
               desc_text = row["Description"]
           st.markdown(
               f"""
<a href="{row['Url']}" target="_blank" style="text-decoration:none;">
<div class="card">
                       {icon_html}
<div class="title">{row['Title']}</div>
<div class="desc">{desc_text}</div>
</div>
</a>
               """,
               unsafe_allow_html=True
           )