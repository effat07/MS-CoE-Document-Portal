import streamlit as st
import base64
import os
 
st.set_page_config(page_title="MS CoE Portal", layout="wide", initial_sidebar_state="collapsed")
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;700&display=swap');
 
html, body, [class*="st-"] {
    font-family: 'Manrope', sans-serif;
}
 
.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: 800;
    color: #2A0D5D;
    margin-bottom: 50px;
    margin-top: 20px;
}
 

.home-grid {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 45px;
}
 
.home-card {
    background: white;
    border: 1px solid rgba(0,0,0,0.1);
    border-radius: 20px;
    padding: 30px;
    width: 220px;
    height: 250px;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-decoration: none !important;
}
 
.home-card:hover {
    transform: translateY(-10px);
    box-shadow: 0px 15px 30px rgba(42, 13, 93, 0.2);
    border: 1px solid #2A0D5D;
}
 
.home-card img {
    width: 80px;
    height: 80px;
    margin-bottom: 20px;
}
 
.home-card-title {
    font-size: 20px;
    font-weight: 700;
    color: #2A0D5D;
}
 
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
 
st.markdown('<div class="main-title">Data Practice Document Repository</div>', unsafe_allow_html=True)
 
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""
 
hyperscalers = [
    {"name": "Microsoft", "icon": "microsoft (1).png", "path": "Microsoft"},
    {"name": "AWS", "icon": "aws.png", "path": "Aws"},
    {"name": "GCP", "icon": "gcp.png", "path": "Gcp"},
    {"name": "Snowflake", "icon": "snowflake.png", "path": "Snowflake"},
    {"name": "Databricks", "icon": "databricks.png", "path": "Databricks"}
]
 
cols = st.columns(5)
 
for idx, cloud in enumerate(hyperscalers):
    with cols[idx]:
        icon_b64 = get_base64(f"icons/{cloud['icon']}")
        
        st.markdown(
            f"""
            <a href="/{cloud['path']}" target="_self" style="text-decoration: none;">
                <div class="home-card">
                    <img src="data:image/png;base64,{icon_b64}">
                    <div class="home-card-title">{cloud['name']}</div>
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )
 
