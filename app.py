
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

st.set_page_config(page_title="MS CoE Documents Repository", layout="wide")

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"]  {{
   font-family: 'Poppins', sans-serif;
}}
.stApp {{
   background: linear-gradient(115deg,#ADD8E6,#f8fafc);
}}
.portal-title {{
   font-size:42px;
   font-weight:700;
   text-align:center;
   background: linear-gradient(90deg,#4f46e5,#06b6d4);
   -webkit-background-clip:text;
   -webkit-text-fill-color:transparent;
   margin-top: 30px;
   margin-bottom:25px;
   letter-spacing:0.5px;
}}
.card {{
   background: rgba(255,255,255,0.65);
   backdrop-filter: blur(10px);
   padding:18px;
   border-radius:16px;
   text-align:center;
   margin-bottom:25px;
   height:160px;
   display:flex;
   flex-direction:column;
   justify-content:center;
   align-items:center;
   border:1px solid rgba(255,255,255,0.2);
   box-shadow:0px 10px 30px rgba(0,0,0,0.08);
   transition:all 0.35s ease;
   cursor:pointer;
}}
.card:hover {{
   transform: translateY(-10px) scale(1.04);
   box-shadow:0px 20px 40px rgba(79,70,229,0.25);
   background: linear-gradient(135deg,#ffffff,#f1f5ff);
}}
.card img {{
   width:95px;
   margin-top: 5px;S
   margin-bottom:5px;
   transition:all 0.3s ease;
}}
.card:hover img {{
   transform:scale(1.15);
   filter: drop-shadow(0px 5px 10px rgba(79,70,229,0.5));
}}
.title {{
   font-size:14px;
   font-weight:600;
   color:#1f2937;
   letter-spacing:0.3px;
}}
.desc {{
   font-size:12px;
   color:#6b7280;
}}

.stSelectbox label {{
   font-weight:600;
}}
.stTextInput>div>div>input {{
   border-radius:12px;
   padding:10px;
}}
.stTextInput input:focus {{
   border:2px solid #4f46e5;
}}
.block-container {{
   padding-top:2rem;
}}
</style>
""", unsafe_allow_html=True)

logo_data = get_icon("icons/microsoft (1).png")
st.markdown(
   f"""
<div class='portal-title'>
<img src="data:image/png;base64,{logo_data}" style="height:45px;width:40px;vertical-align:middle;margin-right:8px;">
       MS CoE Documents Repository
</div>
   """,
   unsafe_allow_html=True
)

df = pd.read_excel("Documents.xlsx", engine="openpyxl")
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
   cols = st.columns(cards_per_row, gap="large")
   for col, (_, row) in zip(cols, df.iloc[i:i+cards_per_row].iterrows()):
       with col:
           icon_html = ""
           if "Icon" in row and pd.notna(row["Icon"]):
               icon_data = get_icon(f"icons/{row['Icon']}.png")
               if icon_data:
                   icon_html = f'<img src="data:image/png;base64,{icon_data}"/>'
           st.markdown(
               f"""
<a href="{row['Url']}" target="_blank" style="text-decoration:none;">
<div class="card">
                   {icon_html}
<div class="title">{row['Title']}</div>
</div>
</a>
               """,
               unsafe_allow_html=True
           )