import random
import streamlit as str_app
from gTTS import gTTS
import os

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
            radial-gradient(circle at 12% 18%, rgba(0,137,123,0.10) 0%, transparent 42%),
            radial-gradient(circle at 88% 78%, rgba(255,213,79,0.14) 0%, transparent 42%),
            linear-gradient(135deg, #f4fbf7 0%, #e2f2e6 100%);
        background-attachment: fixed;
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
        padding: 38px 22px;
        border-radius: 24px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 18px 40px rgba(0, 77, 64, 0.45), 0 0 0 8px rgba(128, 203, 196, 0.30);
        border: 4px solid #ffd54f;
        position: relative;
        overflow: hidden;
    }
    .hero-box::after {
        content: "";
        position: absolute;
        top: -60%;
        left: -60%;
        width: 220%;
        height: 220%;
        background: radial-gradient(circle, rgba(255,255,255,0.10) 0%, transparent 60%);
        animation: heroGlow 7s ease-in-out infinite;
        pointer-events: none;
    }
    @keyframes heroGlow {
        0%, 100% { transform: translate(0, 0); }
        50% { transform: translate(8%, 8%); }
    }
    .hero-box h1, .hero-box h2, .hero-box p {
        position: relative;
        z-index: 1;
    }
    .hero-box h1 {
        font-size: 2rem;
        margin-bottom: 10px;
        font-weight: 800;
        letter-spacing: 1px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.25);
    }
    .hero-box p {
        font-size: 1.05rem;
        line-height: 1.5;
        color: #e0f2f1;
    }
    .books-info-card {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 18px;
        border-left: 6px solid #004d40;
        box-shadow: 0 8px 22px rgba(0,0,0,0.10);
        margin-bottom: 20px;
        transition: 0.3s ease;
    }
    .books-info-card:hover {
        box-shadow: 0 12px 28px rgba(0,77,64,0.18);
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
        background: linear-gradient(135deg, #e0f2f1 0%, #fff8e1 100%);
        padding: 14px;
        border-radius: 14px;
        border: 2px dashed #00897b;
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    .score-pill {
        display: inline-block;
        background: linear-gradient(135deg, #00897b, #00695c);
        color: white !important;
        font-weight: bold;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.95rem;
        box-shadow: 0 3px 8px rgba(0,105,92,0.3);
    }
    .attempt-pill {
        display: inline-block;
        background-color: #fff3e0;
        color: #e65100 !important;
        font-weight: bold;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        border: 1px solid #ffb74d;
        margin: 6px 0 14px 0;
    }
    div[data-testid="stImage"] img {
        border-radius: 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.15);
        border: 3px solid #ffffff;
    }
    div[data-testid="stAudio"] {
        margin-bottom: 12px;
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
if "teacher_auth" not in str_app.session_state:
    str_app.session_state.teacher_auth = False

# MASTER QUESTION BANK KAJFA (SESSION STATE KEESSATTI QABAMUU ISAA KAN FAYYADAMU GAAFII HAARAA ITTI DABALUUF FI HAQUUF)
if "SECRET_MASTER_QUESTION_BANKS" not in str_app.session_state:
    str_app.session_state.SECRET_MASTER_QUESTION_BANKS = {
        "Kutaa 1": {
            "afaan_oromoo": [
                {"question": "Qubeen jalqabaa  Afaan Oromoo kami?", "options": ["A) A", "B) B", "C) C", "D) D"], "answer": "A", "type": "mcq"},
                {"question": "Jecha 'Mama' jedhu keessatti sagaleen irra deddeebi'amu maali?", "options": ["A) M", "B) N", "C) T", "D) S"], "answer": "A", "type": "mcq"},
                {"question": "Bishaan dhuguuf maal fayyadamna?", "options": ["A) Xurii", "B) Xiyyaara", "C) Xuuftuu", "D) Qodaa"], "answer": "D", "type": "mcq"},
                {"question": "Jecha 'Haadha' jedhu keessaa qubee jalqabaa filadhu:", "options": ["A) H", "B) B", "C) K", "D) L"], "answer": "A", "type": "mcq"},
                {"question": "Mana barumsaa maaliif deemna?", "options": ["A) Barachuuf", "B) Rafuuf", "C) Taphachuuf qofa", "D) Maseenuuf"], "answer": "A", "type": "mcq"},
                {"question": "Qubee 'B'n jecha kam jalqaba?", "options": ["A) Balleessaa", "B) Adaamaa", "C) Caalaa", "D) Dhagaa"], "answer": "A", "type": "mcq"},
                 {"question": "Jecha Lafaa Kan ta'e kami?", "options": ["A) Tulluu", "B) Kubbaa", "C) Mana", "D) Madda"], "answer": "C", "type": "mcq"},
                 {"question": "Horii Manaa Kan ta'e kami?", "options": ["A) Qamalee", "B) Jaldeessa", "C) Leenca", "D) Hoolaa"], "answer": "D", "type": "mcq"},
                 {"question": "Jecha Dheeraa Kan ta'e kami?", "options": ["A) Laafaa", "B) laga", "C) mala", "D) nama"], "answer": "A", "type": "mcq"},
                 {"question": "Qubee Afaan oromoo keessaa Dachaa kan ta'e kami?", "options": ["A) A", "B) B", "C) Ch", "D) x"], "answer": "C", "type": "mcq"},
            ],
            "math": [
                {"question": "1 + 1 hammami?", "options": ["A) 1", "B) 2", "C) 3", "D) 4"], "answer": "B", "type": "mcq"},
                {"question": "3 - 1 hammami?", "options": ["A) 1", "B) 2", "C) 3", "D) 0"], "answer": "B", "type": "mcq"},
                {"question": "Lakkoofsi 5 irra caalu kami?", "options": ["A) 4", "B) 3", "C) 6", "D) 2"], "answer": "C", "type": "mcq"},
                {"question": "2 + 3 hammami?", "options": ["A) 5", "B) 4", "C) 6", "D) 7"], "answer": "A", "type": "mcq"},
                {"question": "10 - 5 hammami?", "options": ["A) 2", "B) 5", "C) 4", "D) 3"], "answer": "B", "type": "mcq"},
                {"question": "Lakkoofsa 0 booda maaltu dhufa?", "options": ["A) 1", "B) 2", "C) 3", "D) 4"], "answer": "A", "type": "mcq"}
            ],
            "english": [
                {"question": "What letter comes after 'A'?", "options": ["A) B", "B) C", "C) D", "D) E"], "answer": "A", "type": "mcq"},
                {"question": "Choose the color of the sky:", "options": ["A) Red", "B) Blue", "C) Green", "D) Yellow"], "answer": "B", "type": "mcq"},
                {"question": "How many fingers on one hand?", "options": ["A) 3", "B) 4", "C) 5", "D) 10"], "answer": "C", "type": "mcq"},
                {"question": "Select the correct capital letter for 'g':", "options": ["A) G", "B) H", "C) F", "D) J"], "answer": "A", "type": "mcq"},
                {"question": "What do we use to see?", "options": ["A) Ears", "B) Eyes", "C) Nose", "D) Hands"], "answer": "B", "type": "mcq"},
                {"question": "Complete: 'A for ___'", "options": ["A) Apple", "B) Ball", "C) Cat", "D) Dog"], "answer": "A", "type": "mcq"}
            ]
        },
        "Kutaa 2": {
            "afaan_oromoo": [
                {"question": "Jechi 'Nama' jedhu hiika maali qaba?", "options": ["A) Lubbu qabeessa", "B) Mukaa", "C) Bishaan", "D) Dhagaa"], "answer": "A", "type": "mcq"},
                {"question": "Quboonni sagaleessoo (vowels) Afaan Oromoo meeqa?", "options": ["A) 5", "B) 22", "C) 27", "D) 30"], "answer": "A", "type": "mcq"},
                {"question": "Jecha 'Fira' jedhuuf faallaan isaa maali?", "options": ["A) Diina", "B) Jaalallee", "C) Obboleessa", "D) Hiriyaa"], "answer": "A", "type": "mcq"},
                {"question": "Dirmammuu yeroo jedhamu maal ibsa?", "options": ["A) Gadaa", "B) Guyyaa", "C) Halkan", "D) Boru"], "answer": "B", "type": "mcq"},
                {"question": "Nagaan bultaniifi deebiin isaa maali?", "options": ["A) Fayyaa bulle", "B) Raffee", "C) Deeme", "D) Dhufe"], "answer": "A", "type": "mcq"},
                {"question": "Afaan Oromoo keessatti qubeen 'Ch'n qubee akkamiiti?", "options": ["A) Qubee dachaa", "B) Qubee dubbachiiftuu", "C) Qubee salphaa", "D) Qubee gabaabaa"], "answer": "A", "type": "mcq"}
            ],
            "math": [
                {"question": "10 + 10 hammami?", "options": ["A) 15", "B) 20", "C) 25", "D) 30"], "answer": "B", "type": "mcq"},
                {"question": "5 x 2 hammami?", "options": ["A) 7", "B) 10", "C) 12", "D) 8"], "answer": "B", "type": "mcq"},
                {"question": "15 - 7 hammami?", "options": ["A) 8", "B) 7", "C) 9", "D) 6"], "answer": "A", "type": "mcq"},
                {"question": "8 + 6 hammami?", "options": ["A) 12", "B) 13", "C) 14", "D) 15"], "answer": "C", "type": "mcq"},
                {"question": "4 x 3 hammami?", "options": ["A) 12", "B) 10", "C) 14", "D) 16"], "answer": "A", "type": "mcq"},
                {"question": "Lakkoofsi 20 hir'uu ykn guutuu?", "options": ["A) Guutuu", "B) Hir'uu", "C) Lamaanuu miti", "D) Walii gala"], "answer": "A", "type": "mcq"}
            ],
            "english": [
                {"question": "What is the plural of 'Cat'?", "options": ["A) Cat", "B) Cats", "C) Cates", "D) Caties"], "answer": "B", "type": "mcq"},
                {"question": "Choose the animal that barks:", "options": ["A) Cat", "B) Dog", "C) Cow", "D) Bird"], "answer": "B", "type": "mcq"},
                {"question": "Opposite of 'Hot' is:", "options": ["A) Warm", "B) Cold", "C) Ice", "D) Sun"], "answer": "B", "type": "mcq"},
                {"question": "Complete: 'I ___ a student.'", "options": ["A) am", "B) is", "C) are", "D) be"], "answer": "A", "type": "mcq"},
                {"question": "Which one is a fruit?", "options": ["A) Potato", "B) Mango", "C) Carrot", "D) Onion"], "answer": "B", "type": "mcq"},
                {"question": "How many days are in a week?", "options": ["A) 5", "B) 6", "C) 7", "D) 8"], "answer": "C", "type": "mcq"}
            ]
        },
        "Kutaa 3": {
            "afaan_oromoo": [
                {"question": "Fookloorii jechuun maali?", "options": ["A) Aadaa fi duudhaa", "B) Herrega", "C) Kompiitara", "D) Farmaasii"], "answer": "A", "type": "mcq"},
                {"question": "Mamaaksa 'Odoo beekanuu...' maaliin xumurama?", "options": ["A) Boolla seenu", "B) Gammoojjitti hafu", "C) Bishaan dhugu", "D) Rafu"], "answer": "A", "type": "mcq"},
                {"question": "Afaan Oromoo keessatti hudhaan ( ' ) maal godha?", "options": ["A) Sagalee cisaa godha", "B) Sagalee cittuu godha", "C) Dheeressa", "D) Jabessa"], "answer": "B", "type": "mcq"},
                {"question": "Jechoota hammamtaa ibsan keessaa kami?", "options": ["A) Baay'ee", "B) Gurraacha", "C) Dheeraa", "D) Deemaa"], "answer": "A", "type": "mcq"},
                {"question": "Hiika jecha 'Arjooma':", "options": ["A) Arjaamu/Lootuu", "B) Jibbiinsa", "C) Qorqalbii", "D) Walitti bu'iinsa"], "answer": "A", "type": "mcq"},
                {"question": "Dhaabbanni barumsaa maal fa'i qaba?", "options": ["A) Barattoota fi Barsiisota", "B) Bineensota qofa", "C) Konkolaataa qofa", "D) Xiyyaara"], "answer": "A", "type": "mcq"}
            ],
            "math": [
                {"question": "50 - 25 hammami?", "options": ["A) 20", "B) 25", "C) 30", "D) 15"], "answer": "B", "type": "mcq"},
                {"question": "6 x 4 hammami?", "options": ["A) 20", "B) 24", "C) 28", "D) 22"], "answer": "B", "type": "mcq"},
                {"question": "100 / 10 hammami?", "options": ["A) 5", "B) 10", "C) 15", "D) 20"], "answer": "B", "type": "mcq"},
                {"question": "30 + 45 hammami?", "options": ["A) 75", "B) 70", "C) 80", "D) 65"], "answer": "A", "type": "mcq"},
                {"question": "Herrega: (2 x 5) + 3 =", "options": ["A) 13", "B) 10", "C) 15", "D) 12"], "answer": "A", "type": "mcq"},
                {"question": "Garaagarummaa 50 fi 20 meeqa?", "options": ["A) 30", "B) 20", "C) 40", "D) 10"], "answer": "A", "type": "mcq"}
            ],
            "english": [
                {"question": "Opposite of 'Big' is:", "options": ["A) Small", "B) Tall", "C) Fast", "D) Heavy"], "answer": "A", "type": "mcq"},
                {"question": "Choose the verb: 'She sings a song.'", "options": ["A) She", "B) sings", "C) a", "D) song"], "answer": "B", "type": "mcq"},
                {"question": "Plural of 'Box':", "options": ["A) Boxs", "B) Boxes", "C) Boxen", "D) Boxies"], "answer": "B", "type": "mcq"},
                {"question": "Past form of 'Eat':", "options": ["A) Eats", "B) Ate", "C) Eaten", "D) Eating"], "answer": "B", "type": "mcq"},
                {"question": "What is the capital of Ethiopia?", "options": ["A) Addis Ababa", "B) Hawassa", "C) Adama", "D) Jimma"], "answer": "A", "type": "mcq"},
                {"question": "A person who teaches in a school is a:", "options": ["A) Doctor", "B) Teacher", "C) Driver", "D) Farmer"], "answer": "B", "type": "mcq"}
            ]
        },
        "Kutaa 4": {
            "afaan_oromoo": [
                {"question": "Akkaataan itti walaloo barreessan keessaa inni ijoo maali?", "options": ["A) Rurkee fi wal-fakkeenya sagalee", "B) Lakkoofsa qofa", "C) Fakkii kaasuu", "D) Herreguu"], "answer": "A", "type": "mcq"},
                {"question": "Jechoota Gochibsa (Adverb) ta'an filadhu:", "options": ["A) Suuta", "B) Muka", "C) Gurraacha", "D) Inni"], "answer": "A", "type": "mcq"},
                {"question": "Bara durii ergaa waliif dabarsuuf maaliin fayyadamu ture?", "options": ["A) Ergaa afaanii fi Sagalee fardaa/moraa", "B) Bilbila harkaatiin", "C) Imeeliidhaan", "D) Interneetiin"], "answer": "A", "type": "mcq"},
                {"question": "Jecha 'Gabaabaa' jedhuuf faallaan isaa maali?", "options": ["A) Dheeraa", "B) Furdaa", "C) Xiqqaatamaa", "D) Ulfaataa"], "answer": "A", "type": "mcq"},
                {"question": "Seenaa fi Aadaa keenya kunuunsun maaliif barbaachisa?", "options": ["A) Dhalootatti dabarsuuf", "B) Dagachuuf", "C) Gatachuuf", "D) Dhabamsiisuuf"], "answer": "A", "type": "mcq"},
                {"question": "Afaan Oromoo keessatti qubooni jabaatan yoo barreeffaman:", "options": ["A) Qubee dachaa ta'u", "B) Qubee fardii ta'u", "C) Qubee dubbachiiftuu lamaan barreeffamu", "D) Qubee dubbisaa lamaan barreeffamu"], "answer": "D", "type": "mcq"}
            ],
            "math": [
                {"question": "144 / 12 hammami?", "options": ["A) 10", "B) 11", "C) 12", "D) 14"], "answer": "C", "type": "mcq"},
                {"question": "25 x 4 hammami?", "options": ["A) 80", "B) 90", "C) 100", "D) 110"], "answer": "C", "type": "mcq"},
                {"question": "Kopee birrii 200 ta'e irraa 150 yoo kaffalle rezaaltiin meeqa?", "options": ["A) 50", "B) 40", "C) 60", "D) 30"], "answer": "A", "type": "mcq"},
                {"question": "1/2 fi 1/2 yoo walitti ida'an meeqa ta'a?", "options": ["A) 1", "B) 1/4", "C) 2", "D) 0"], "answer": "A", "type": "mcq"},
                {"question": "Pemetaa skweerii loolli isaa 5cm ta'ee meeqa?", "options": ["A) 20cm", "B) 25cm", "C) 15cm", "D) 10cm"], "answer": "A", "type": "mcq"},
                {"question": "Shallaggaa: 8 x 8 - 4 =", "options": ["A) 60", "B) 64", "C) 58", "D) 62"], "answer": "A", "type": "mcq"}
            ],
            "english": [
                {"question": "Past tense of 'Run' is:", "options": ["A) Running", "B) Ran", "C) Runed", "D) Runs"], "answer": "B", "type": "mcq"},
                {"question": "Identify the pronoun: 'They are playing football.'", "options": ["A) They", "B) are", "C) playing", "D) football"], "answer": "A", "type": "mcq"},
                {"question": "Choose the correct spelling:", "options": ["A) Beautifull", "B) Beautiful", "C) Beutiful", "D) Beautifyl"], "answer": "B", "type": "mcq"},
                {"question": "A place where we read books is a:", "options": ["A) Hospital", "B) Library", "C) Bank", "D) Market"], "answer": "B", "type": "mcq"},
                {"question": "What is the synonym of 'Happy'?", "options": ["A) Sad", "B) Joyful", "C) Angry", "D) Tired"], "answer": "B", "type": "mcq"},
                {"question": "Complete: 'She ___ her homework yesterday.'", "options": ["A) do", "B) did", "C) does", "D) doing"], "answer": "B", "type": "mcq"}
            ]
        },
        "Kutaa 5": {
            "afaan_oromoo": [
                {"question": "Seenaa Oromoo keessatti Gadaan sirna akkamii ti?", "options": ["A) Sirna dimokraasii fi bulchiinsaa", "B) Sirna daldala qofa", "C) Sirna waraanaa qofa", "D) Sirna barumsaa ammayyaa"], "answer": "A", "type": "mcq"},
                {"question": "Dhaamsa Caqasaa fi Dubbisaa keessaa yaanni ijoo maali?", "options": ["A) Beekkumsa horachuu fi hubannoo gabbifachuu", "B) Wawwaachuu", "C) Sagalee ol kaasuu", "D) Aarsuu"], "answer": "A", "type": "mcq"},
                {"question": "Mormii fi Miti-mormii walaloo keessatti maaltu uuma?", "options": ["A) Miira fi Yada walxaxaa", "B) Lakkoofsa", "C) Fakkii", "D) Herrega"], "answer": "A", "type": "mcq"},
                {"question": "Dookumentaroonni aadaa fi seenaa maaliif fayyadu?", "options": ["A) Ragaa seenaa kaa'uuf", "B) Taphaaf qofa", "C) Fiilmii sobaa uumuuf", "D) Dagachiisuuf"], "answer": "A", "type": "mcq"},
                {"question": "Afaan Oromoo keessatti Maqibsa (Adjective) ta'u kan danda'u kami?", "options": ["A) Bareedaa", "B) Deeme", "C) Inni", "D) Mana"], "answer": "A", "type": "mcq"},
                {"question": "Ogbarruu afaaniin kan dhihaatan keessaa kami?", "options": ["A) Mamaaksa fi Eebba", "B) Kitaaba barataa", "C) Qorannoo saayinsii", "D) Gaazexaa"], "answer": "A", "type": "mcq"}
            ],
            "math": [
                {"question": "Hanga harka 3/4 kan 100 meeqa?", "options": ["A) 50", "B) 75", "C) 25", "D) 100"], "answer": "B", "type": "mcq"},
                {"question": "Avireejii (Mean) lakkoofsota 10, 20 fi 30 meeqa?", "options": ["A) 20", "B) 15", "C) 25", "D) 30"], "answer": "A", "type": "mcq"},
                {"question": "Dhibbeentaa (%): 20% kan 200 meeqa?", "options": ["A) 20", "B) 40", "C) 50", "D) 60"], "answer": "B", "type": "mcq"},
                {"question": "Skweer ruutii (Sqrt) kan 81 meeqa?", "options": ["A) 7", "B) 8", "C) 9", "D) 10"], "answer": "C", "type": "mcq"},
                {"question": "15 x 15 hammami?", "options": ["A) 200", "B) 225", "C) 250", "D) 215"], "answer": "B", "type": "mcq"},
                {"question": "Shallaggaa: 3^2 + 4^2 =", "options": ["A) 25", "B) 12", "C) 14", "D) 20"], "answer": "A", "type": "mcq"}
            ],
            "english": [
                {"question": "Choose the correct preposition: 'The book is ___ the table.'", "options": ["A) on", "B) in", "C) at", "D) under"], "answer": "A", "type": "mcq"},
                {"question": "Opposite of 'Ancient' is:", "options": ["A) Old", "B) Modern", "C) Historic", "D) Past"], "answer": "B", "type": "mcq"},
                {"question": "Choose the correct conjunction: 'He failed ___ he did not study.'", "options": ["A) because", "B) but", "C) or", "D) so"], "answer": "A", "type": "mcq"},
                {"question": "What is the comparative form of 'Good'?", "options": ["A) Gooder", "B) Better", "C) Best", "D) More good"], "answer": "B", "type": "mcq"},
                {"question": "Identify the passive voice: 'The ball was kicked by Ali.'", "options": ["A) Ali kicked the ball", "B) The ball was kicked by Ali", "C) Ali is kicking", "D) Kicking ball Ali"], "answer": "B", "type": "mcq"},
                {"question": "A person who flies an airplane is a:", "options": ["A) Sailor", "B) Pilot", "C) Driver", "D) Astronaut"], "answer": "B", "type": "mcq"}
            ]
        },
        "Kutaa 6": {
            "afaan_oromoo": [
                {"question": "Jecha 'Goota' jedhuuf hiika tokko filadhu:", "options": ["A) Sodaa", "B) Jajjabaa/Namicha hojii guddaa hojjete", "C) Dadhabaa", "D) Dhukkubsataa"], "answer": "B", "type": "mcq"},
                {"question": "Hiika ciigoo: 'Morma irraa qaba' jechuun maali?", "options": ["A) Morma qabaachuu", "B) Miti-deeggaru / Mormuu", "C) Dhiiga morma", "D) Muka morma"], "answer": "B", "type": "mcq"},
                {"question": "Ijaarsa Chasa Caaslugaa keessatti 'Fiixee'n maal ibsa?", "options": ["A) Kutaa barruu", "B) Xumura jechaa ykn jechamaa", "C) Jalqaba fuulaa", "D) Qaama midhaanii"], "answer": "B", "type": "mcq"},
                {"question": "Hojii Qorannoo Afaanii keessatti fiilmgirafiin maal agarsiisa?", "options": ["A) Ragaalee suuraa fi sagaleetiin kaafaman", "B) Kitaaba gabaabaa", "C) Walaloo", "D) Seenaa kaleessaa"], "answer": "A", "type": "mcq"},
                {"question": "Ciroo Yeroo jechuun maal ibsa?", "options": ["A) Yeroo gochi tokko itti raawwatame", "B) Bakka gochi itti raawwatame", "C) Akkaataa gochaa", "D) Sababa gochaa"], "answer": "A", "type": "mcq"},
                {"question": "Jechi 'Furtuu' jedhu yeroo mammaaksatti fayyadamnu:", "options": ["A) Cufiinsa fi banaa ibsa", "B) Herrega ibsa", "C) Nyata ibsa", "D) Taphachuu ibsa"], "answer": "A", "type": "mcq"}
            ],
            "math": [
                {"question": "Herrega shallaggaa: 25 + (5 * 2) =", "options": ["A) 60", "B) 35", "C) 30", "D) 50"], "answer": "B", "type": "mcq"},
                {"question": "Equation hiiki: 2x + 10 = 20, x meeqa?", "options": ["A) 5", "B) 10", "C) 2", "D) 4"], "answer": "A", "type": "mcq"},
                {"question": "Radiyaasiin sarboolii (Circle) 7cm ta'nan, Diiyaameetriin meeqa?", "options": ["A) 14cm", "B) 21cm", "C) 49cm", "D) 10cm"], "answer": "A", "type": "mcq"},
                {"question": "2^4 (2 raised to 4) hammami?", "options": ["A) 8", "B) 16", "C) 12", "D) 32"], "answer": "B", "type": "mcq"},
                {"question": "Yoo x = 3 fi y = 4 ta'e, x^2 + y^2 meeqa?", "options": ["A) 25", "B) 12", "C) 49", "D) 14"], "answer": "A", "type": "mcq"},
                {"question": "Ratio 3:5 kan 80 meeqa qooda?", "options": ["A) 30 fi 50", "B) 20 fi 60", "C) 40 fi 40", "D) 10 fi 70"], "answer": "A", "type": "mcq"}
            ],
            "english": [
                {"question": "Identify the adjective in the sentence: 'She has a fast car.'", "options": ["A) She", "B) has", "C) fast", "D) car"], "answer": "C", "type": "mcq"},
                {"question": "Select the correct conditional: 'If it rains, we ___ at home.'", "options": ["A) will stay", "B) stayed", "C) stays", "D) staying"], "answer": "A", "type": "mcq"},
                {"question": "What is the superlative form of 'Expensive'?", "options": ["A) Most expensive", "B) More expensive", "C) Expensivest", "D) Expensiver"], "answer": "A", "type": "mcq"},
                {"question": "Choose the synonym for 'Huge':", "options": ["A) Small", "B) Enormous", "C) Tiny", "D) Short"], "answer": "B", "type": "mcq"},
                {"question": "Complete with relative pronoun: 'The boy ___ won the match is my brother.'", "options": ["A) who", "B) which", "C) where", "D) whose"], "answer": "A", "type": "mcq"},
                {"question": "Identify the noun: 'Honesty is the best policy.'", "options": ["A) Honesty", "B) is", "C) best", "D) the"], "answer": "A", "type": "mcq"}
            ]
        }
    }

# KUUSAA QORMAATA SAGALEE (AUDIO DICTATION TEST BANK)
if "SECRET_AUDIO_DICTATION_BANKS" not in str_app.session_state:
    str_app.session_state.SECRET_AUDIO_DICTATION_BANKS = {
        "Kutaa 1": [
            {"word": "Laafaa", "hint": "Sagalee dubbatu dhaggeeffadhuu barreessii (Fkn: laa-faa)"},
            {"word": "malaa", "hint": "Sagalee dubbatu dhaggeeffadhuu barreessii"},
            {"word":"Tulluu","hint":"sagalee dhaggeeffadhuu barreessii"},
            {"word": "Mana", "hint": "Sagalee dubbatu dhaggeeffadhuu barreessii"},
        ],
        "Kutaa 2": [
            {"word": "nama", "hint": "Jecha sagaleeffame barreessi"},
            {"word": "fira", "hint": "Jecha sagaleeffame barreessi"}
        ],
        "Kutaa 3": [
            {"word": "arjooma", "hint": "Sagalee dhaggeeffadhuu barreessi"},
            {"word": "fookloorii", "hint": "Sagalee dhaggeeffadhuu barreessi"}
        ],
        "Kutaa 4": [
            {"word": "suuta", "hint": "Sagalee dhaggeeffadhuu barreessi"},
            {"word": "gabaabaa", "hint": "Jecha sagaleeffame barreessi"}
        ],
        "Kutaa 5": [
            {"word": "gadaa", "hint": "Sagalee dhaggeeffadhuu barreessi"},
            {"word": "bareedaa", "hint": "Jecha sagaleeffame barreessi"}
        ],
        "Kutaa 6": [
            {"word": "tabba", "hint": "Sagalee 'tabba' jedhu dhaggeeffadhuu barreessi"},
            {"word": "goota", "hint": "Jecha sagaleeffame barreessi"}
        ]
    }

def load_databases_for_grade(grade_str):
    bank = str_app.session_state.SECRET_MASTER_QUESTION_BANKS.get(grade_str, str_app.session_state.SECRET_MASTER_QUESTION_BANKS["Kutaa 6"])

    def select_unique_random_questions(pool):
        if len(pool) >= 6:
            return random.sample(pool, 6)
        else:
            selected = pool[:]
            while len(selected) < 6 and pool:
                selected.append(random.choice(pool))
            return selected

    return {
        "afaan_oromoo": select_unique_random_questions(bank["afaan_oromoo"]),
        "math": select_unique_random_questions(bank["math"]),
        "english": select_unique_random_questions(bank["english"])
    }


def role_selection_screen():
    str_app.markdown(
        """
        <div class="hero-box">
            <h1>📖 Hiika Way (HW) APP</h1>
            <p>
                Baga Nagaan Gara App Dandeettii Dubbisuu, Barreessuu, Shallaguu Fi Qormaata Sagalee (Dictation) Barattootaa Adda Baasu "Hika Way" Kitesa Negasa tiin kalaqameetti Nagaan Dhuftan!
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
                <li><b>🔊 Qormaata Sagalee (Audio Dictation):</b> Dandeettii barreessuu barattootaa sagaleen madaaluu.</li>
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
            str_app.session_state.current_page = "teacher_login"
            str_app.rerun()
        str_app.markdown("</div>", unsafe_allow_html=True)


def teacher_login_screen():
    str_app.markdown(
        """
        <div class="hero-box">
            <h2>🔒 Seensa Iccitii Barsiisaa (Teacher Login)</h2>
            <p>Maaloo Daashboordii seenuuf Paasworii barsiisaa galchaa</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    pwd = str_app.text_input("Paasworii (Password)", type="password", placeholder="Iccitii galchaa...")
    
    col1, col2 = str_app.columns(2)
    with col1:
        if str_app.button("Mirkaneessi Seeni"):
            if pwd == "admin123":
                str_app.session_state.teacher_auth = True
                str_app.session_state.current_page = "teacher_dashboard"
                str_app.rerun()
            else:
                str_app.error("❌ Paasworriin dogoggora! Maaloo irra deebi'aa yaalaa.")
    with col2:
        if str_app.button("⬅️ Duubatti"):
            str_app.session_state.current_page = "role_selection"
            str_app.rerun()


def name_input_screen():
    str_app.markdown(
        """
        <div class="hero-box">
            <h2>Galmee Maqaa, Korniyaa & Lakk. Daree Barataa</h2>
            <p>Maaloo odeeffannoo guutuu kee as irratti galchi</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    name = str_app.text_input("Maqaa Guutuu", placeholder="Maqaa kee guutuu barreessi...")
    gender = str_app.selectbox("Korniyaa (Gender)", ["Dhiira", "Dhalaa"])
    section = str_app.text_input("Lakk. Daree (Section / Room)", placeholder="Fkn: Kutaa 6A ykn Daree 2")
    grade = str_app.selectbox(
        "Kutaa Barumsaa (Grade 1 - 6)",
        ["Kutaa 1", "Kutaa 2", "Kutaa 3", "Kutaa 4", "Kutaa 5", "Kutaa 6"],
    )

    col1, col2 = str_app.columns(2)
    with col1:
        if str_app.button("Gara Appiitti Darbi"):
            if name.strip() and section.strip():
                clean_name = name.strip()
                str_app.session_state.current_student = clean_name
                str_app.session_state.current_grade = grade

                if clean_name not in str_app.session_state.global_students:
                    str_app.session_state.global_students[clean_name] = {
                        "grade": grade,
                        "gender": gender,
                        "section": section.strip(),
                        "afaanOromoo": 0,
                        "math": 0,
                        "english": 0,
                        "audioDictation": 0,
                    }

                selected_qs = load_databases_for_grade(grade)
                str_app.session_state.student_random_questions[clean_name] = selected_qs

                str_app.session_state.current_page = "home"
                str_app.rerun()
            else:
                str_app.warning("Maaloo Maqaa guutuu fi Lakk. Daree kee guuti!")
    with col2:
        if str_app.button("⬅️ Duubatti"):
            str_app.session_state.current_page = "role_selection"
            str_app.rerun()


def home_screen():
    str_app.markdown(
        f"""
        <div class="hero-box">
            <h2>Baga nagaan dhuftte, {str_app.session_state.current_student} ({str_app.session_state.current_grade})!</h2>
            <p>Gosa barnootaa ykn Qormaata barachuu barbaaddu filadhu</p>
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

    str_app.write("")
    if str_app.button("🔊 Qormaata Sagalee (Audio Dictation Test)"):
        str_app.session_state.current_page = "audio_dictation"
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
        str_app.warning("Gaaffiin Afaan Oromoo hin argamne.")
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
    c2.markdown(f'<span class="score-pill">Qabxii: {str_app.session_state.ao_score}</span>', unsafe_allow_html=True)

    str_app.markdown(f"### {q.get('question', '')}")

    if q.get("image"):
        img_c1, img_c2, img_c3 = str_app.columns([1, 2, 1])
        with img_c2:
            str_app.image(q["image"], use_container_width=True)

    user_answer = None
    if q.get("type", "mcq") == "mcq" and "options" in q:
        user_answer = str_app.radio(
            "Filannoo kee filadhu:", q["options"], key=f"ao_radio_{student}_{idx}", index=None
        )
    else:
        user_answer = str_app.text_input("Deebii kee asitti barreessi:", key=f"ao_ans_{student}_{idx}")

    attempt_key = ("afaan_oromoo", student, idx)
    if attempt_key not in str_app.session_state.attempts:
        str_app.session_state.attempts[attempt_key] = 0

    current_attempts = str_app.session_state.attempts[attempt_key]
    str_app.markdown(f'<span class="attempt-pill">⚠️ Carraa deebii yaaluu: {current_attempts} / 3</span>', unsafe_allow_html=True)

    if str_app.button("Mirkaneessi Afaan Oromoo"):
        if user_answer is None or (isinstance(user_answer, str) and not user_answer.strip()):
            str_app.warning("⚠️ Maaloo dursii filannoo/deebii kee filadhu!")
        elif current_attempts < 3:
            str_app.session_state.attempts[attempt_key] += 1
            is_correct = False

            if "answer" in q:
                correct = str(q["answer"])
                if user_answer and (user_answer.strip().upper() == correct.upper() or user_answer.strip().startswith(correct)):
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
        str_app.warning("Gaaffiin Herregaa hin argamne.")
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
    c2.markdown(f'<span class="score-pill">Qabxii: {str_app.session_state.m_score}</span>', unsafe_allow_html=True)

    str_app.markdown(f"### {q.get('question', '')}")

    if q.get("image"):
        img_c1, img_c2, img_c3 = str_app.columns([1, 2, 1])
        with img_c2:
            str_app.image(q["image"], use_container_width=True)

    user_answer = None
    if q.get("type", "mcq") == "mcq" and "options" in q:
        user_answer = str_app.radio(
            "Filannoo kee filadhu:", q["options"], key=f"m_radio_{student}_{idx}", index=None
        )
    else:
        user_answer = str_app.text_input("Deebii kee asitti barreessi:", key=f"m_ans_{student}_{idx}")

    attempt_key = ("math", student, idx)
    if attempt_key not in str_app.session_state.attempts:
        str_app.session_state.attempts[attempt_key] = 0

    current_attempts = str_app.session_state.attempts[attempt_key]
    str_app.markdown(f'<span class="attempt-pill">⚠️ Carraa deebii yaaluu: {current_attempts} / 3</span>', unsafe_allow_html=True)

    if str_app.button("Mirkaneessi Herregaa"):
        if user_answer is None or (isinstance(user_answer, str) and not user_answer.strip()):
            str_app.warning("⚠️ Maaloo dursii filannoo/deebii kee filadhu!")
        elif current_attempts < 3:
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
        str_app.warning("English questions not found.")
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
    c2.markdown(f'<span class="score-pill">Score: {str_app.session_state.e_score}</span>', unsafe_allow_html=True)

    str_app.markdown(f"### {q.get('question', '')}")

    if q.get("image"):
        img_c1, img_c2, img_c3 = str_app.columns([1, 2, 1])
        with img_c2:
            str_app.image(q["image"], use_container_width=True)

    user_answer = None
    if q.get("type", "mcq") and "options" in q:
        user_answer = str_app.radio(
            "Choose your option:", q["options"], key=f"e_radio_{student}_{idx}", index=None
        )
    else:
        user_answer = str_app.text_input("Type your answer here:", key=f"e_ans_{student}_{idx}")

    attempt_key = ("english", student, idx)
    if attempt_key not in str_app.session_state.attempts:
        str_app.session_state.attempts[attempt_key] = 0

    current_attempts = str_app.session_state.attempts[attempt_key]
    str_app.markdown(f'<span class="attempt-pill">⚠️ Attempt count: {current_attempts} / 3</span>', unsafe_allow_html=True)

    if str_app.button("Check Answer"):
        if user_answer is None or (isinstance(user_answer, str) and not user_answer.strip()):
            str_app.warning("⚠️ Please select an option / type your answer first!")
        elif current_attempts < 3:
            str_app.session_state.attempts[attempt_key] += 1
            is_correct = False

            if "answer" in q:
                ans_str = str(q["answer"]).lower()
                if user_answer:
                    cleaned_ans = user_answer.strip().lower()
                    if cleaned_ans == ans_str or cleaned_ans.startswith(ans_str[0]):
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
                    ans_text = q.get("answer", "")
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


def audio_dictation_screen():
    student = str_app.session_state.current_student
    grade = str_app.session_state.current_grade
    dict_list = str_app.session_state.SECRET_AUDIO_DICTATION_BANKS.get(grade, [])

    str_app.subheader(f"🔊 Qormaata Sagalee (Audio Dictation Test) - {grade} ({student})")

    if not dict_list:
        str_app.warning("Qormaatni sagalee kutaa kanaaf hin jiru.")
        if str_app.button("🏠 Gara Manayeessaa"):
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    if "aud_index" not in str_app.session_state:
        str_app.session_state.aud_index = 0
        str_app.session_state.aud_score = 0

    idx = str_app.session_state.aud_index
    if idx >= len(dict_list):
        str_app.success("Qormaatni Sagalee xumurameera! Galatoomi.")
        if str_app.button("🏠 Gara Manayeessaa"):
            str_app.session_state.aud_index = 0
            str_app.session_state.aud_score = 0
            str_app.session_state.current_page = "home"
            str_app.rerun()
        return

    item = dict_list[idx]
    target_word = item["word"]
    hint = item["hint"]

    str_app.progress((idx + 1) / len(dict_list))
    str_app.markdown(f"**Gaaffii Sagalee {idx + 1} / {len(dict_list)}**")
    str_app.markdown(f"💡 **Qajeelfama:** {hint}")

    # Giraamarri gTTS fayyadamuun sagalee Afaan Oromootiin suuta qopheessuu
    try:
        tts = gTTS(text=target_word, lang='om', slow=True)
        audio_file = f"temp_audio_{idx}.mp3"
        tts.save(audio_file)
        str_app.audio(audio_file, format='audio/mp3')
    except Exception as e:
        str_app.error(f"Sagaleen uumamuu hin danda'amne: {e}")

    user_typed_word = str_app.text_input("Jecha sagaleen jedhame asitti barreessi:", key=f"aud_input_{student}_{idx}")

    attempt_key = ("audio", student, idx)
    if attempt_key not in str_app.session_state.attempts:
        str_app.session_state.attempts[attempt_key] = 0

    current_attempts = str_app.session_state.attempts[attempt_key]
    str_app.write(f"⚠️ Carraa yaalii: **{current_attempts} / 3**")

    if str_app.button("Mirkaneessi Jecha Sagalee"):
        if current_attempts < 3:
            str_app.session_state.attempts[attempt_key] += 1
            is_correct = False
            if user_typed_word and user_typed_word.strip().lower() == target_word.lower():
                is_correct = True

            if is_correct:
                str_app.session_state.aud_score += 10
                str_app.success("🎉 Sirriidha! Baayyee bareedduu barreessite.")
                str_app.session_state.attempts[attempt_key] = 3
            else:
                rem = 3 - str_app.session_state.attempts[attempt_key]
                if rem > 0:
                    str_app.warning(f"❌ Dogoggora! Carraan hafe: {rem}")
                else:
                    str_app.error(f"❌ Carraan xumurameera. Jechi sirrii: '{target_word}' ture.")
        else:
            str_app.info("Carraan gaaffii kanaa xumurameera.")

    str_app.markdown("---")
    b1, b2 = str_app.columns(2)
    with b1:
        if idx > 0 and str_app.button("⬅️ Duubatti", key="aud_prev"):
            str_app.session_state.aud_index -= 1
            str_app.rerun()
    with b2:
        if idx < len(dict_list) - 1:
            if str_app.button("Fuuldharatti ➡️", key="aud_next"):
                str_app.session_state.aud_index += 1
                str_app.rerun()
        else:
            if str_app.button("Xumuruu & Galchuu", key="aud_finish"):
                str_app.session_state.global_students[student]["audioDictation"] = str_app.session_state.aud_score
                str_app.success(f"Qabxii Qormaata Sagalee: {str_app.session_state.aud_score}")
                str_app.session_state.aud_index = 0
                str_app.session_state.aud_score = 0
                str_app.session_state.current_page = "home"
                str_app.rerun()


def teacher_dashboard_screen():
    if not str_app.session_state.teacher_auth:
        str_app.warning("Maaloo dura paasworii galchaa!")
        str_app.session_state.current_page = "teacher_login"
        str_app.rerun()
        return

    str_app.subheader("🎓 Gabaasa Barsiisaa & Kuusaa Gaaffii (Teacher Dashboard)")
    
    tab1, tab2, tab3 = str_app.tabs([
        "📊 Qabxii & Gabaasa Qinda'aa (Reports)", 
        "🔒 Kuusaa Gaaffii Haquu & Ilaaluu (Manage Banks)", 
        "➕ Gaaffii Haaraa Dabaluu (Add Question)"
    ])

    with tab1:
        str_app.markdown("**Gabaasa Yeroo, Madaallii fi Tarreeffama Barattootaa**")
        students = str_app.session_state.global_students
        str_app.write(f"**Baay'inni barattoota galmaa'an:** {len(students)}")

        if not students:
            str_app.info("Ammaaf barataan galmaa'e hin jiru.")
        else:
            max_subject_score = 30  # Gosa barnootaa tokkoon tokkoon isaaniif gaaffii 6 * 5 = 30
            max_total_score = 90

            subjects_map = {
                "afaanOromoo": "📖 Afaan Oromoo",
                "math": "🔢 Herrega (Mathematics)",
                "english": "🔤 Ingliffaa (English)"
            }

            table_data = []
            csv_data = "Maqaa Barataa,Kutaa,Korniyaa,Lakk Daree,Afaan Oromoo,Herrega,Ingliffaa,Qormaata Sagalee,Waliigala,Parsantii (%)\n"

            for name, data in students.items():
                ao = data["afaanOromoo"]
                math = data["math"]
                eng = data["english"]
                aud = data["audioDictation"]
                total = ao + math + eng
                percentage = (total / max_total_score) * 100

                table_data.append({
                    "Maqaa Barataa": name,
                    "Kutaa": data["grade"],
                    "Korniyaa": data["gender"],
                    "Lakk. Daree": data["section"],
                    "Afaan Oromoo": f"{ao}/30",
                    "Herrega": f"{math}/30",
                    "Ingliffaa": f"{eng}/30",
                    "Q. Sagalee": f"{aud} pts",
                    "Waliigala": f"{total}/90",
                    "Parsantii (%)": f"{percentage:.1f}%",
                })

                csv_data += f"{name},{data['grade']},{data['gender']},{data['section']},{ao},{math},{eng},{aud},{total},{percentage:.1f}%\n"

            str_app.markdown("### 📋 Cuunfaa Waliigala Barattootaa Hunda")
            str_app.dataframe(table_data, use_container_width=True)
            str_app.download_button(
                label="📥 Download Excel Report (CSV)",
                data=csv_data,
                file_name="HiikaWay_Student_Report.csv",
                mime="text/csv",
            )

            str_app.markdown("---")
            str_app.markdown("### 📌 Gabaasa Qinda'aa fi Yaada Madaallii (Gosa Barnootaan)")

            for subj_key, subj_title in subjects_map.items():
                str_app.markdown(f"#### ❖ {subj_title}")
                
                sirritti_list = []
                foyyee_list = []
                hubanne_list = []

                for name, data in students.items():
                    subj_score = data[subj_key]
                    subj_pct = (subj_score / max_subject_score) * 100

                    if subj_pct >= 80:
                        eval_msg = "Sirritti deebiseera (80%-100%)"
                        sirritti_list.append({"Maqaa": name, "Kutaa": data["grade"], "Daree": data["section"], "Qabxii": f"{subj_score}/30", "Madaallii": eval_msg})
                    elif subj_pct >= 60:
                        eval_msg = "Foyyee qaba (60%-79.9%)"
                        foyyee_list.append({"Maqaa": name, "Kutaa": data["grade"], "Daree": data["section"], "Qabxii": f"{subj_score}/30", "Madaallii": eval_msg})
                    else:
                        eval_msg = "Hin hubanne (<59.9%)"
                        hubanne_list.append({"Maqaa": name, "Kutaa": data["grade"], "Daree": data["section"], "Qabxii": f"{subj_score}/30", "Madaallii": eval_msg})

                col_a, col_b, col_c = str_app.columns(3)
                with col_a:
                    str_app.markdown("**🟢 Sirritti Deebisan (80%-100%)**")
                    if sirritti_list:
                        str_app.dataframe(sirritti_list, use_container_width=True)
                    else:
                        str_app.info("Barataan hin jiru.")

                with col_b:
                    str_app.markdown("**🟡 Foyyee Qaban (60%-79.9%)**")
                    if foyyee_list:
                        str_app.dataframe(foyyee_list, use_container_width=True)
                    else:
                        str_app.info("Barataan hin jiru.")

                with col_c:
                    str_app.markdown("**🔴 Hin Hubanne (<59.9%)**")
                    if hubanne_list:
                        str_app.dataframe(hubanne_list, use_container_width=True)
                    else:
                        str_app.info("Barataan hin jiru.")

                str_app.markdown("---")

    with tab2:
        str_app.markdown("### 🔒 Kuusaa Gaaffii Ilaaluu fi Haquu (View & Delete Questions)")
        str_app.write("As irratti gaaffiwwan kuusaa keessa jiran ilaaluun gaaffii hin barbaachisne haquu (delete) ni dandeessa:")

        bank_type_view = str_app.radio(
            "Gosa Kuusaa Filadhu:",
            ["📝 Gaaffilee MCQ (Afaan Oromoo / Herrega / Ingliffaa)", "🔊 Jechoota Qormaata Sagalee (Audio Dictation)"],
            key="manage_bank_type",
            horizontal=True,
        )

        if bank_type_view.startswith("📝"):
            selected_secret_grade = str_app.selectbox("Kutaa Filadhu (Manage Banks)", list(str_app.session_state.SECRET_MASTER_QUESTION_BANKS.keys()), key="del_grade")
            grade_banks = str_app.session_state.SECRET_MASTER_QUESTION_BANKS[selected_secret_grade]

            for subject_name, q_list in grade_banks.items():
                str_app.markdown(f"#### 📖 Gosa Barnootaa: {subject_name.upper()}")
                for i, q_item in enumerate(q_list[:], 0):
                    col_q1, col_q2 = str_app.columns([4, 1])
                    with col_q1:
                        str_app.markdown(f"**Gaaffii {i+1}:** {q_item.get('question')}")
                        str_app.write(f"Filannoo: {q_item.get('options', [])} | **Deebii:** {q_item.get('answer')}")
                        if q_item.get("image"):
                            str_app.image(q_item["image"], width=160)
                    with col_q2:
                        delete_btn_key = f"del_{selected_secret_grade}_{subject_name}_{i}"
                        if str_app.button("🗑️ Haqi", key=delete_btn_key):
                            str_app.session_state.SECRET_MASTER_QUESTION_BANKS[selected_secret_grade][subject_name].pop(i)
                            str_app.success("Gaaffiin milkaa'inaan haqameera!")
                            str_app.rerun()
                    str_app.markdown("---")
        else:
            selected_audio_grade = str_app.selectbox("Kutaa Filadhu (Audio Bank)", list(str_app.session_state.SECRET_AUDIO_DICTATION_BANKS.keys()), key="del_audio_grade")
            audio_list = str_app.session_state.SECRET_AUDIO_DICTATION_BANKS[selected_audio_grade]

            str_app.markdown(f"#### 🔊 Jechoota Qormaata Sagalee - {selected_audio_grade}")
            if not audio_list:
                str_app.info("Ammaaf jechi kutaa kanaaf hin galmoofne.")
            for i, a_item in enumerate(audio_list[:], 0):
                col_a1, col_a2 = str_app.columns([4, 1])
                with col_a1:
                    str_app.markdown(f"**Jecha {i+1}:** `{a_item.get('word')}`")
                    str_app.write(f"Qajeelfama: {a_item.get('hint')}")
                    if a_item.get("image"):
                        str_app.image(a_item["image"], width=160)
                    if a_item.get("audio_bytes"):
                        str_app.audio(a_item["audio_bytes"])
                with col_a2:
                    del_audio_key = f"del_audio_{selected_audio_grade}_{i}"
                    if str_app.button("🗑️ Haqi", key=del_audio_key):
                        str_app.session_state.SECRET_AUDIO_DICTATION_BANKS[selected_audio_grade].pop(i)
                        str_app.success("Jechi sagalee milkaa'inaan haqameera!")
                        str_app.rerun()
                str_app.markdown("---")

    with tab3:
        str_app.markdown("### ➕ Kuusaa Gaaffii Irratti Gaaffii Haaraa Dabaluu")
        str_app.write("Barsiisaan gaaffii haaraa MCQ (fakkii waliin) ykn jecha Qormaata Sagalee (audio + fakkii waliin) kuusaa keessatti dabaluu danda'a.")

        add_bank_type = str_app.radio(
            "Maal Dabaluu Barbaadda?",
            ["📝 Gaaffii MCQ Haaraa (Afaan Oromoo / Herrega / Ingliffaa)", "🔊 Jecha Qormaata Sagalee Haaraa (Audio Dictation)"],
            key="add_bank_type",
            horizontal=True,
        )

        if add_bank_type.startswith("📝"):
            add_grade = str_app.selectbox("Kutaa Filadhu", list(str_app.session_state.SECRET_MASTER_QUESTION_BANKS.keys()), key="add_q_grade")
            add_subject = str_app.selectbox("Gosa Barnootaa Filadhu", ["afaan_oromoo", "math", "english"], key="add_q_subject")

            new_q_text = str_app.text_area("Gaaffii Barreessi:", placeholder="Fkn: Qubee...?")

            opt_a = str_app.text_input("Filannoo A", value="A) ")
            opt_b = str_app.text_input("Filannoo B", value="B) ")
            opt_c = str_app.text_input("Filannoo C", value="C) ")
            opt_d = str_app.text_input("Filannoo D", value="D) ")

            new_answer = str_app.selectbox("Deebii Sirrii (Furtuu)", ["A", "B", "C", "D"])

            str_app.markdown("**🖼️ Fakkii Gaaffichaa (Filannoo - Optional)**")
            img_mode = str_app.radio(
                "Fakkii Akkamiin Dabalta?",
                ["Fakkii Hin Dabalu", "URL Fakkii Galchi", "Fakkii Kompiyutera Irraa Fe'i (Upload)"],
                key="add_q_img_mode",
                horizontal=True,
            )
            new_q_image = None
            if img_mode == "URL Fakkii Galchi":
                img_url = str_app.text_input("URL Fakkii (https://...)", key="add_q_img_url")
                if img_url.strip():
                    new_q_image = img_url.strip()
            elif img_mode == "Fakkii Kompiyutera Irraa Fe'i (Upload)":
                uploaded_img = str_app.file_uploader("Fakkii Filadhu", type=["png", "jpg", "jpeg"], key="add_q_img_upload")
                if uploaded_img is not None:
                    new_q_image = uploaded_img.getvalue()
                    str_app.image(new_q_image, width=200, caption="Fakkii Filatame (Preview)")

            if str_app.button("💾 Gaaffii Kuusaatti Dabali"):
                if new_q_text.strip():
                    new_question_dict = {
                        "question": new_q_text.strip(),
                        "options": [opt_a, opt_b, opt_c, opt_d],
                        "answer": new_answer,
                        "type": "mcq"
                    }
                    if new_q_image is not None:
                        new_question_dict["image"] = new_q_image
                    str_app.session_state.SECRET_MASTER_QUESTION_BANKS[add_grade][add_subject].append(new_question_dict)
                    str_app.success("🎉 Gaaffiin haaraan kuusaa keessatti milkaa'inaan dabalamateera!")
                else:
                    str_app.warning("Maaloo gaafficha guututti barreessi!")

        else:
            add_audio_grade = str_app.selectbox("Kutaa Filadhu", list(str_app.session_state.SECRET_AUDIO_DICTATION_BANKS.keys()), key="add_audio_grade")
            new_word = str_app.text_input("Jecha Haaraa (Word)", placeholder="Fkn: bareedaa", key="add_audio_word")
            new_hint = str_app.text_area("Qajeelfama (Hint)", placeholder="Fkn: Sagalee dhaggeeffadhuu barreessi", key="add_audio_hint")

            str_app.markdown("**🔊 Sagalee Dhugaa Fe'i (Filannoo - Optional)**")
            str_app.caption("Yoo sagalee dhugaa (mp3/wav) hin fe'in, appichi ofumaan sagalee kompiitaraatiin (Text-to-Speech) dubbisa.")
            uploaded_audio = str_app.file_uploader("Sagalee (Audio) Filadhu", type=["mp3", "wav", "ogg", "m4a"], key="add_audio_file")
            new_audio_bytes = uploaded_audio.getvalue() if uploaded_audio is not None else None
            if new_audio_bytes is not None:
                str_app.audio(new_audio_bytes)

            str_app.markdown("**🖼️ Fakkii Wal-simuu Jechichaa (Filannoo - Optional)**")
            audio_img_mode = str_app.radio(
                "Fakkii Akkamiin Dabalta?",
                ["Fakkii Hin Dabalu", "URL Fakkii Galchi", "Fakkii Kompiyutera Irraa Fe'i (Upload)"],
                key="add_audio_img_mode",
                horizontal=True,
            )
            new_audio_image = None
            if audio_img_mode == "URL Fakkii Galchi":
                audio_img_url = str_app.text_input("URL Fakkii (https://...)", key="add_audio_img_url")
                if audio_img_url.strip():
                    new_audio_image = audio_img_url.strip()
            elif audio_img_mode == "Fakkii Kompiyutera Irraa Fe'i (Upload)":
                uploaded_audio_img = str_app.file_uploader("Fakkii Filadhu", type=["png", "jpg", "jpeg"], key="add_audio_img_upload")
                if uploaded_audio_img is not None:
                    new_audio_image = uploaded_audio_img.getvalue()
                    str_app.image(new_audio_image, width=200, caption="Fakkii Filatame (Preview)")

            if str_app.button("💾 Jecha Sagalee Kuusaatti Dabali"):
                if new_word.strip() and new_hint.strip():
                    new_audio_dict = {
                        "word": new_word.strip(),
                        "hint": new_hint.strip(),
                    }
                    if new_audio_image is not None:
                        new_audio_dict["image"] = new_audio_image
                    if new_audio_bytes is not None:
                        new_audio_dict["audio_bytes"] = new_audio_bytes
                    str_app.session_state.SECRET_AUDIO_DICTATION_BANKS[add_audio_grade].append(new_audio_dict)
                    str_app.success("🎉 Jechi Qormaata Sagalee haaraan milkaa'inaan dabalamateera!")
                else:
                    str_app.warning("Maaloo Jecha fi Qajeelfama guutuu galchi!")

    str_app.write("")
    if str_app.button("⬅️ Gara Furtuu Hojii Deebi'i"):
        str_app.session_state.teacher_auth = False
        str_app.session_state.current_page = "role_selection"
        str_app.rerun()


# ROUTE CONTROLLER
if str_app.session_state.current_page == "role_selection":
    role_selection_screen()
elif str_app.session_state.current_page == "teacher_login":
    teacher_login_screen()
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
elif str_app.session_state.current_page == "audio_dictation":
    audio_dictation_screen()
elif str_app.session_state.current_page == "teacher_dashboard":
    teacher_dashboard_screen()
