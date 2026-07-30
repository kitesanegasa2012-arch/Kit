import random
import streamlit as str_app

# PAGE CONFIGURATION
str_app.set_page_config(
    page_title="Hiika Way (HW) App", page_icon="📖", layout="centered"
)

# CUSTOM STYLING (Background, Border, and Cover Page UI Enhancements)
str_app.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f4fbf7 0%, #e2f2e6 100%);
    }
    
    /* Student Button: Blue */
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

    /* Teacher Button: Purple */
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

    /* General Button Styling fallback */
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
    </style>
""",
    unsafe_allow_html=True,
)

# KUUSAA GAFFIILEE 200 (MASTER DATABASE FOLDERS)
# Folder 1: Afaan Oromoo (Gaaffilee bal'aa kuusaa 200 irraa filataman)
MASTER_AO_DB = {
    "Kutaa 6": [
        {
            "type": "reading",
            "title": "Dubbisa 1: Hojii Gamtaa",
            "text": (
                "Hojjiin gamtaa milkaa'ina fida. Namoonni waliin hojjetan rakkoo"
                " salphaatti injifatu."
            ),
            "question": "Gaaffii Dubbisaa: Hojjiin gamtaa maal fida?",
            "expected": ["milkaa'ina", "milkaa ina", "injifannoo"],
        },
        {
            "type": "mcq",
            "title": "Qeeqqa Barruu 2",
            "text": "Barruu keessatti 'Milkaa'ina' jechuun hiika maal qaba?",
            "options": ["A) Kufaatii", "B) Galma ga'uu", "C) Daddaffii", "D) Boqonnaa"],
            "answer": "B",
        },
        {
            "type": "mcq",
            "title": "Qeeqqa Barruu 3",
            "text": "Mammaaksi 'Tokkummaan humna' jedhu maal barsiisa?",
            "options": [
                "A) Kophaa hojjechuu",
                "B) Waliin dhaabbachuu",
                "C) Lafa qabachuu",
                "D) Dhibbaa",
            ],
            "answer": "B",
        },
        {
            "type": "mcq",
            "title": "Qeeqqa Barruu 4",
            "text": "Jechi 'Cicha' jedhu hiika kam qaba?",
            "options": [
                "A) Dadhabuu",
                "B) Mirkaneeffannoo jabaa",
                "C) Lafa lakkisuu",
                "D) Fiigicha",
            ],
            "answer": "B",
        },
    ]
}

# Folder 2: Herrega (Mathematics Master Database)
MASTER_MATH_DB = {
    "Kutaa 6": [
        {
            "question": "L.C.M of 6 and 8 = ?",
            "options": ["A) 24", "B) 48", "C) 12", "D) 18"],
            "answer": "24",
        },
        {
            "question": (
                "Hangi oowwii 20% dabaluun 60 ta'e, jalqaba hammami ture?"
            ),
            "options": ["A) 50", "B) 48", "C) 55", "D) 45"],
            "answer": "50",
        },
        {
            "question": "15 × 4 - 10 = ?",
            "options": ["A) 50", "B) 60", "C) 40", "D) 30"],
            "answer": "50",
        },
        {
            "question": "Haftee (Remainder) 45 ukka 7tti yeroo hiramu meeqa?",
            "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
            "answer": "3",
        },
    ]
}

# Folder 3: Ingliffaa (English Master Database)
MASTER_ENG_DB = {
    "Kutaa 6": [
        {
            "type": "reading",
            "title": "Reading 1: Scientific Research",
            "text": (
                "Researchers analyze data, study patterns, and draw valid"
                " conclusions based on empirical evidence."
            ),
            "question": "Question: What do researchers analyze?",
            "expected": ["data", "empirical evidence"],
        },
        {
            "type": "mcq",
            "title": "Advanced Grammar 2",
            "text": (
                "Choose the correct passive voice: 'She writes a letter.'"
            ),
            "options": [
                "A) A letter is written by her.",
                "B) A letter was written.",
                "C) She wrote a letter.",
                "D) Letter is write.",
            ],
            "answer": "A",
        },
        {
            "type": "mcq",
            "title": "Vocabulary 3",
            "text": "What is the synonym of 'rapid'?",
            "options": ["A) Slow", "B) Fast", "C) Heavy", "D) Small"],
            "answer": "B",
        },
        {
            "type": "mcq",
            "title": "Grammar 4",
            "text": "Choose the correct preposition: 'He is good ______ math.'",
            "options": ["A) at", "B) in", "C) on", "D) with"],
            "answer": "A",
        },
    ]
}


# Session State Management
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

# Store randomized 2 questions per student session to solve the class size & testing issue
if "student_random_questions" not in str_app.session_state:
  str_app.session_state.student_random_questions = {}


# ==========================================
# 1. ROLE SELECTION SCREEN (COVER PAGE)
# ==========================================
def role_selection_screen():
  str_app.markdown(
      """
        <div class="hero-box">
            <h1>📖 Hiika Way (HW) APP</h1>
            <p>
                Baga Nagaan Gara App Dandeettii Dubbisuu, Barreessuu Fi Shallaguu Barattootaa Adda Baasu Hiika Way itti Nagaan Dhuftan!<br><br>
                <b>App kanaaf: Kutaa 1 - Kutaa 6 (Afaan Oromoo, Herrega, Ingliffaa)</b><br>
                <b>Created by Kitesa Negasa Feyisa</b>
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # Cover page styling adjustments: Reduced image width & light colored background
  _, img_col, _ = str_app.columns([1, 1.5, 1])
  with img_col:
    str_app.image(
        "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=600&q=80",
        use_container_width=True,
    )

  str_app.markdown(
      "<h3 style='text-align: center; color: #004d40; margin-top: 15px;"
      " margin-bottom: 15px;'>🔑 Furtuu Filadhu:</h3>",
      unsafe_allow_html=True,
  )

  col1, col2 = str_app.columns(2)
  with col1:
    str_app.markdown(
        "<p style='text-align: center; color: #1976D2; font-weight: bold;"
        " font-size: 1.1rem; background-color: #E3F2FD; padding: 6px;"
        " border-radius: 8px;'>👤 Barataa (Student)</p>",
        unsafe_allow_html=True,
    )
    str_app.markdown('<div class="student-btn">', unsafe_allow_html=True)
    if str_app.button("🔑 Seeni (Barataa)", key="student_btn"):
      str_app.session_state.current_page = "name_input"
      str_app.rerun()
    str_app.markdown("</div>", unsafe_allow_html=True)

  with col2:
    str_app.markdown(
        "<p style='text-align: center; color: #7B1FA2; font-weight: bold;"
        " font-size: 1.1rem; background-color: #F3E5F5; padding: 6px;"
        " border-radius: 8px;'>🎓 Barsiisaa (Teacher)</p>",
        unsafe_allow_html=True,
    )
    str_app.markdown('<div class="teacher-btn">', unsafe_allow_html=True)
    if str_app.button("📊 Gabaasa Barsiisaa", key="teacher_btn"):
      str_app.session_state.current_page = "teacher_dashboard"
      str_app.rerun()
    str_app.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 2. NAME & GRADE INPUT SCREEN
