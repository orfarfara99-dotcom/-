import streamlit as st
import datetime
from streamlit_drawable_canvas import st_canvas

# --- 1. הגדרות דף ---
st.set_page_config(page_title="בקרה קונסטרוקטיבית", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS מעודכן (כפתורים רחבים ויישור לשמאל) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800&display=swap');
    .stApp { background-color: #F4F7FB; font-family: 'Heebo', sans-serif; direction: rtl; }
    #MainMenu, header, footer {visibility: hidden;}
    
    .top-header {
        background: linear-gradient(90deg, #1A4789 0%, #2A64B5 100%);
        color: white; padding: 20px 15px; text-align: center;
        border-bottom-left-radius: 20px; border-bottom-right-radius: 20px;
        margin-top: -60px; margin-bottom: 10px;
    }

    .project-info-bar {
        background-color: #E2E8F0; padding: 12px; border-radius: 8px;
        margin-bottom: 20px; font-size: 0.95rem; color: #1A202C;
        border-right: 5px solid #1A4789; text-align: right;
    }

    /* עיצוב כפתורי האלמנטים - רחבים יותר */
    div.stButton > button {
        background-color: white; color: #1A4789; border-radius: 16px; padding: 18px;
        font-weight: 700; border-right: 6px solid #1A4789; margin-bottom: 15px; 
        width: 100%; text-align: right; font-size: 1.1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    .section-title { 
        color: #1A4789; font-weight: 800; font-size: 1.2rem; 
        margin-bottom: 20px; text-align: center;
    }

    /* יישור כפתור חזרה לשמאל */
    .back-btn-container { 
        display: flex;
        justify-content: flex-start; /* דוחף שמאלה ב-RTL */
        margin-top: 20px;
    }
    .back-btn-container button {
        background-color: transparent !important;
        color: #718096 !important;
        border: 1px solid #CBD5E0 !important;
        border-radius: 12px !important;
        padding: 8px 15px !important;
        font-size: 0.9rem !important;
        width: auto !important;
        text-align: center !important;
    }

    .inspection-row {
        background-color: white; padding: 15px; border-radius: 12px;
        margin-bottom: 15px; border: 1px solid #EAEAEA; text-align: right;
    }
    
    .stButton button[kind="primary"] { background-color: #1A4789 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ניהול מצב (State) ---
if 'screen' not in st.session_state: st.session_state.screen = 'project_info'
if 'project_details' not in st.session_state:
    st.session_state.project_details = {"name": "", "inspector": "", "contractor": "", "date": datetime.date.today()}

def go_to(screen):
    st.session_state.screen = screen
    st.rerun()

# --- 4. מסכי האפליקציה ---

if st.session_state.screen == 'project_info':
    st.markdown('<div class="top-header"><h1>התחברות</h1></div>', unsafe_allow_html=True)
    with st.container():
        st.session_state.project_details['name'] = st.text_input("שם הפרויקט", value=st.session_state.project_details['name'])
        st.session_state.project_details['contractor'] = st.text_input("קבלן מבצע", value=st.session_state.project_details['contractor'])
        st.session_state.project_details['inspector'] = st.text_input("שם המפקח", value=st.session_state.project_details['inspector'])
        if st.button("המשך ←", type="primary"):
            if st.session_state.project_details['name']: go_to('main')

elif st.session_state.screen == 'main':
    st.markdown('<div class="top-header"><h1>תפריט בקרה</h1></div>', unsafe_allow_html=True)
    if st.session_state.project_details['name']:
        st.markdown(f'<div class="project-info-bar">🏗️ <b>פרויקט:</b> {st.session_state.project_details["name"]} | 👷 <b>קבלן:</b> {st.session_state.project_details["contractor"]}</div>', unsafe_allow_html=True)
    
    st.markdown("<div class='section-title'>בחר אלמנט לבדיקה</div>", unsafe_allow_html=True)
    
    # כפתורי אלמנטים - רחבים ונוחים
    st.button("🏢 מבנה בטון", on_click=lambda: go_to('elements'))
    st.button("🔩 מבנה פלדה", on_click=lambda: go_to('elements'))
    st.button("🌉 גשרים", on_click=lambda: go_to('elements'))
    st.button("🚇 מנהור", on_click=lambda: go_to('elements'))
    
    # כפתור חזרה מיושר לשמאל
    st.markdown('<div class="back-btn-container">', unsafe_allow_html=True)
    if st.button("↩️ שנה פרטי פרויקט"): go_to('project_info')
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.screen == 'elements':
    st.markdown('<div class="top-header"><h1>בדיקות</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="inspection-row">כאן תופיע רשימת הבדיקות...</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="back-btn-container">', unsafe_allow_html=True)
    if st.button("← חזרה לתפריט"): go_to('main')
    st.markdown('</div>', unsafe_allow_html=True)
