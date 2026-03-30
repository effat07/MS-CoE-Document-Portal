
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
   background: #FFFFFF;
}}
.portal-title {{
   font-size:42px;
   font-weight:700;
   text-align:center;
   background: #2A0D5D;
   -webkit-background-clip:text;
   -webkit-text-fill-color:transparent;
   margin-top: 30px;
   margin-bottom:25px;
   letter-spacing:0px;
}}
.card {{
   background: rgba(255,255,255,0.65);
   backdrop-filter: blur(10px);
   padding:14px 10px;
   border-radius:14px;
   text-align:center;
   # margin-bottom:10px;
   width:200px;
   margin:8px;
   height:200px;
   display:flex;
   flex-direction:column;
   justify-content:flex-start;
   align-items:center;
   border:1px solid rgba(0,0,0,0.08);
   box-shadow:0px 4px 10px rgba(0,0,0,0.08);
   transition:all 0.35s ease;
   cursor:pointer;
}}
.card:hover {{
   transform: translateY(-10px) scale(1.04);
   box-shadow:0px 20px 40px rgba(79,70,229,0.25);
   background: linear-gradient(135deg,#ffffff,#f1f5ff);
}}
.card img {{
   width:75px;
   margin-top: 6px;
   margin-bottom:4px;
   transition:all 0.3s ease;
}}
.card:hover img {{
   transform:scale(1.15);
   filter: drop-shadow(0px 5px 10px rgba(79,70,229,0.5));
}}
.title {{
   font-size:14px;
   font-weight:600;
   color:#2A0D5D;
   # letter-spacing:0.3px;
   margin-bottom:3px;
}}

.desc {{
   font-size: 12px;
   color: #6b7280;
   margin-top: 4px;
   line-height: 1.3;
   text-align: center;
   max-width:100%
   overflow:hidden;
   display:-webkit-box;
   -webkit-line-clamp:3;
   -webkit-box-orient:vertical;
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
<img src="data:image/png;base64,{logo_data}" style="height:65px;width:50px;vertical-align:middle;margin-right:8px;">
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