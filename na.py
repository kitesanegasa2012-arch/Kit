import json
import os
import random
import streamlit as str_app

# PAGE CONFIGURATION
str_app.set_page_config(
    page_title="HIKA WAY (HW) App", page_icon="📖", layout="centered"
)

# CUSTOM STYLING
str_app.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f4fbf7 0%, #e2f2e6 100%);
    }
    .student-btn button {
        background-color: #1976D2;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 22px;
        border: 2px solid #0d47a1;
        width: 100%;
        box-shadow: 0 4px 10px rgba(25, 118, 210, 0.3);
        transition: 0.3s ease;
    }
    .student-btn button:hover {
        background-color: #0d47a1;
        color: white;
        border-color: #002171;
        box-shadow: 0 6px 15px rgba(13, 71, 161, 0.4);
    }
    .teacher-btn button {
        background-color: #7B1FA2;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 22px;
        border: 2px solid #4a148c;
        width: 100%;
        box-shadow: 0 4px 10px rgba(123, 31, 162, 0.3);
        transition: 0.3s ease;
    }
    .teacher-btn button:hover {
        background-color: #4a148c;
        color: white;
        border-color: #311b92;
        box-shadow: 0 6px 15px rgba(74, 20, 140, 0.4);
    }
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 22px;
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
        padding: 35px 20px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(0, 77, 64, 0.4);
        border: 3px solid #80cbc4;
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
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #004d40;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .books-info-card h4 {
        color: #004d40;
        margin-top: 0;
        margin-bottom: 10px;
        font-size: 1.15rem;
    }
    .books-info-card ul {
        margin: 0;
        padding-left: 20px;
        color: #333333;
        font-size: 0.95rem;
        text-align: left;
    }
    .books-info-card li {
        margin-bottom: 5px;
    }
    .welcome-text-banner {
        text-align: center;
        font-weight: bold;
        color: #004d40;
        font-size: 1.2rem;
        background-color: #e0f2f1;
        padding: 12px;
        border-radius: 10px;
        border: 2px dashed #00897b;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# SESSION STATE INITIALIZATION
if "global_students" not in str_app.session_state:
    str_app.session_state.global_students = {}
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


def load_databases_for_grade(grade_str, gosa_str=""):
    grade_num = grade_str.replace("Kutaa ", "").strip()
    
    # Foldarii 'kit/' keessatti maqaan faayilii akka sirriitti wal simatu taasifameera
    ao_file = f"kit/ao_kutaa{grade_num}.json"
    math_file = f"kit/math_kutaa{grade_num}.json"
    eng_file = f"kit/eng_kutaa{grade_num}.json"

    def fetch_questions(filename, default_pool):
        if not os.path.exists(filename):
            return default_pool
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                elif isinstance(data, dict):
                    for key in ["questions", "data", "list"]:
                        if key in data and isinstance(data[key], list):
                            return data[key]
                return default_pool
        except (FileNotFoundError, json.JSONDecodeError):
            return default_pool
import random
import streamlit as st

st.set_page_config(
    page_title="Manni Barumsaa - Qormaata fi Gaaffiiwwan",
    page_icon="📚",
    layout="centered",
)

st.title("Manni Barumsaa - Qormaata fi Gaaffiiwwan")

# 1. KUUSAA GAAFFIIEWWAN KALLATTIIDHAAN KODII KEESSATTI QOPHEEFFAME (IN-MEMORY DATABASE)
DATABASE = {
    "Kutaa 1": {
        "Afaan Oromoo": [
            {
                "question": (
                    "Qubee Afaan Oromoo keessatti qubeen jalqabaa maali?"
                ),
                "options": ["A) A", "B) B", "C) C", "D) D"],
                "answer": "A",
                "type": "mcq",
            },
            {
                "question": "Jechi 'Nagaa' jedhu hiika akkamii qaba?",
                "options": ["A) Fayyaa", "B) Gadda", "C) Beela", "D) Loluu"],
                "answer": "A",
                "type": "mcq",
            },
        ],
        "Herrega (Math)": [
            {
                "question": "Kutaa 1 - Herrega: 2 + 3 hammami?",
                "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
                "answer": "B",
                "type": "mcq",
            }
        ],
        "English": [
            {
                "question": "What is the capital letter of 'a'?",
                "options": ["A) A", "B) B", "C) C", "D) D"],
                "answer": "A",
                "type": "mcq",
            }
        ],
    },
    "Kutaa 2": {
        "Afaan Oromoo": [
            {
                "question": "Aadaa Oromoo keessatti irreecha jechuun maali?",
                "options": [
                    "A) Ayyaana galateeffannaa",
                    "B) Lola",
                    "C) Beela",
                    "D) Hirriba",
                ],
                "answer": "A",
                "type": "mcq",
            }
        ],
        "Herrega (Math)": [
            {
                "question": "10 - 4 hammami?",
                "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
                "answer": "B",
                "type": "mcq",
            }
        ],
        "English": [
            {
                "question": "Choose the correct article: 'This is ___ apple.'",
                "options": ["A) a", "B) an", "C) the", "D) on"],
                "answer": "B",
                "type": "mcq",
            }
        ],
    },
    # Kutaa 3 hanga 6 asitti dabaluu dandeessa...
}

# Kutaa fi Gosa Barnootaa filachiisuu
col1, col2 = st.columns(2)

with col1:
    kutaa = st.selectbox(
        "Kutaa Filadhu:",
        [
            "Kutaa 1",
            "Kutaa 2",
            "Kutaa 3",
            "Kutaa 4",
            "Kutaa 5",
            "Kutaa 6",
        ],
    )

with col2:
    gosa = st.selectbox(
        "Gosa Barnootaa:", ["Afaan Oromoo", "Herrega (Math)", "English"]
    )


# Gaaffilee DATABASE keessaa kutaa fi gosa filatameen baasuu
def load_questions_from_memory(selected_kutaa, selected_gosa):
    if (
        selected_kutaa in DATABASE
        and selected_gosa in DATABASE[selected_kutaa]
    ):
        return DATABASE[selected_kutaa][selected_gosa]
    return []  # Yoo gaaffiin hin jirre faayilii duwwaa deebisa


questions = load_questions_from_memory(kutata := kutaa, gosa)

if not questions:
    st.warning(
        f"Gaaffiin {kutaa} fi {gosa}af qophaa'e ammayyuu kuusaa keessatti hin"
        " jiru. Maaloo itti dabali."
    )
else:
    # Session state qopheessuu gaaffii jijjiiruuf
    session_key = f"{kutaa}_{gosa}"
    if (
        "current_session_key" not in st.session_state
        or st.session_state.current_session_key != session_key
    ):
        st.session_state.current_session_key = session_key
        st.session_state.current_q = random.choice(questions)
        st.session_state.show_answer = False

    q = st.session_state.current_q

    st.divider()
    st.subheader(f"Qormaata: {gosa} ({kutaa})")

    if "text" in q and q["text"]:
        st.info(q["text"])

    question_text = q.get("question") or q.get("text")
    st.write(f"**{question_text}**")

    user_answer = None

    if q.get("type") == "mcq" and "options" in q:
        user_answer = st.radio(
            "Filannoo kee filadhu:", q["options"], key=f"mcq_{session_key}"
        )

    if st.button("Deebii Ilaali"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        if q.get("type") == "mcq":
            correct = q.get("answer")
            if user_answer and user_answer.startswith(correct):
                st.success(f"Sirriidha! Deebiin: {correct}")
            else:
                st.error(f"Dogoggora. Deebiin sirrii: {correct}")

    if st.button("Gaaffii Biraa Fiduu"):
        st.session_state.current_q = random.choice(questions)
        st.session_state.show_answer = False
        st.rerun()

def role_selection_screen():
    str_app.markdown(
        """
        <div class="hero-box">
            <h1>📖 Hiika Way (HW) APP</h1>
            <p>
                Baga Nagaan Gara App Dandeettii Dubbisuu, Barreessuu Fi Shallaguu Barattootaa Adda Baasu "Hika Way" Kitesa Negasa tiin kalaqameetti Nagaan Dhuftan!
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    str_app.markdown(
        """
        <div class="books-info-card">
            <h4>📚 Qabiyyee Kitaabota madaallii (Kutaa 1 - 6):</h4>
            <ul>
                <li><b>Kutaa 1 & 2:</b> Qubee bu'uuraa, jechoota gaggabaaboo fi herrega lakkoofsaa jalqabaa.</li>
                <li><b>Kutaa 3 & 4:</b> Dubbisa hubachuu, jechoota hiika isaanii waliin, fi shallaggaa walxaxaa hin taane.</li>
                <li><b>Kutaa 5 & 6:</b> Gaaffilee hubannoo dubbisaa bal'aa, caqasa, fi rakkoolee herregaa fi ingliffaa olaanoo.</li>
            </ul>
        </div>
        <div class="welcome-text-banner">
            🙌 WELCOME TO HIKA WAY APP
        </div>
    """,
        unsafe_allow_html=True,
    )

    str_app.markdown(
        "<h3 style='text-align: center; color: #004d40; margin-top: 15px; margin-bottom: 15px;'>🔑 Furtuu Filadhu:</h3>",
        unsafe_allow_html=True,
    )

    col1, col2 = str_app.columns(2)
    with col1:
        str_app.markdown(
            "<p style='text-align: center; color: #1976D2; font-weight: bold; font-size: 1.1rem; background-color: #E3F2FD; padding: 6px; border-radius: 8px;'>👤 Barataa (Student)</p>",
            unsafe_allow_html=True,
        )
        str_app.markdown('<div class="student-btn">', unsafe_allow_html=True)
        if str_app.button("🔑 Seeni (Barataa)", key="student_btn"):
            str_app.session_state.current_page = "name_input"
            str_app.rerun()
        str_app.markdown("</div>", unsafe_allow_html=True)

    with col2:
        str_app.markdown(
            "<p style='text-align: center; color: #7B1FA2; font-weight: bold; font-size: 1.1rem; background-color: #F3E5F5; padding: 6px; border-radius: 8px;'>🎓 Barsiisaa (Teacher)</p>",
            unsafe_allow_html=True,
        )
        str_app.markdown('<div class="teacher-btn">', unsafe_allow_html=True)
        if str_app.button("📊 Gabaasa Barsiisaa", key="teacher_btn"):
            str_app.session_state.current_page = "teacher_dashboard"
            str_app.rerun()
        str_app.markdown("</div>", unsafe_allow_html=True)


def name_input_screen():
    str_app.markdown(
        """
        <div class="hero-box">
            <h2>Galmee Maqaa & Kutaa Barataa</h2>
            <p>Maaloo maqaa kee guutuu fi kutaa kee filadhu</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    name = str_app.text_input("Maqaa Kee", placeholder="Maqaa kee guutuu barreessi...")
    grade = str_app.selectbox(
        "Kutaa Barumsaa (Grade 1 - 6)",
        ["Kutaa 1", "Kutaa 2", "Kutaa 3", "Kutaa 4", "Kutaa 5", "Kutaa 6"],
    )

    col1, col2 = str_app.columns(2)
    with col1:
        if str_app.button("Gara Appiitti Darbi"):
            if name.strip():
                clean_name = name.strip()
                str_app.session_state.current_student = clean_name
                str_app.session_state.current_grade = grade

                if clean_name not in str_app.session_state.global_students:
                    str_app.session_state.global_students[clean_name] = {
                        "grade": grade,
                        "afaanOromoo": 0,
                        "math": 0,
                        "english": 0,
                    }

                selected_qs = load_databases_for_grade(grade)
                str_app.session_state.student_random_questions[clean_name] = selected_qs

                str_app.session_state.current_page = "home"
                str_app.rerun()
            else:
                str_app.warning("Mee dura maqaa kee barreessi!")
    with col2:
        if str_app.button("⬅️ Duubatti"):
            str_app.session_state.current_page = "role_selection"
            str_app.rerun()


def home_screen():
    str_app.markdown(
        f"""
        <div class="hero-box">
            <h2>Baga nagaan dhuftte, {str_app.session_state.current_student} ({str_app.session_state.current_grade})!</h2>
            <p>Gosa barnootaa barachuu barbaaddu filadhu (Gosa tokkoon tokkoon isaaniif Gaaffii 6 qaba)</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if str_app.button("📖 Afaan Oromoo (Dubbisuu, Qubee, Jechoota, Hiika & Caqasa)"):
        str_app.session_state.current_page = "afaan_oromoo"
        str_app.rerun()

    str_app.write("")
    if str_app.button("🔢 Herrega - Mathematics (Shallaggaa fi Rakkoo Hiikuu)"):
        str_app.session_state.current_page = "math"
        str_app.rerun()

    str_app.write("")
    if str_app.button("🔤 Ingliffaa - English (Reading, Grammar & Vocabulary)"):
        str_app.session_state.current_page = "english"
        str_app.rerun()

    str_app.markdown("---")
    if str_app.button("⬅️ Ba'uu / Maqaa Jijjiiruu"):
        str_app.session_state.current_student = ""
        str_app.session_state.current_page = "role_selection"
        str_app.rerun()


def afaan_oromoo_screen():
    student = str_app.session_state.current_student
    questions = str_app.session_state.student_random_questions.get(student, {}).get("afaan_oromoo", [])

    str_app.subheader(f"Afaan Oromoo - {str_app.session_state.current_grade} ({student})")

    if not questions:
        str_app.warning("Gaaffiin Afaan Oromoo faayilii kana keessatti hin argamne ykn faayiliin hin jiru.")
        if str_app.button("🏠 Gara Manayeessaa"):
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    if "ao_index" not in str_app.session_state:
        str_app.session_state.ao_index = 0
        str_app.session_state.ao_score = 0

    idx = str_app.session_state.ao_index
    if idx >= len(questions):
        str_app.success("Gaaffiin Afaan Oromoo xumurameera! Gara manayeessaatti deebi'aa.")
        if str_app.button("🏠 Gara Manayeessaa"):
            str_app.session_state.ao_index = 0
            str_app.session_state.ao_score = 0
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    q = questions[idx]
    str_app.progress((idx + 1) / len(questions))
    c1, c2 = str_app.columns([3, 1])
    c1.markdown(f"**Gaaffii {idx + 1} / {len(questions)}**")
    c2.markdown(f"**Qabxii: {str_app.session_state.ao_score}**")

    passage_text = q.get("paragraph", q.get("text", ""))
    if passage_text and len(passage_text.strip()) > 0 and passage_text != q.get("question", ""):
        str_app.markdown(
            f"""
            <div style="background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
                <b>📚 Qajeelfama / Dubbisa:</b><br>{passage_text}
            </div>
        """,
            unsafe_allow_html=True,
        )

    str_app.markdown(f"### {q.get('question', '')}")
    user_answer = None
    if q.get("type", "mcq") == "mcq" and "options" in q:
        user_answer = str_app.radio(
            "Filannoo kee filadhu:", q["options"], key=f"ao_radio_{student}_{idx}"
        )
    else:
        user_answer = str_app.text_input("Deebii kee asitti barreessi:", key=f"ao_ans_{student}_{idx}")

    attempt_key = ("afaan_oromoo", student, idx)
    if attempt_key not in str_app.session_state.attempts:
        str_app.session_state.attempts[attempt_key] = 0

    current_attempts = str_app.session_state.attempts[attempt_key]
    str_app.write(f"⚠️ Carraa deebii yaaluu: **{current_attempts} / 3**")

    if str_app.button("Mirkaneessi Afaan Oromoo"):
        if current_attempts < 3:
            str_app.session_state.attempts[attempt_key] += 1
            is_correct = False

            if "answer" in q:
                correct = str(q["answer"])
                if user_answer and (user_answer.strip().upper() == correct.upper() or user_answer.strip().startswith(correct)):
                    is_correct = True
            elif "expected" in q:
                if user_answer and any(exp.lower() in user_answer.strip().lower() for exp in q["expected"]):
                    is_correct = True

            if is_correct:
                str_app.session_state.ao_score += 5
                str_app.success("🎉 Sirriidha!")
                str_app.session_state.attempts[attempt_key] = 3
            else:
                rem = 3 - str_app.session_state.attempts[attempt_key]
                if rem > 0:
                    str_app.warning(f"❌ Dogoggora! Carraan hafe: {rem}")
                else:
                    str_app.error(f"❌ Carraan 3ffaan xumurameera. Deebiin sirrii: {q.get('answer', '')}")
        else:
            str_app.info("Barataan carraa 3 guutee xumureera.")

    str_app.markdown("---")
    b1, b2 = str_app.columns(2)
    with b1:
        if idx > 0 and str_app.button("⬅️ Duubatti (Previous)", key="ao_prev"):
            str_app.session_state.ao_index -= 1
            str_app.rerun()
    with b2:
        if idx < len(questions) - 1:
            if str_app.button("Fuuldharatti (Next) ➡️", key="ao_next"):
                str_app.session_state.ao_index += 1
                str_app.rerun()
        else:
            if str_app.button("Xumuruu & Galchuu", key="ao_finish"):
                str_app.session_state.global_students[student]["afaanOromoo"] = str_app.session_state.ao_score
                str_app.success("Qabxiin Afaan Oromoo guutuu galmeeffameera!")
                str_app.session_state.ao_index = 0
                str_app.session_state.ao_score = 0
                str_app.session_state.current_page = "home"
                str_app.rerun()


def math_screen():
    student = str_app.session_state.current_student
    questions = str_app.session_state.student_random_questions.get(student, {}).get("math", [])

    str_app.subheader(f"Herrega - {str_app.session_state.current_grade} ({student})")

    if not questions:
        str_app.warning("Gaaffiin Herregaa faayilii kana keessatti hin argamne ykn faayiliin hin jiru.")
        if str_app.button("🏠 Gara Manayeessaa"):
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    if "m_index" not in str_app.session_state:
        str_app.session_state.m_index = 0
        str_app.session_state.m_score = 0

    idx = str_app.session_state.m_index
    if idx >= len(questions):
        str_app.success("Gaaffiin Herregaa xumurameera! Gara manayeessaatti deebi'aa.")
        if str_app.button("🏠 Gara Manayeessaa"):
            str_app.session_state.m_index = 0
            str_app.session_state.m_score = 0
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    q = questions[idx]
    str_app.progress((idx + 1) / len(questions))
    c1, c2 = str_app.columns([3, 1])
    c1.markdown(f"**Gaaffii Herregaa: {idx + 1} / {len(questions)}**")
    c2.markdown(f"**Qabxii: {str_app.session_state.m_score}**")

    passage_text = q.get("paragraph", q.get("text", ""))
    if passage_text and len(passage_text.strip()) > 0 and passage_text != q.get("question", ""):
        str_app.markdown(
            f"""
            <div style="background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
                <b>📚 Qajeelfama / Hubachiisa:</b><br>{passage_text}
            </div>
        """,
            unsafe_allow_html=True,
        )

    str_app.markdown(f"### {q.get('question', '')}")
    user_answer = None
    if q.get("type", "mcq") == "mcq" and "options" in q:
        user_answer = str_app.radio(
            "Filannoo kee filadhu:", q["options"], key=f"m_radio_{student}_{idx}"
        )
    else:
        user_answer = str_app.text_input("Deebii kee asitti barreessi:", key=f"m_ans_{student}_{idx}")

    attempt_key = ("math", student, idx)
    if attempt_key not in str_app.session_state.attempts:
        str_app.session_state.attempts[attempt_key] = 0

    current_attempts = str_app.session_state.attempts[attempt_key]
    str_app.write(f"⚠️ Carraa deebii yaaluu: **{current_attempts} / 3**")

    if str_app.button("Mirkaneessi Herregaa"):
        if current_attempts < 3:
            str_app.session_state.attempts[attempt_key] += 1
            is_correct = False
            correct_ans = str(q.get("answer", "")).upper()

            if user_answer:
                cleaned_ans = user_answer.strip().upper()
                if cleaned_ans == correct_ans or (correct_ans and cleaned_ans.startswith(correct_ans[0])):
                    is_correct = True

            if is_correct:
                str_app.session_state.m_score += 5
                str_app.success("🎉 Sirriidha!")
                str_app.session_state.attempts[attempt_key] = 3
            else:
                rem = 3 - str_app.session_state.attempts[attempt_key]
                if rem > 0:
                    str_app.warning(f"❌ Dogoggora qaba! Carraan hafe: {rem}")
                else:
                    str_app.error(f"❌ Carraan xumurameera. Deebiin sirrii: {q.get('answer', '')}")
        else:
            str_app.info("Barataan carraa 3 guutee xumureera.")

    str_app.markdown("---")
    b1, b2 = str_app.columns(2)
    with b1:
        if idx > 0 and str_app.button("⬅️ Duubatti (Previous)", key="m_prev"):
            str_app.session_state.m_index -= 1
            str_app.rerun()
    with b2:
        if idx < len(questions) - 1:
            if str_app.button("Fuuldharatti (Next) ➡️", key="m_next"):
                str_app.session_state.m_index += 1
                str_app.rerun()
        else:
            if str_app.button("Xumuruu & Deebi'i", key="m_finish"):
                str_app.session_state.global_students[student]["math"] = str_app.session_state.m_score
                str_app.success(f"Galatoomi! Qabxii Herregaa: {str_app.session_state.m_score}")
                str_app.session_state.m_index = 0
                str_app.session_state.m_score = 0
                str_app.session_state.current_page = "home"
                str_app.rerun()


def english_screen():
    student = str_app.session_state.current_student
    questions = str_app.session_state.student_random_questions.get(student, {}).get("english", [])

    str_app.subheader(f"English - {str_app.session_state.current_grade} ({student})")

    if not questions:
        str_app.warning("English questions not found or file is missing.")
        if str_app.button("🏠 Home"):
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    if "e_index" not in str_app.session_state:
        str_app.session_state.e_index = 0
        str_app.session_state.e_score = 0

    idx = str_app.session_state.e_index
    if idx >= len(questions):
        str_app.success("English questions completed! Return to home.")
        if str_app.button("🏠 Home"):
            str_app.session_state.e_index = 0
            str_app.session_state.e_score = 0
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    q = questions[idx]
    str_app.progress((idx + 1) / len(questions))
    c1, c2 = str_app.columns([3, 1])
    c1.markdown(f"**Question {idx + 1} / {len(questions)}**")
    c2.markdown(f"**Score: {str_app.session_state.e_score}**")

    passage_text = q.get("paragraph", q.get("text", ""))
    if passage_text and len(passage_text.strip()) > 0 and passage_text != q.get("question", ""):
        str_app.markdown(
            f"""
            <div style="background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
                <b>📚 Reading Passage / Context:</b><br>{passage_text}
            </div>
        """,
            unsafe_allow_html=True,
        )

    str_app.markdown(f"### {q.get('question', '')}")
    user_answer = None
    if q.get("type", "mcq") == "mcq" and "options" in q:
        user_answer = str_app.radio(
            "Choose your option:", q["options"], key=f"e_radio_{student}_{idx}"
        )
    else:
        user_answer = str_app.text_input("Type your answer here:", key=f"e_ans_{student}_{idx}")

    attempt_key = ("english", student, idx)
    if attempt_key not in str_app.session_state.attempts:
        str_app.session_state.attempts[attempt_key] = 0

    current_attempts = str_app.session_state.attempts[attempt_key]
    str_app.write(f"⚠️ Attempt count: **{current_attempts} / 3**")

    if str_app.button("Check Answer"):
        if current_attempts < 3:
            str_app.session_state.attempts[attempt_key] += 1
            is_correct = False

            if "answer" in q:
                ans_str = str(q["answer"]).lower()
                if user_answer:
                    cleaned_ans = user_answer.strip().lower()
                    if cleaned_ans == ans_str or cleaned_ans.startswith(ans_str[0]):
                        is_correct = True
            elif "expected" in q:
                if user_answer and any(exp.lower() in user_answer.strip().lower() for exp in q["expected"]):
                    is_correct = True

            if is_correct:
                str_app.session_state.e_score += 5
                str_app.success("🎉 Correct!")
                str_app.session_state.attempts[attempt_key] = 3
            else:
                rem = 3 - str_app.session_state.attempts[attempt_key]
                if rem > 0:
                    str_app.warning(f"❌ Incorrect! Remaining attempts: {rem}")
                else:
                    ans_text = q.get("answer", q.get("expected", [""])[0])
                    str_app.error(f"❌ Maximum attempts reached. Correct answer: {ans_text}")
        else:
            str_app.info("Maximum attempts completed for this question.")

    str_app.markdown("---")
    b1, b2 = str_app.columns(2)
    with b1:
        if idx > 0 and str_app.button("⬅️ Duubatti (Previous)", key="e_prev"):
            str_app.session_state.e_index -= 1
            str_app.rerun()
    with b2:
        if idx < len(questions) - 1:
            if str_app.button("Fuuldharatti (Next) ➡️", key="e_next"):
                str_app.session_state.e_index += 1
                str_app.rerun()
        else:
            if str_app.button("Finish & Return", key="e_finish"):
                str_app.session_state.global_students[student]["english"] = str_app.session_state.e_score
                str_app.success(f"Well done! Total English Score: {str_app.session_state.e_score}")
                str_app.session_state.e_index = 0
                str_app.session_state.e_score = 0
                str_app.session_state.current_page = "home"
                str_app.rerun()


def teacher_dashboard_screen():
    str_app.subheader("🎓 Gabaasa Barsiisaa - Kutaa Barsiisaa (Teacher Report)")
    str_app.markdown("**Qabxii Barattootaa, Parsantii (%) fi Cuunfaa Gabaasaa**")

    students = str_app.session_state.global_students
    str_app.write(f"**Baay'inni barattoota galmaa'an:** {len(students)}")

    if not students:
        str_app.info("Ammaaf barataan galmaa'e hin jiru.")
    else:
        max_total_score = 90  # Gaaffii 6 x 5 (Gosa tokkoof qabxii 30, gosa 3 waliigala 90)
        table_data = []
        csv_data = "Maqaa Barataa,Kutaa,Afaan Oromoo,Herrega,Ingliffaa,Waliigala,Parsantii (%),Cuunfaa\n"

        for name, data in students.items():
            ao = data["afaanOromoo"]
            math = data["math"]
            eng = data["english"]
            total = ao + math + eng
            percentage = (total / max_total_score) * 100

            table_data.append({
                "Maqaa Barataa": name,
                "Kutaa": data["grade"],
                "Afaan Oromoo": f"{ao}/30",
                "Herrega": f"{math}/30",
                "Ingliffaa": f"{eng}/30",
                "Waliigala": f"{total}/90",
                "Parsantii (%)": f"{percentage:.1f}%",
            })

            csv_data += f"{name},{data['grade']},{ao},{math},{eng},{total},{percentage:.1f}%\n"

        str_app.dataframe(table_data, use_container_width=True)
        str_app.download_button(
            label="📥 Download Excel Report (CSV)",
            data=csv_data,
            file_name="HiikaWay_Student_Report.csv",
            mime="text/csv",
        )

    str_app.write("")
    if str_app.button("⬅️ Gara Furtuu Hojii Deebi'i"):
        str_app.session_state.current_page = "role_selection"
        str_app.rerun()


# ROUTE CONTROLLER
if str_app.session_state.current_page == "role_selection":
    role_selection_screen()
elif str_app.session_state.current_page == "name_input":
    name_input_screen()
elif str_app.session_state.current_page == "home":
    home_screen()
elif str_app.session_state.current_page == "afaan_oromoo":
    afaan_oromoo_screen()
elif str_app.session_state.current_page == "math":
    math_screen()
elif str_app.session_state.current_page == "english":
    english_screen()
elif str_app.session_state.current_page == "teacher_dashboard":
    teacher_dashboard_screen()
