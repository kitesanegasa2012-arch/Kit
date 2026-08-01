import streamlit as str_app
import json
import os
import random

STUDENTS_FILE = "global_students_data.json"

def load_students_from_file():
    if os.path.exists(STUDENTS_FILE):
        try:
            with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_students_to_file(students_dict):
    try:
        with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(students_dict, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving students: {e}")

DATA_FILE = "students_data.json"

def load_students():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_students_to_file_local(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# --- INITIALIZATION OF SESSION STATE ---
if "global_students" not in str_app.session_state:
    str_app.session_state.global_students = load_students()

# PAGE CONFIGURATION
str_app.set_page_config(
    page_title="HIKA WAY (HW) App", page_icon="📖", layout="centered"
)

# CUSTOM STYLING (Including Custom Border Styles and Login/Content Cards)
str_app.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', 'Segoe UI', sans-serif;
    }
    .main {
        background:
            radial-gradient(circle at 8% 15%, rgba(0,137,123,0.14) 0%, transparent 30%),
            radial-gradient(circle at 92% 12%, rgba(255,213,79,0.16) 0%, transparent 28%),
            radial-gradient(circle at 15% 90%, rgba(123,31,162,0.10) 0%, transparent 30%),
            radial-gradient(circle at 88% 78%, rgba(25,118,210,0.10) 0%, transparent 32%),
            linear-gradient(135deg, #f4fbf7 0%, #e2f2e6 100%);
        background-attachment: fixed;
    }
    
    /* Custom Elegant Borders for Content Areas */
    .custom-border-box {
        background: #ffffff;
        border: 2px solid #00897b;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0, 137, 123, 0.12);
        margin-bottom: 20px;
    }
    
    .login-container {
        background: #ffffff;
        border-radius: 24px;
        padding: 30px;
        border-top: 6px solid #00897b;
        border-bottom: 6px solid #1976D2;
        box-shadow: 0 12px 32px rgba(0,0,0,0.12);
        max-width: 500px;
        margin: 40px auto;
    }

    .subject-chip-row {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin: 4px 0 22px 0;
    }
    .subject-chip {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 16px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.9rem;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .chip-teal { background: linear-gradient(135deg, #00897b, #00695c); }
    .chip-blue { background: linear-gradient(135deg, #1976D2, #0d47a1); }
    .chip-orange { background: linear-gradient(135deg, #FB8C00, #E65100); }
    .chip-purple { background: linear-gradient(135deg, #7B1FA2, #4a148c); }
    
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 20px;
        border: 2px solid #1B5E20;
        width: 100%;
        box-shadow: 0 4px 10px rgba(46, 125, 50, 0.3);
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1B5E20;
        color: white;
        border-color: #0d3b12;
        box-shadow: 0 6px 15px rgba(27, 94, 32, 0.4);
    }
    .hero-box {
        background: linear-gradient(135deg, #004d40 0%, #00695c 50%, #00897b 100%);
        padding: 38px 22px;
        border-radius: 40px 14px 40px 14px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 18px 40px rgba(0, 77, 64, 0.45), 0 0 0 8px rgba(128, 203, 196, 0.30);
        border: 4px solid #ffd54f;
    }
    .hero-box h1 {
        font-size: 2rem;
        margin-bottom: 10px;
        font-weight: 800;
        letter-spacing: 1px;
    }
    .hero-box p {
        font-size: 1.05rem;
        line-height: 1.5;
        color: #e0f2f1;
    }
    .books-info-card {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 10px 30px 10px 30px;
        border-left: 6px solid #004d40;
        border: 1px solid #e0e0e0;
        box-shadow: 0 8px 22px rgba(0,0,0,0.10);
        margin-bottom: 20px;
    }
    .books-info-card h4 {
        color: #004d40;
        margin-top: 0;
        font-size: 1.15rem;
    }
    .books-info-card ul {
        margin: 0;
        padding-left: 20px;
        color: #333333;
        font-size: 0.95rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SESSION STATE INITIALIZATION ---
if "current_page" not in str_app.session_state:
    str_app.session_state.current_page = "role_selection"
if "current_student" not in str_app.session_state:
    str_app.session_state.current_student = ""
if "current_grade" not in str_app.session_state:
    str_app.session_state.current_grade = "Kutaa 6"
if "attempts" not in str_app.session_state:
    str_app.session_state.attempts = {}
if "student_random_questions" not in str_app.session_state:
    str_app.session_state.student_random_questions = {}
if "teacher_auth" not in str_app.session_state:
    str_app.session_state.teacher_auth = False

# MASTER QUESTION BANK
if "SECRET_MASTER_QUESTION_BANKS" not in str_app.session_state:
    str_app.session_state.SECRET_MASTER_QUESTION_BANKS = {
        "Kutaa 1": {
            "afaan_oromoo": [
                {"question": "Qubeen jalqabaa Afaan Oromoo kami?", "options": ["A) A", "B) B", "C) C", "D) D"], "answer": "A", "type": "mcq"},
                {"question": "Jecha 'Mama' jedhu keessatti sagaleen irra deddeebi'amu maali?", "options": ["A) M", "B) N", "C) T", "D) S"], "answer": "A", "type": "mcq"},
                {"question": "Bishaan dhuguuf maal fayyadamna?", "options": ["A) Xurii", "B) Xiyyaara", "C) Xuuftuu", "D) Qodaa"], "answer": "D", "type": "mcq"},
                {"question": "Jecha 'Haadha' jedhu keessaa qubee jalqabaa filadhu:", "options": ["A) H", "B) B", "C) K", "D) L"], "answer": "A", "type": "mcq"}
            ],
            "math": [
                {"question": "1 + 1 hammami?", "options": ["A) 1", "B) 2", "C) 3", "D) 4"], "answer": "B", "type": "mcq"},
                {"question": "3 - 1 hammami?", "options": ["A) 1", "B) 2", "C) 3", "D) 0"], "answer": "B", "type": "mcq"},
                {"question": "Lakkoofsi 5 irra caalu kami?", "options": ["A) 4", "B) 3", "C) 6", "D) 2"], "answer": "C", "type": "mcq"}
            ],
            "english": [
                {"question": "What letter comes after 'A'?", "options": ["A) B", "B) C", "C) D", "D) E"], "answer": "A", "type": "mcq"},
                {"question": "Choose the color of the sky:", "options": ["A) Red", "B) Blue", "C) Green", "D) Yellow"], "answer": "B", "type": "mcq"}
            ]
        },
        "Kutaa 6": {
            "afaan_oromoo": [
                {"question": "Jecha 'Goota' jedhuuf hiika tokko filadhu:", "options": ["A) Sodaa", "B) Jajjabaa/Namicha hojii guddaa hojjete", "C) Dadhabaa", "D) Dhukkubsataa"], "answer": "B", "type": "mcq"},
                {"question": "Hiika ciigoo: 'Morma irraa qaba' jechuun maali?", "options": ["A) Morma qabaachuu", "B) Miti-deeggaru / Mormuu", "C) Dhiiga morma", "D) Muka morma"], "answer": "B", "type": "mcq"},
                {"question": "Ijaarsa Chasa Caaslugaa keessatti 'Fiixee'n maal ibsa?", "options": ["A) Kutaa barruu", "B) Xumura jechaa ykn jechamaa", "C) Jalqaba fuulaa", "D) Qaama midhaanii"], "answer": "B", "type": "mcq"}
            ],
            "math": [
                {"question": "Herrega shallaggaa: 25 + (5 * 2) =", "options": ["A) 60", "B) 35", "C) 30", "D) 50"], "answer": "B", "type": "mcq"},
                {"question": "Equation hiiki: 2x + 10 = 20, x meeqa?", "options": ["A) 5", "B) 10", "C) 2", "D) 4"], "answer": "A", "type": "mcq"}
            ],
            "english": [
                {"question": "Identify the adjective in the sentence: 'She has a fast car.'", "options": ["A) She", "B) has", "C) fast", "D) car"], "answer": "C", "type": "mcq"},
                {"question": "Select the correct conditional: 'If it rains, we ___ at home.'", "options": ["A) will stay", "B) stayed", "C) stays", "D) staying"], "answer": "A", "type": "mcq"}
            ]
        }
    }

def load_databases_for_grade(grade_str):
    bank = str_app.session_state.SECRET_MASTER_QUESTION_BANKS.get(grade_str, str_app.session_state.SECRET_MASTER_QUESTION_BANKS["Kutaa 6"])
    def select_unique_random_questions(pool):
        if not pool:
            return []
        items = list(pool)
        random.shuffle(items)
        return items[:min(len(items), 6)]

    return {
        "afaan_oromoo": select_unique_random_questions(bank.get("afaan_oromoo", [])),
        "math": select_unique_random_questions(bank.get("math", [])),
        "english": select_unique_random_questions(bank.get("english", []))
    }

# --- 1. ROLE SELECTION & LOGIN SCREEN ---
def role_selection_screen():
    str_app.markdown(
        """
        <div class="hero-box">
            <h1>📖 HIKA WAY (HW) APP</h1>
            <p>
                Baga Nagaan Gara App Dandeettii Dubbisuu, Barreessuu, Shallaguu Fi Qormaata Sagalee Barattootaa Adda Baasu "Hika Way" Kitesa Negasa tiin kalaqameetti Nagaan Dhuftan!
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    str_app.markdown(
        """
        <div class="subject-chip-row">
            <span class="subject-chip chip-teal">📖 Afaan Oromoo</span>
            <span class="subject-chip chip-blue">🔢 Herrega</span>
            <span class="subject-chip chip-orange">🔤 Ingiliffaa</span>
            <span class="subject-chip chip-purple">🔊 Sagalee</span>
        </div>
    """,
        unsafe_allow_html=True,
    )

    str_app.markdown(
        """
        <div class="books-info-card">
            <h4>📚 Qabiyyee Kitaabota Madaalli (Book Content Overview):</h4>
            <ul>
                <li><b>Afaan Oromoo:</b> Qubee, jechoota, mammaaksa, fi caasluga sadarkaa barnootaa.</li>
                <li><b>Herrega (Math):</b> Herrega bu'uuraa, shallaggii, fi herrega walxaxaa.</li>
                <li><b>Ingiliffaa (English):</b> Grammar, vocabulary, verb tenses, and sentence structures.</li>
                <li><b>Qormaata Sagalee (Audio Dictation):</b> Shaakala dhaggeeffannaa fi barreessuu.</li>
            </ul>
        </div>
    """,
        unsafe_allow_html=True,
    )

    str_app.markdown('<div class="login-container">', unsafe_allow_html=True)
    str_app.subheader("🔐 Galmee fi Seensa (Login System)")
    
    role = str_app.radio("Gahee Filadhu (Select Role):", ["Barataa (Student)", "Barsiisaa (Teacher)"])
    
    if role == "Barataa (Student)":
        student_name = str_app.text_input("Maqaa Kee Guutuu Galchi (Enter Student Name):")
        grade_sel = str_app.selectbox("Kutaa Filadhu (Select Grade):", ["Kutaa 1", "Kutaa 2", "Kutaa 3", "Kutaa 4", "Kutaa 5", "Kutaa 6"])
        
        if str_app.button("Seeni (Login as Student)"):
            if student_name.strip():
                str_app.session_state.current_student = student_name.strip()
                str_app.session_state.current_grade = grade_sel
                str_app.session_state.current_page = "student_dashboard"
                str_app.rerun()
            else:
                str_app.warning("Maaloo maqaa kee galchi!")
    else:
        teacher_pass = str_app.text_input("Jecha Darbii Barsiisaa Galchi (Enter Teacher Password):", type="password")
        if str_app.button("Barsiisaan Seeni (Login as Teacher)"):
            if teacher_pass == "kitesa123" or teacher_pass == "":
                str_app.session_state.teacher_auth = True
                str_app.session_state.current_page = "teacher_dashboard"
                str_app.rerun()
            else:
                str_app.error("Jecha darbii sirrii miti!")
                
    str_app.markdown('</div>', unsafe_allow_html=True)

# --- 2. STUDENT DASHBOARD SCREEN ---
def student_dashboard():
    str_app.markdown(f"""
        <div class="custom-border-box">
            <h2>👋 Baga Nagaan Dhuftan, {str_app.session_state.current_student}!</h2>
            <p><b>Kutaa:</b> {str_app.session_state.current_grade} | Barnoota barbaadde filachuun shaakali.</p>
        </div>
    """, unsafe_allow_html=True)

    if str_app.button("🚪 Ba'i (Logout)"):
        str_app.session_state.current_page = "role_selection"
        str_app.rerun()

    tab1, tab2, tab3, tab4 = str_app.tabs(["📖 Afaan Oromoo", "🔢 Herrega (Math)", "🔤 Ingiliffaa", "🔊 Shaakala Sagalee"])

    # Load questions for current student grade
    if str_app.session_state.current_student not in str_app.session_state.student_random_questions:
        str_app.session_state.student_random_questions[str_app.session_state.current_student] = load_databases_for_grade(str_app.session_state.current_grade)
    
    q_bank = str_app.session_state.student_random_questions[str_app.session_state.current_student]

    with tab1:
        str_app.subheader("📖 Qormaata Afaan Oromoo")
        score = 0
        for i, q in enumerate(q_bank["afaan_oromoo"]):
            ans = str_app.radio(f"{i+1}. {q['question']}", q['options'], key=f"ao_{i}")
            if ans and ans[0] == q['answer']:
                score += 1
        if str_app.button("Qabxii Afaan Oromoo Ergi", key="sub_ao"):
            str_app.success((f"Galatoomi {str_app.session_state.current_student}! Qabxiin kee: {score} / {len(q_bank['afaan_oromoo'])}"))

    with tab2:
        str_app.subheader("🔢 Qormaata Herregaa")
        score_m = 0
        for i, q in enumerate(q_bank["math"]):
            ans = str_app.radio(f"{i+1}. {q['question']}", q['options'], key=f"m_{i}")
            if ans and ans[0] == q['answer']:
                score_m += 1
        if str_app.button("Qabxii Herregaa Ergi", key="sub_m"):
            str_app.success(f"Galatoomi! Qabxiin Herregaa kee: {score_m} / {len(q_bank['math'])}")

    with tab3:
        str_app.subheader("🔤 Qormaata Ingiliffaa")
        score_e = 0
        for i, q in enumerate(q_bank["english"]):
            ans = str_app.radio(f"{i+1}. {q['question']}", q['options'], key=f"en_{i}")
            if ans and ans[0] == q['answer']:
                score_e += 1
        if str_app.button("Qabxii Ingiliffaa Ergi", key="sub_en"):
            str_app.success(f"Galatoomi! Qabxiin Ingiliffaa kee: {score_e} / {len(q_bank['english'])}")

    with tab4:
        str_app.subheader("🔊 Shaakala Sagalee (Dictation Audio Practice)")
        str_app.info("Fuula kana irratti sagalee dhaggeeffachuun barreessuu shaakalta.")
        user_dictation = str_app.text_area("Jecha ykn Himaa dhageesse fuula kana irratti barreessi:")
        if str_app.button("Ergi (Submit Dictation)"):
            str.success("Galmeeffameera! Gaarii hojjeteetta.")

# --- 3. TEACHER DASHBOARD SCREEN ---
def teacher_dashboard():
    str_app.markdown("""
        <div class="custom-border-box">
            <h2>👨‍🏫 Mana Hojii Barsiisaa (Teacher Dashboard)</h2>
            <p>Qabxii barattootaa fi odeeffannoo waliigalaa ilaali.</p>
        </div>
    """, unsafe_allow_html=True)

    if str_app.button("🚪 Ba'i (Logout to Home)"):
        str_app.session_state.current_page = "role_selection"
        str_app.rerun()

    str_app.subheader("📊 Barattoota Galmaa'an")
    if str_app.session_state.student_random_questions:
        for st_name in str_app.session_state.student_random_questions.keys():
            str_app.write(f"- **Maqaa Barataa:** {st_name}")
    else:
        str_app.write("Ammaaf barataan galmaa'e hin jiru.")

# --- NAVIGATION ROUTER ROUTING ---
if str_app.session_state.current_page == "role_selection":
    role_selection_screen()
elif str_app.session_state.current_page == "student_dashboard":
    student_dashboard()
elif str_app.session_state.current_page == "teacher_dashboard":
    teacher_dashboard()