# ==========================================
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

  name = str_app.text_input(
      "Maqaa Kee", placeholder="Maqaa kee guutuu barreessi..."
  )
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

        # RANDOMIZATION LOGIC: Pick 2 random questions for this student from Master Folders
        ao_pool = MASTER_AO_DB.get(grade, MASTER_AO_DB["Kutaa 6"])
        math_pool = MASTER_MATH_DB.get(grade, MASTER_MATH_DB["Kutaa 6"])
        eng_pool = MASTER_ENG_DB.get(grade, MASTER_ENG_DB["Kutaa 6"])

        str_app.session_state.student_random_questions[clean_name] = {
            "afaan_oromoo": random.sample(
                ao_pool, min(2, len(ao_pool))
            ),  # Gaaffii 2 qofa
            "math": random.sample(
                math_pool, min(2, len(math_pool))
            ),  # Gaaffii 2 qofa
            "english": random.sample(
                eng_pool, min(2, len(eng_pool))
            ),  # Gaaffii 2 qofa
        }

        str_app.session_state.current_page = "home"
        str_app.rerun()
      else:
        str_app.warning("Mee dura maqaa kee barreessi!")
  with col2:
    if str_app.button("⬅️ Duubatti"):
      str_app.session_state.current_page = "role_selection"
      str_app.rerun()


