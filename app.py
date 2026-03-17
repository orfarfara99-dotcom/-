import streamlit as st
import datetime
from streamlit_drawable_canvas import st_canvas

# --- 1. הגדרות דף ---
st.set_page_config(page_title="בקרה קונסטרוקטיביות", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS מעודכן (תיקון צבעים ותצוגת מובייל) ---
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
        background-color: #E2E8F0; padding: 10px; border-radius: 8px;
        margin-bottom: 20px; font-size: 0.9rem; color: #2D3748;
        border-right: 4px solid #1A4789;
    }

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
        background-color: white; color: #1A4789; border-radius: 16px; padding: 15px;
        font-weight: 700; border-right: 5px solid #1A4789; margin-bottom: 10px; width: 100%;
        text-align: right; display: block;
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

# פונקציית עזר להצגת פרטי הפרויקט בראש כל מסך
def show_project_bar():
    st.markdown(f"""
        <div class="project-info-bar">
            📍 <b>פרויקט:</b> {st.session_state.project_details['name']} | 
            🏗️ <b>קבלן:</b> {st.session_state.project_details['contractor']} <br>
            👤 <b>מפקח:</b> {st.session_state.project_details['inspector']} | 
            📅 <b>תאריך:</b> {st.session_state.project_details['date']}
        </div>
    """, unsafe_allow_html=True)

# --- 4. מסכי האפליקציה ---

# מסך 1: פרטי פרויקט
if st.session_state.screen == 'project_info':
    st.markdown('<div class="top-header"><h1>התחברות</h1><p>יומן עבודה חדש</p></div>', unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='inspection-row'><div class='section-title'>פרטי הפרויקט</div>", unsafe_allow_html=True)
        st.session_state.project_details['name'] = st.text_input("שם הפרויקט", value=st.session_state.project_details['name'], placeholder="למשל: בניין A1")
        st.session_state.project_details['inspector'] = st.text_input("שם המפקח", value=st.session_state.project_details['inspector'], placeholder="שם המהנדס")
        st.session_state.project_details['contractor'] = st.text_input("קבלן מבצע", value=st.session_state.project_details['contractor'], placeholder="שם חברת הביצוע")
        st.session_state.project_details['date'] = st.date_input("תאריך הבדיקה", value=st.session_state.project_details['date'])
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("המשך לבחירת סוג בקרה ←", type="primary"):
            if st.session_state.project_details['name'] and st.session_state.project_details['contractor']:
                go_to('main')
            else:
                st.error("חובה למלא שם פרויקט וקבלן")

# מסך 2: תפריט ראשי (החזרת כל האלמנטים)
elif st.session_state.screen == 'main':
    st.markdown('<div class="top-header"><h1>בחירת אלמנט</h1></div>', unsafe_allow_html=True)
    show_project_bar()
    
    st.markdown("<div class='section-title'>בחר סוג אלמנט לבדיקה</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏢 מבנה בטון"): go_to('elements')
        if st.button("🛣️ דרכים ופיתוח"): go_to('elements')
    with col2:
        if st.button("🔩 מבנה פלדה"): go_to('elements')
        if st.button("🌉 גשרים ומחלפים"): go_to('elements')
    
    if st.button("🚇 מנהור ותשתית"): go_to('elements')
    if st.button("↩️ חזור לפרטי פרויקט"): go_to('project_info')

# מסך 3: רשימת בדיקות
elif st.session_state.screen == 'elements':
    st.markdown('<div class="top-header"><h1>בדיקת אלמנט</h1></div>', unsafe_allow_html=True)
    show_project_bar()
    
    st.markdown(f"""
        <div class="status-bar">
            <div class="status-box"><h2>87</h2><span>סה"כ</span></div>
            <div class="status-box"><h2>0</h2><span>ליקוי</span></div>
            <div class="status-box"><h2>0</h2><span>תקין</span></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>רשימת תיוג לבדיקה 🏗️</div>", unsafe_allow_html=True)
    
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
        st.markdown(f'<span class="inspection-text">{i+1}. {task}</span>', unsafe_allow_html=True)
        st.selectbox("סטטוס", ["ממתין ⏳", "תקין ✅", "ליקוי ❌"], key=f"sel_{i}")
        st.text_input("הערות/ממצאים", key=f"note_{i}", placeholder="פרט כאן...")
        st.file_uploader("📷 צרף הוכחה מהשטח", key=f"pic_{i}")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("💾 סיום וחתימה", type="primary"): go_to('signature')
    if st.button("← חזרה לתפריט"): go_to('main')

# מסך 4: חתימה
elif st.session_state.screen == 'signature':
    st.markdown('<div class="top-header"><h1>חתימה ואישור</h1></div>', unsafe_allow_html=True)
    show_project_bar()
    
    st.write("אני המפקח החתום מטה מאשר כי הבדיקות בוצעו בהתאם לנהלים.")
    canvas_result = st_canvas(stroke_width=3, stroke_color="#1A4789", background_color="#ffffff", height=200, key="sig_final")
    
    if st.button("הנפק דוח PDF רשמי", type="primary"):
        st.success("הדוח נשלח בהצלחה למשרד!")
        st.balloons()
    
    if st.button("← חזור לעריכה"): go_to('elements')
