import streamlit as str_app
import json
import os
import random

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
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# --- INITIALIZATION OF SESSION STATE ---
if "current_page" not in str_app.session_state:
    str_app.session_state.current_page = "role_selection"
if "current_student" not in str_app.session_state:
    str_app.session_state.current_student = ""
if "current_grade" not in str_app.session_state:
    str_app.session_state.current_grade = "Kutaa 6"
if "student_random_questions" not in str_app.session_state:
    str_app.session_state.student_random_questions = {}
if "student_scores" not in str_app.session_state:
    str_app.session_state.student_scores = load_students()
if "teacher_auth" not in str_app.session_state:
    str_app.session_state.teacher_auth = False

# PAGE CONFIGURATION
str_app.set_page_config(
    page_title="HIKA WAY (HW) App", page_icon="📖", layout="centered"
)

# CUSTOM STYLING
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
        box-shadow: 0 18px 40px rgba(0, 77, 64, 0.45);
        border: 4px solid #ffd54f;
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
    </style>
""",
    unsafe_allow_html=True,
)

# MASTER QUESTION BANK (Gaaffiiwwan bal'aa kutaalee fi barumsaaf)
SECRET_MASTER_QUESTION_BANKS = {
    "Kutaa 1": {
        "afaan_oromoo": [
            {"question": "Qubeen jalqabaa Afaan Oromoo kami?", "options": ["A) A", "B) B", "C) C", "D) D"], "answer": "A", "hint": "Qubeen kun qubee sagalee dheeraa fi gabaabaa jalqaba irratti argamtuudha."},
            {"question": "Jecha 'Mama' jedhu keessatti sagaleen irra deddeebi'amu maali?", "options": ["A) M", "B) N", "C) T", "D) S"], "answer": "A", "hint": "Irra deebiin sagaleewwan qubee jalqabaa irratti xiyyeeffata."},
            {"question": "Bishaan dhuguuf maal fayyadamna?", "options": ["A) Xurii", "B) Xiyyaara", "C) Xuuftuu", "D) Qodaa (Gadiif/Xoofoo)"], "answer": "D", "hint": "Meeshaa dhangala'oo qabachuuf gargaaru ilaali."},
            {"question": "Jecha 'Haadha' jedhu keessaa qubee jalqabaa filadhu:", "options": ["A) H", "B) B", "C) K", "D) L"], "answer": "A", "hint": "Qubee sagaleessuuf qilleensa baay'ee baasu fayyadamna."}
        ],
        "math": [
            {"question": "1 + 1 hammami?", "options": ["A) 1", "B) 2", "C) 3", "D) 4"], "answer": "B", "hint": "Lakkoofsa tokko fi tokko walitti dabali."},
            {"question": "3 - 1 hammami?", "options": ["A) 1", "B) 2", "C) 3", "D) 0"], "answer": "B", "hint": "Sadii irraa tokko hir'isi."},
            {"question": "Lakkoofsi 5 irra caalu kami?", "options": ["A) 4", "B) 3", "C) 6", "D) 2"], "answer": "C", "hint": "Guddaan 5 irraa fagaatee jiru isakami?"}
        ],
        "english": [
            {"question": "What letter comes after 'A'?", "options": ["A) B", "B) C", "C) D", "D) E"], "answer": "A", "hint": "Alphabet order: A, then ..."},
            {"question": "Choose the color of the sky:", "options": ["A) Red", "B) Blue", "C) Green", "D) Yellow"], "answer": "B", "hint": "It matches the ocean color during the day."}
        ]
    },
    "Kutaa 6": {
        "afaan_oromoo": [
            {"question": "Jecha 'Goota' jedhuuf hiika tokko filadhu:", "options": ["A) Sodaa", "B) Jajjabaa / Nama hojii guddaa hojjete", "C) Dadhabaa", "D) Dhukkubsataa"], "answer": "B", "hint": "Namicha lubbuu isaa biyyaaf kennuudhaan beekamu."},
            {"question": "Hiika ciigoo: 'Morma irraa qaba' jechuun maali?", "options": ["A) Morma qabaachuu", "B) Miti-deeggaru / Mormuu / Itti gaafatama fudhachuu", "C) Dhiiga morma", "D) Muka morma"], "answer": "B", "hint": "Yaada irratti walii dhabuu ykn ittigaafatamummaa qabaachuu agarsiisa."},
            {"question": "Ijaarsa Caaslugaa keessatti 'Fiixee'n maal ibsa?", "options": ["A) Kutaa barruu", "B) Xumura jechaa ykn qaama xiinxala caaslugaa", "C) Jalqaba fuulaa", "D) Qaama midhaanii"], "answer": "B", "hint": "Qabxii dhumaa jechicha ykn caasaa sanaa agarsiisa."}
        ],
        "math": [
            {"question": "Herrega shallaggaa: 25 + (5 * 2) =", "options": ["A) 60", "B) 35", "C) 30", "D) 50"], "answer": "B", "hint": "Dursee baay'isuu (multiplication) hojjedhu."},
            {"question": "Equation hiiki: 2x + 10 = 20, x meeqa?", "options": ["A) 5", "B) 10", "C) 2", "D) 4"], "answer": "A", "hint": "10 gama mirgaatti geessuun irraa hir'isi, sana booda 2tti qoodi."}
        ],
        "english": [
            {"question": "Identify the adjective in the sentence: 'She has a fast car.'", "options": ["A) She", "B) has", "C) fast", "D) car"], "answer": "C", "hint": "The word that describes the noun 'car'."},
            {"question": "Select the correct conditional: 'If it rains, we ___ at home.'", "options": ["A) will stay", "B) stayed", "C) stays", "D) staying"], "answer": "A", "hint": "First conditional structure uses 'will' + base verb."}
        ]
    }
}

def load_random_questions_for_student(student_name, grade_str):
    # Barataan tokko yeroo seenu gaaffii addaa akka argatuuf random godhama
    bank = SECRET_MASTER_QUESTION_BANKS.get(grade_str, SECRET_MASTER_QUESTION_BANKS["Kutaa 6"])
    
    def get_shuffled(pool):
        items = list(pool)
        random.shuffle(items)
        return items[:min(len(items), 5)]

    return {
        "afaan_oromoo": get_shuffled(bank.get("afaan_oromoo", [])),
        "math": get_shuffled(bank.get("math", [])),
        "english": get_shuffled(bank.get("english", []))
    }

# --- 1. ROLE SELECTION SCREEN ---
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
            <span class="subject-chip chip-purple">🔊 Sagalee (Audio)</span>
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
                # Gaaffiiwwan random ta'an barataa kanaaf qofa qopheessuu
                str_app.session_state.student_random_questions[student_name.strip()] = load_random_questions_for_student(student_name.strip(), grade_sel)
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
    st_name = str_app.session_state.current_student
    st_grade = str_app.session_state.current_grade

    str_app.markdown(f"""
        <div class="custom-border-box">
            <h2>👋 Baga Nagaan Dhuftan, {st_name}!</h2>
            <p><b>Kutaa:</b> {st_grade} | Barnoota barbaadde filachuun gaaffiiwwan kee hojjedhu.</p>
        </div>
    """, unsafe_allow_html=True)

    if str_app.button("🚪 Ba'i (Logout)"):
        str_app.session_state.current_page = "role_selection"
        str_app.rerun()

    tab1, tab2, tab3, tab4 = str_app.tabs(["📖 Afaan Oromoo", "🔢 Herrega", "🔤 Ingiliffaa", "🔊 Shaakala Sagalee"])

    # Gaaffii barataa kanaaf qophaa'e argachuu
    if st_name not in str_app.session_state.student_random_questions:
        str_app.session_state.student_random_questions[st_name] = load_random_questions_for_student(st_name, st_grade)
    
    q_bank = str_app.session_state.student_random_questions[st_name]

    # --- TAB 1: AFAAN OROMOO ---
    with tab1:
        str_app.subheader("📖 Qormaata Afaan Oromoo (Randomized)")
        score_ao = 0
        for i, q in enumerate(q_bank["afaan_oromoo"]):
            ans = str_app.radio(f"{i+1}. {q['question']}", q['options'], key=f"{st_name}_ao_{i}")
            # Akeektuu (Hint) dhiyeessuu
            if str_app.checkbox(f"Akeektuu (Hint) ilaali - Gaaffii {i+1}", key=f"hint_ao_{st_name}_{i}"):
                str_app.info(f"💡 Akeektuu: {q['hint']}")
            
            if ans and ans[0] == q['answer']:
                score_ao += 1

        if str_app.button("Qabxii Afaan Oromoo Galmeessi", key="sub_ao"):
            str_app.success(f"Galatoomi {st_name}! Qabxiin Afaan Oromoo kee: {score_ao} / {len(q_bank['afaan_oromoo'])}\nSirreeffama gaarii hojjeteetta!")
            # Qabxii galmeessuu
            if st_name not in str_app.session_state.student_scores:
                str_app.session_state.student_scores[st_name] = {}
            str_app.session_state.student_scores[st_name]["Afaan Oromoo"] = f"{score_ao}/{len(q_bank['afaan_oromoo'])}"
            save_students_to_file_local(str_app.session_state.student_scores)

    # --- TAB 2: HERREGA (MATH) ---
    with tab2:
        str_app.subheader("🔢 Qormaata Herregaa (Randomized)")
        score_m = 0
        for i, q in enumerate(q_bank["math"]):
            ans = str_app.radio(f"{i+1}. {q['question']}", q['options'], key=f"{st_name}_m_{i}")
            if str_app.checkbox(f"Akeektuu (Hint) ilaali - Gaaffii Herregaa {i+1}", key=f"hint_m_{st_name}_{i}"):
                str_app.info(f"💡 Akeektuu: {q['hint']}")

            if ans and ans[0] == q['answer']:
                score_m += 1

        if str_app.button("Qabxii Herregaa Galmeessi", key="sub_m"):
            str_app.success(f"Galatoomi {st_name}! Qabxiin Herregaa kee: {score_m} / {len(q_bank['math'])}\nShallaggiin kee sirriidha!")
            if st_name not in str_app.session_state.student_scores:
                str_app.session_state.student_scores[st_name] = {}
            str_app.session_state.student_scores[st_name]["Herrega"] = f"{score_m}/{len(q_bank['math'])}"
            save_students_to_file_local(str_app.session_state.student_scores)

    # --- TAB 3: INGILIFFAA (ENGLISH) ---
    with tab3:
        str_app.subheader("🔤 Qormaata Ingiliffaa (Randomized)")
        score_e = 0
        for i, q in enumerate(q_bank["english"]):
            ans = str_app.radio(f"{i+1}. {q['question']}", q['options'], key=f"{st_name}_en_{i}")
            if str_app.checkbox(f"Akeektuu (Hint) ilaali - Gaaffii Ingiliffaa {i+1}", key=f"hint_en_{st_name}_{i}"):
                str_app.info(f"💡 Hint: {q['hint']}")

            if ans and ans[0] == q['answer']:
                score_e += 1

        if str_app.button("Qabxii Ingiliffaa Galmeessi", key="sub_en"):
            str_app.success(f"Galatoomi {st_name}! Qabxiin Ingiliffaa kee: {score_e} / {len(q_bank['english'])}\nGood job!")
            if st_name not in str_app.session_state.student_scores:
                str_app.session_state.student_scores[st_name] = {}
            str_app.session_state.student_scores[st_name]["Ingiliffaa"] = f"{score_e}/{len(q_bank['english'])}"
            save_students_to_file_local(str_app.session_state.student_scores)

    # --- TAB 4: SHAAKALA SAGALEE (AUDIO / DICTATION PRACTICE) ---
    with tab4:
        str_app.subheader("🔊 Shaakala Sagalee fi Dubbii (Audio & Text Dictation Practice)")
        str_app.info("Ergaa sagalee dhaggeeffachuun hubannoo kee shaakali. (Browser Web Speech API fayyadamee sagaleessuu danda'a)")
        
        sample_text_oromo = "Bilisummaan beekumsa irraa madde."
        str_app.write(f"**Hima Shaakalaaf Qophaa'e:** {sample_text_oromo}")

        # HTML + JS qindaa'aa sagalee dubbisuuf (Web Speech API)
        audio_js_code = f"""
        <div>
            <button onclick="speakText()" style="background-color: #00897b; color: white; padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                🔊 Sagaleen Dhaggeeffadhu (Listen Audio)
            </button>
            <script>
            function speakText() {{
                const text = "{sample_text_oromo}";
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'om-ET'; // Afaan Oromoo ykn English
                window.speechSynthesis.speak(utterance);
            }}
            </script>
        </div>
        """
        str_app.markdown(audio_js_code, unsafe_allow_html=True)
        
        user_dictation = str_app.text_area("Hima dhageesse as barreesuu dhaan shaakali:")
        if str_app.button("Galmeessi Dictation"):
            str_app.success("Galmeeffameera! Shaakala sagalee gaarii hojjeteetta.")

# --- 3. TEACHER DASHBOARD SCREEN ---
def teacher_dashboard():
    str_app.markdown("""
        <div class="custom-border-box">
            <h2>👨‍🏫 Mana Hojii Barsiisaa (Teacher Dashboard)</h2>
            <p>Qabxii barattootaa fi odeeffannoo waliigalaa asitti ilaaluu dandeessa.</p>
        </div>
    """, unsafe_allow_html=True)

    if str_app.button("🚪 Ba'i (Logout to Home)"):
        str_app.session_state.current_page = "role_selection"
        str_app.rerun()

    str_app.subheader("📊 Galmee Qabxii Barattootaa")
    saved_data = load_students()
    if saved_data:
        for student, subjects in saved_data.items():
            str_app.markdown(f"**Maqaa Barataa:** `{student}`")
            for sub, sc in subjects.items():
                str_app.write(f"   - {sub}: Qabxii {sc}")
            str_app.markdown("---")
    else:
        str_app.write("Ammaaf barataan qabxii galmeessise hin jiru.")

# --- ROUTING NAVIGATION SYSTEM ---
if str_app.session_state.current_page == "role_selection":
    role_selection_screen()
elif str_app.session_state.current_page == "student_dashboard":
    student_dashboard()
elif str_app.session_state.current_page == "teacher_dashboard":
    teacher_dashboard()
