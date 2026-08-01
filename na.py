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
if "teacher_auth" not in str_app.session_state:
    str_app.session_state.teacher_auth = False

# MASTER QUESTION BANK KAJFA (SESSION STATE KEESSATTI QABAMUU ISAA KAN FAYYADAMU GAAFII HAARAA ITTI DABALUUF)
if "SECRET_MASTER_QUESTION_BANKS" not in str_app.session_state:
    str_app.session_state.SECRET_MASTER_QUESTION_BANKS = {
        "Kutaa 1": {
            "afaan_oromoo": [
                {"question": "Qubee jalqabaa qubee Afaan Oromoo maali?", "options": ["A) A", "B) B", "C) C", "D) D"], "answer": "A", "type": "mcq"},
                {"question": "Jecha 'Mama' jedhu keessatti sagaleen irra deddeebi'amu maali?", "options": ["A) M", "B) N", "C) T", "D) S"], "answer": "A", "type": "mcq"},
                {"question": "Bishaan dhuguuf maal fayyadamna?", "options": ["A) Xurii", "B) Xiyyaara", "C) Xuuftuu", "D) Qodaa"], "answer": "D", "type": "mcq"},
                {"question": "Jecha 'Haadha' jedhu keessaa qubee jalqabaa filadhu:", "options": ["A) H", "B) B", "C) K", "D) L"], "answer": "A", "type": "mcq"},
                {"question": "Mana barumsaa maaliif deemna?", "options": ["A) Barachuuf", "B) Rafuuf", "C) Taphachuuf qofa", "D) Maseenuuf"], "answer": "A", "type": "mcq"},
                {"question": "Qubee 'B'n jecha kam jalqaba?", "options": ["A) Balleessaa", "B) Adaamaa", "C) Caalaa", "D) Dhagaa"], "answer": "A", "type": "mcq"}
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
    c2.markdown(f"**Qabxii: {str_app.session_state.ao_score}**")

    str_app.markdown(f"### {q.get('question', '')}")
    user_answer = None
    if q.get("type", "mcq") == "mcq" and "options" in q:
        user_answer = str_app.radio(
            "Filannoo kee filadhu:", q["options"], key=f"ao_radio_{student}_{idx}"
        )
    else:
        user_answer = str_app.text_input("Deebii kee asitti barreessi:", key=f"ao_ans_{student}_{idx}")

    if str_app.button("Deebii Mirkaneessi", key=f"ao_btn_{student}_{idx}"):
        correct = q.get("answer", "")
        if user_answer and user_answer.startswith(correct):
            str_app.success("🎉 Sirrii dha!")
            str_app.session_state.ao_score += 1
        else:
            str_app.error(f"❌ Dogoggora! Deebiin sirrii: {correct}")
        
        str_app.session_state.ao_index += 1
        str_app.rerun()


# Page Routing Logic
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