# ==========================================
# 3. HOME SCREEN (3 GOSA BARNOOTAA)
# ==========================================
def home_screen():
  str_app.markdown(
      f"""
        <div class="hero-box">
            <h2>Baga nagaan dhuftte, {str_app.session_state.current_student} ({str_app.session_state.current_grade})!</h2>
            <p>Gosa barnootaa barachuu barbaaddu filadhu (Gaaffiiwwan kuusaa keessaa carraan siif filataman)</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  if str_app.button(
      "📖 Afaan Oromoo (Dubbisuu, Qubee, Jechoota, Hiika & Caqasa)"
  ):
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


# ==========================================
# 4. AFAAN OROMOO MODULE (Random 2 Questions)
# ==========================================
def afaan_oromoo_screen():
  student = str_app.session_state.current_student
  questions = str_app.session_state.student_random_questions.get(
      student, {}
  ).get("afaan_oromoo", [])

  str_app.subheader(
      f"Afaan Oromoo - {str_app.session_state.current_grade} ({student})"
  )

  if "ao_index" not in str_app.session_state:
    str_app.session_state.ao_index = 0
    str_app.session_state.ao_score = 0

  idx = str_app.session_state.ao_index
  if not questions or idx >= len(questions):
    str_app.success(
        "Gaaffiin Afaan Oromoo xumurameera! Gara manayeessaatti deebi'aa."
    )
    if str_app.button("🏠 Gara Manayeessaa"):
      str_app.session_state.ao_index = 0
      str_app.session_state.ao_score = 0
      str_app.session_state.current_page = "home"
      str_app.rerun()
    return

  q = questions[idx]

  str_app.progress((idx + 1) / len(questions))
  c1, c2 = str_app.columns([3, 1])
  c1.markdown(
      f"**Gaaffii {idx + 1} / {len(questions)} (Folder 200 keessaa):"
      f" {q['title']}**"
  )
  c2.markdown(f"**Qabxii: {str_app.session_state.ao_score}**")

  if q["type"] == "reading" and "text" in q:
    str_app.markdown(
        f"""
            <div style="background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
                <b>📚 Qajeelfama Dubbisuu:</b><br>{q['text']}
            </div>
        """,
        unsafe_allow_html=True,
    )

  str_app.markdown(f"### {q.get('question', q.get('text'))}")

  if "options" in q:
    for opt in q["options"]:
      str_app.write(opt)

  attempt_key = ("afaan_oromoo", student, idx)
  if attempt_key not in str_app.session_state.attempts:
    str_app.session_state.attempts[attempt_key] = 0

  current_attempts = str_app.session_state.attempts[attempt_key]
  str_app.write(
      f"⚠️ Carraa deebii yaaluu: **{current_attempts} / 3** (Carraan 3ffaan"
      " ni kuusama)"
  )

  ans = str_app.text_input(
      "Deebii kee asitti barreessi:", key=f"ao_ans_{student}_{idx}"
  )

  if str_app.button("Mirkaneessi Afaan Oromoo"):
    if current_attempts < 3:
      str_app.session_state.attempts[attempt_key] += 1
      is_correct = False

      if "answer" in q:
        if (
            ans.strip().upper() == q["answer"]
            or ans.strip().lower() == q["answer"].lower()
        ):
          is_correct = True
      elif "expected" in q:
        if any(exp in ans.strip().lower() for exp in q["expected"]):
          is_correct = True

      if is_correct:
        str_app.session_state.ao_score += 10
        str_app.success("🎉 Sirriitti deebiste, Foyyee qabda, Si hafa!")
        str_app.session_state.attempts[attempt_key] = 3
      else:
        rem = 3 - str_app.session_state.attempts[attempt_key]
        if rem > 0:
          str_app.warning(
              f"❌ Dogoggora! Ammas yaali. Carraan hafe: {rem}"
          )
        else:
          str_app.error("❌ Carraan 3ffaan xumurameera.")
    else:
      str_app.info("Barataan carraa 3 guutee xumureera.")

  str_app.markdown("---")
  b1, b2 = str_app.columns(2)
  with b1:
    if idx > 0 and str_app.button("⬅️ Duubatti (Previous)"):
      str_app.session_state.ao_index -= 1
      str_app.rerun()
  with b2:
    if idx < len(questions) - 1:
      if str_app.button("Fuuldharatti (Next) ➡️"):
        str_app.session_state.ao_index += 1
        str_app.rerun()
    else:
      if str_app.button("Xumuruu & Galchuu"):
        str_app.session_state.global_students[student]["afaanOromoo"] = (
            str_app.session_state.ao_score
        )
        str_app.success("Qabxiin Afaan Oromoo guutuu galmeeffameera!")
        str_app.session_state.ao_index = 0
        str_app.session_state.ao_score = 0
        str_app.session_state.current_page = "home"
        str_app.rerun()


# ==========================================
# 5. MATH MODULE (Random 2 Questions)
# ==========================================
def math_screen():
  student = str_app.session_state.current_student
  questions = str_app.session_state.student_random_questions.get(
      student, {}
  ).get("math", [])

  str_app.subheader(
      f"Herrega - {str_app.session_state.current_grade} ({student})"
  )

  if "m_index" not in str_app.session_state:
    str_app.session_state.m_index = 0
    str_app.session_state.m_score = 0

  idx = str_app.session_state.m_index
  if not questions or idx >= len(questions):
    str_app.success("Gaaffiin Herregaa xumurameera! Gara manayeessaatti deebi'aa.")
    if str_app.button("🏠 Gara Manayeessaa"):
      str_app.session_state.m_index = 0
      str_app.session_state.m_score = 0
      str_app.session_state.current_page = "home"
      str_app.rerun()
    return

  q = questions[idx]

  c1, c2 = str_app.columns([3, 1])
  c1.markdown(f"**Gaaffii Herregaa: {idx + 1} / {len(questions)}**")
  c2.markdown(f"**Qabxii: {str_app.session_state.m_score}**")

  str_app.markdown(f"### {q['question']}")
  for opt in q["options"]:
    str_app.write(opt)

  attempt_key = ("math", student, idx)
  if attempt_key not in str_app.session_state.attempts:
    str_app.session_state.attempts[attempt_key] = 0

  current_attempts = str_app.session_state.attempts[attempt_key]
  str_app.write(
      f"⚠️ Carraa deebii yaaluu: **{current_attempts} / 3** (Carraan 3ffaan"
      " ni kuusama)"
  )

  m_ans = str_app.text_input(
      "Deebii kee asitti barreessi (Fkn: 24 ykn A):", key=f"m_ans_{student}_{idx}"
  )

  if str_app.button("Mirkaneessi Herregaa"):
    if current_attempts < 3:
      str_app.session_state.attempts[attempt_key] += 1
      is_correct = False
      cleaned_ans = m_ans.strip().upper()

      if cleaned_ans == q["answer"].upper() or cleaned_ans == q["answer"][0]:
        is_correct = True

      if is_correct:
        str_app.session_state.m_score += 10
        str_app.success("🎉 Sirriitti deebiste, Foyyee qabda, Si hafa!")
        str_app.session_state.attempts[attempt_key] = 3
      else:
        rem = 3 - str_app.session_state.attempts[attempt_key]
        if rem > 0:
          str_app.warning(f"❌ Dogoggora qaba! Carraan hafe: {rem}")
        else:
          str_app.error(
              f"❌ Carraan 3ffaan xumurameera. Deebiin sirrii: {q['answer']}"
          )
    else:
      str_app.info("Barataan carraa 3 guutee xumureera.")

  str_app.markdown("---")
  b1, b2 = str_app.columns(2)
  with b1:
    if idx > 0 and str_app.button("⬅️ Duubatti (Previous)"):
      str_app.session_state.m_index -= 1
      str_app.rerun()
  with b2:
    if idx < len(questions) - 1:
      if str_app.button("Fuuldharatti (Next) ➡️"):
        str_app.session_state.m_index += 1
        str_app.rerun()
    else:
      if str_app.button("Xumuruu & Deebi'i"):
        str_app.session_state.global_students[student]["math"] = (
            str_app.session_state.m_score
        )
        str_app.success(
            f"Galatoomi! Qabxii Herregaa waliigalaa: {str_app.session_state.m_score}"
        )
        str_app.session_state.m_index = 0
        str_app.session_state.m_score = 0
        str_app.session_state.current_page = "home"
        str_app.rerun()


# ==========================================
# 6. ENGLISH MODULE (Random 2 Questions)
# ==========================================
def english_screen():
  student = str_app.session_state.current_student
  questions = str_app.session_state.student_random_questions.get(
      student, {}
  ).get("english", [])

  str_app.subheader(
      f"English - {str_app.session_state.current_grade} ({student})"
  )

  if "e_index" not in str_app.session_state:
    str_app.session_state.e_index = 0
    str_app.session_state.e_score = 0

  idx = str_app.session_state.e_index
  if not questions or idx >= len(questions):
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
  c1.markdown(f"**Question {idx + 1} / {len(questions)} : {q['title']}**")
  c2.markdown(f"**Score: {str_app.session_state.e_score}**")

  if q["type"] == "reading" and "text" in q:
    str_app.markdown(
        f"""
            <div style="background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
                <b>📚 Reading Passage:</b><br>{q['text']}
            </div>
        """,
        unsafe_allow_html=True,
    )

  str_app.markdown(f"### {q.get('question', q.get('text'))}")
  if "options" in q:
    for opt in q["options"]:
      str_app.write(opt)

  attempt_key = ("english", student, idx)
  if attempt_key not in str_app.session_state.attempts:
    str_app.session_state.attempts[attempt_key] = 0

  current_attempts = str_app.session_state.attempts[attempt_key]
  str_app.write(
      f"⚠️ Attempt count: **{current_attempts} / 3** (3rd attempt saves final"
      " record)"
  )

  e_ans = str_app.text_input(
      "Type your answer here:", key=f"e_ans_{student}_{idx}"
  )

  if str_app.button("Check Answer"):
    if current_attempts < 3:
      str_app.session_state.attempts[attempt_key] += 1
      is_correct = False
      cleaned_ans = e_ans.strip().lower()

      if "answer" in q:
        if (
            cleaned_ans == q["answer"].lower()
            or cleaned_ans == q["answer"][0].lower()
        ):
          is_correct = True
      elif "expected" in q:
        if any(exp in cleaned_ans for exp in q["expected"]):
          is_correct = True

      if is_correct:
        str_app.session_state.e_score += 10
        str_app.success("🎉 Sirriitti deebiste, Foyyee qabda, Si hafa!")
        str_app.session_state.attempts[attempt_key] = 3
      else:
        rem = 3 - str_app.session_state.attempts[attempt_key]
        if rem > 0:
          str_app.warning(f"❌ Incorrect! Remaining attempts: {rem}")
        else:
          ans_text = q.get("answer", q.get("expected", [""])[0])
          str_app.error(f"❌ 3rd attempt reached. Correct answer: {ans_text}")
    else:
      str_app.info("Maximum attempts completed for this question.")

  str_app.markdown("---")
  b1, b2 = str_app.columns(2)
  with b1:
    if idx > 0 and str_app.button("⬅️ Duubatti (Previous)"):
      str_app.session_state.e_index -= 1
      str_app.rerun()
  with b2:
    if idx < len(questions) - 1:
      if str_app.button("Fuuldharatti (Next) ➡️"):
        str_app.session_state.e_index += 1
        str_app.rerun()
    else:
      if str_app.button("Finish & Return"):
        str_app.session_state.global_students[student]["english"] = (
            str_app.session_state.e_score
        )
        str_app.success(
            f"Well done! Total English Score: {str_app.session_state.e_score}"
        )
        str_app.session_state.e_index = 0
        str_app.session_state.e_score = 0
        str_app.session_state.current_page = "home"
        str_app.rerun()


# ==========================================
# 7. TEACHER DASHBOARD
# ==========================================
def teacher_dashboard_screen():
  str_app.subheader("🎓 Gabaasa Barsiisaa - Kutaa Barsiisaa (Teacher Report)")
  str_app.markdown(
      "**Qabxii Barattootaa, Parsantii (%) fi Cuunfaa Gabaasaa**"
  )

  students = str_app.session_state.global_students
  str_app.write(f"**Baay'inni barattoota galmaa'an:** {len(students)}")

  if not students:
    str_app.info("Ammaaf barataan galmaa'e hin jiru.")
  else:
    max_total_score = 60
    table_data = []
    csv_data = (
        "Maqaa Barataa,Kutaa,Afaan"
        " Oromoo,Herrega,Ingliffaa,Waliigala,Parsantii (%),Cuunfaa\n"
    )

    for name, data in students.items():
      ao = data["afaanOromoo"]
      math = data["math"]
      eng = data["english"]
      total = ao + math + eng
      percentage = (total / max_total_score) * 100

      table_data.append({
          "Maqaa Barataa": name,
          "Kutaa": data["grade"],
          "Afaan Oromoo": f"{ao}/20",
          "Herrega": f"{math}/20",
          "Ingliffaa": f"{eng}/20",
          "Waliigala": f"{total}/60",
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
