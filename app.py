import streamlit as st
import datetime
from streamlit_drawable_canvas import st_canvas

# --- 1. הגדרות דף ---
st.set_page_config(page_title="בקרה קונסטרוקטיביות", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS מעודכן עם תיקון צבע טקסט ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800&display=swap');
    .stApp { background-color: #F4F7FB; font-family: 'Heebo', sans-serif; direction: rtl; text-align: right; }
    #MainMenu, header, footer {visibility: hidden;}
    
    /* תיקון לצבע המלל של הבדיקות */
    .inspection-text {
        color: #1A4789 !important; 
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        display: block;
        margin-bottom: 10px;
        text-align: right;
    }

    .top-header {
        background: linear-gradient(90deg, #1A4789 0%, #2A64B5 100%);
        color: white; padding: 20px 15px; text-align: center;
        border-bottom-left-radius: 20px; border-bottom-right-radius: 20px;
        margin-top: -60px; margin-bottom: 20px;
    }
    .top-header h1 { color: white !important; font-size: 1.6rem !important; margin: 0; }

    .status-bar {
        display: flex; justify-content: space-between; background-color: #2A64B5;
        padding: 10px 15px; border-radius: 12px; color: white; margin-bottom: 20px;
    }
    .status-box { text-align: center; background: rgba(255,255,255,0.1); padding: 8px 12px; border-radius: 8px; flex: 1; margin: 0 5px; }
    .status-box h2 { color: white !important; margin: 0; font-size: 1.3rem; }

    .inspection-row {
        background-color: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 15px; border: 1px solid #EAEAEA;
    }
    
    .section-title { color: #1A4789; font-weight: 800; font-size: 1.2rem; margin-bottom: 15px; border-bottom: 2px solid #E2E8F0; padding-bottom: 5px; }

    div.stButton > button {
        background-color: white; color: #1A4789; border-radius: 16px; padding: 12px;
        font-weight: 700; border-right: 5px solid #1A4789; margin-bottom: 10px; width: 100%;
    }
    .stButton button[kind="primary"] { background-color: #1A4789 !important; color: white !important; }
    
    /* תיקון לכותרות של שדות קלט במובייל */
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

# --- 4. מסכי האפליקציה ---

if st.session_state.screen == 'project_info':
    st.markdown('<div class="top-header"><h1>התחברות</h1><p>יומן עבודה חדש</p></div>', unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='inspection-row'><div class='section-title'>פרטי הפרויקט</div>", unsafe_allow_html=True)
        st.session_state.project_details['name'] = st.text_input("שם הפרויקט", value=st.session_state.project_details['name'])
        st.session_state.project_details['inspector'] = st.text_input("שם המפקח", value=st.session_state.project_details['inspector'])
        st.session_state.project_details['contractor'] = st.text_input("קבלן מבצע", value=st.session_state.project_details['contractor'])
        st.session_state.project_details['date'] = st.date_input("תאריך", value=st.session_state.project_details['date'])
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("המשך לבחירת סוג בקרה ←", type="primary"):
            if st.session_state.project_details['name']: go_to('main')
            else: st.error("חובה למלא שם פרויקט")

elif st.session_state.screen == 'main':
    st.markdown('<div class="top-header"><h1>תפריט ראשי</h1></div>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>בחר סוג אלמנט</div>", unsafe_allow_html=True)
    if st.button("🏢 מבנה בטון"): go_to('elements')
    if st.button("🔩 מבנה פלדה"): go_to('elements')
    if st.button("🚇 מנהור"): go_to('elements')

elif st.session_state.screen == 'elements':
    st.markdown('<div class="top-header"><h1>בדיקות שטח</h1></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="status-bar">
            <div class="status-box"><h2>87</h2><span>סה"כ</span></div>
            <div class="status-box"><h2>0</h2><span>ליקוי</span></div>
            <div class="status-box"><h2>0</h2><span>תקין</span></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>יסודות וקירות תת-קרקעיים 🏗️</div>", unsafe_allow_html=True)
    
    full_tasks = [
        "בדיקת עומק יסוד לפי תוכנית (mm ±50)",
        "בדיקת ממדי היסוד (אורך x רוחב x גובה)",
        "ניקוי קרקע - ללא שאריות עפר רופף",
        "עובי בטון רזה: מינימום 50 מ\"מ",
        "כיסוי בטון תחתון ≥ 50 מ\"מ",
        "הכנה לאטימות - ממברנה / ביטומן"
    ]
    
    for i, task in enumerate(full_tasks):
        st.markdown(f'<div class="inspection-row">', unsafe_allow_html=True)
        # שימוש בקלאס החדש כדי להבטיח שהטקסט ייראה
        st.markdown(f'<span class="inspection-text">{i+1}. {task}</span>', unsafe_allow_html=True)
        st.selectbox("סטטוס", ["ממתין ⏳", "תקין ✅", "ליקוי ❌"], key=f"sel_{i}")
        st.text_input("הערות", key=f"note_{i}", placeholder="הוסף הערה...")
        st.file_uploader("📷 צרף צילום", key=f"pic_{i}")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💾 סיום וחתימה", type="primary"): go_to('signature')
    if st.button("← חזרה"): go_to('main')

elif st.session_state.screen == 'signature':
    st.markdown('<div class="top-header"><h1>חתימה ואישור</h1></div>', unsafe_allow_html=True)
    st.write(f"מאשר את הבדיקה עבור פרויקט: **{st.session_state.project_details['name']}**")
    canvas_result = st_canvas(stroke_width=3, stroke_color="#1A4789", background_color="#ffffff", height=200, key="sig")
    if st.button("הנפק דוח סופי", type="primary"):
        st.success("הדוח הופק בהצלחה!")
        st.balloons()
