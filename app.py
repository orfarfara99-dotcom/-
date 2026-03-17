import streamlit as st
import datetime
from streamlit_drawable_canvas import st_canvas

# --- 1. הגדרות דף ---
st.set_page_config(page_title="בקרה קונסטרוקטיבית", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS מעודכן (מרכוז חזק ותיקוני עיצוב) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800&display=swap');
    .stApp { background-color: #F4F7FB; font-family: 'Heebo', sans-serif; direction: rtl; text-align: right; }
    #MainMenu, header, footer {visibility: hidden;}
    
    .inspection-text {
        color: #1A4789 !important; 
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        display: block; margin-bottom: 10px; text-align: right;
    }

    .top-header {
        background: linear-gradient(90deg, #1A4789 0%, #2A64B5 100%);
        color: white; padding: 20px 15px; text-align: center;
        border-bottom-left-radius: 20px; border-bottom-right-radius: 20px;
        margin-top: -60px; margin-bottom: 10px;
    }
    .top-header h1 { color: white !important; font-size: 1.6rem !important; margin: 0; }

    .project-info-bar {
        background-color: #E2E8F0; padding: 12px; border-radius: 8px;
        margin-bottom: 20px; font-size: 0.95rem; color: #1A202C;
        border-right: 5px solid #1A4789; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: right;
    }

    /* מרכוז תפריט הכפתורים */
    .stButton {
        display: flex;
        justify-content: center;
    }

    div.stButton > button {
        background-color: white; color: #1A4789; border-radius: 16px; padding: 15px;
        font-weight: 700; border-right: 6px solid #1A4789; margin-bottom: 12px; 
        width: 100%; max-width: 400px; /* מגביל רוחב כדי שייראה טוב במרכז */
        text-align: center; transition: 0.3s;
        margin-left: auto; margin-right: auto;
    }

    .section-title { 
        color: #1A4789; font-weight: 800; font-size: 1.2rem; 
        margin-bottom: 20px; text-align: center; width: 100%;
    }

    .back-btn button {
        background-color: transparent !important;
        color: #718096 !important;
        border: 1px solid #CBD5E0 !important;
        border-right: 1px solid #CBD5E0 !important;
        font-size: 0.85rem !important;
        padding: 8px 20px !important;
        margin-top: 20px !important;
        width: auto !important;
        max-width: 200px !important;
    }

    .inspection-row {
        background-color: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 15px; border: 1px solid #EAEAEA;
    }

    .stButton button[kind="primary"] { background-color: #1A4789 !important; color: white !important; }
    label { color: #4A5568 !important; font-weight: 600 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ניהול מצב (State) ---
if 'screen' not in st.session_state: st.session_state.screen = 'project_info'
if 'project_details' not in st.session_state:
    st.session_state.project_details = {"name": "", "inspector": "", "contractor": "", "date": datetime.date.today()}

def go_to(screen):
    st.session_state.screen = screen
    st.rerun()

def show_header_info():
    if st.session_state.project_details['name']:
        st.markdown(f"""
            <div class="project-info-bar">
                🏗️ <b>פרויקט:</b> {st.session_state.project_details['name']} | 
                👷 <b>קבלן:</b> {st.session_state.project_details['contractor']}
            </div>
        """, unsafe_allow_html=True)

# --- 4. מסכי האפליקציה ---

if st.session_state.screen == 'project_info':
    st.markdown('<div class="top-header"><h1>התחברות</h1><p>פרטי בקרה</p></div>', unsafe_allow_html=True)
    with st.container():
        st.session_state.project_details['name'] = st.text_input("שם הפרויקט", value=st.session_state.project_details['name'])
        st.session_state.project_details['contractor'] = st.text_input("קבלן מבצע", value=st.session_state.project_details['contractor'])
        st.session_state.project_details['inspector'] = st.text_input("שם המפקח", value=st.session_state.project_details['inspector'])
        st.session_state.project_details['date'] = st.date_input("תאריך", value=st.session_state.project_details['date'])
        
        if st.button("המשך לבחירת סוג בקרה ←", type="primary"):
            if st.session_state.project_details['name'] and st.session_state.project_details['contractor']: go_to('main')
            else: st.error("יש למלא שם פרויקט וקבלן")

elif st.session_state.screen == 'main':
    st.markdown('<div class="top-header"><h1>תפריט בקרה</h1></div>', unsafe_allow_html=True)
    show_header_info()
    
    st.markdown("<div class='section-title'>בחר אלמנט לבדיקה</div>", unsafe_allow_html=True)
    
    # הצגת הכפתורים אחד מתחת לשני, מיושרים למרכז דרך ה-CSS
    st.button("🏢 מבנה בטון", on_click=lambda: go_to('elements'))
    st.button("🔩 מבנה פלדה", on_click=lambda: go_to('elements'))
    st.button("🌉 גשרים", on_click=lambda: go_to('elements'))
    st.button("🚇 מנהור", on_click=lambda: go_to('elements'))
    
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("↩️ שנה פרטי פרויקט"): go_to('project_info')
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.screen == 'elements':
    st.markdown('<div class="top-header"><h1>בדיקות שטח</h1></div>', unsafe_allow_html=True)
    show_header_info()
    
    tasks = ["בדיקת עומק יסוד (mm ±50)", "בדיקת ממדי היסוד", "ניקוי קרקע", "עובי בטון רזה", "כיסוי בטון תחתון", "הכנה לאטימות"]
    
    for i, task in enumerate(tasks):
        st.markdown(f'<div class="inspection-row"><span class="inspection-text">{i+1}. {task}</span>', unsafe_allow_html=True)
        st.selectbox("סטטוס", ["ממתין ⏳", "תקין ✅", "ליקוי ❌"], key=f"s_{i}")
        st.text_input("הערות", key=f"n_{i}")
        st.file_uploader("📷 צרף תמונה", key=f"p_{i}")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💾 סיום וחתימה", type="primary"): go_to('signature')
    
    st.markdown('<div class="back-btn" style="text-align:center;">', unsafe_allow_html=True)
    if st.button("← חזרה לתפריט"): go_to('main')
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.screen == 'signature':
    st.markdown('<div class="top-header"><h1>חתימה ואישור</h1></div>', unsafe_allow_html=True)
    show_header_info()
    st_canvas(stroke_width=3, stroke_color="#1A4789", background_color="#ffffff", height=150, key="sig_final")
    if st.button("הנפק דוח סופי", type="primary"):
        st.success("הדוח נשלח!")
        st.balloons()
    
    st.markdown('<div class="back-btn" style="text-align:center;">', unsafe_allow_html=True)
    if st.button("← חזור לבדיקות"): go_to('elements')
    st.markdown('</div>', unsafe_allow_html=True)
