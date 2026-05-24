# # from dotenv import load_dotenv
# # import streamlit as st

# # from utils.audio_processor import process_input
# # from core.transcriber import transcribe_all
# # from core.summarizer import summarize, generate_title
# # from core.extractor import (
# #     extract_action_items,
# #     extract_key_decisions,
# #     extract_questions
# # )
# # from core.rag_engine import build_rag_chain, ask_question

# # # Load environment variables
# # load_dotenv()

# # # Streamlit Page Config
# # st.set_page_config(
# #     page_title="AI Video Assistant",
# #     layout="wide"
# # )

# # st.title("🎥 AI Video Assistant")
# # st.write("Upload YouTube URL or Local Video Path")

# # # User Inputs
# # source = st.text_input("Enter YouTube URL or Local File Path")

# # language = st.selectbox(
# #     "Select Language",
# #     ["english", "hinglish"]
# # )

# # # Main Pipeline Function
# # def run_pipeline(source: str, language: str = "english") -> dict:

# #     st.info("Starting AI Video Assistant Pipeline...")

# #     # Step 1: Audio Processing
# #     chunks = process_input(source)

# #     # Step 2: Transcription
# #     transcript = transcribe_all(chunks, language)

# #     # Step 3: Generate Title
# #     title = generate_title(transcript)

# #     # Step 4: Generate Summary
# #     summary = summarize(transcript)

# #     # Step 5: Extract Insights
# #     action_items = extract_action_items(transcript)

# #     decisions = extract_key_decisions(transcript)

# #     questions = extract_questions(transcript)

# #     # Step 6: Build RAG Chain
# #     rag_chain = build_rag_chain(transcript)

# #     return {
# #         "title": title,
# #         "transcript": transcript,
# #         "summary": summary,
# #         "action_items": action_items,
# #         "key_decisions": decisions,
# #         "open_questions": questions,
# #         "rag_chain": rag_chain,
# #     }

# # # Process Button
# # if st.button("🚀 Process Video"):

# #     if not source:
# #         st.warning("Please enter a valid YouTube URL or File Path")

# #     else:
# #         with st.spinner("Processing Video..."):

# #             result = run_pipeline(source, language)

# #             st.success("Processing Completed!")

# #             # Display Results
# #             st.subheader("📌 Title")
# #             st.write(result["title"])

# #             st.subheader("📋 Summary")
# #             st.write(result["summary"])

# #             st.subheader("✅ Action Items")
# #             st.write(result["action_items"])

# #             st.subheader("🔑 Key Decisions")
# #             st.write(result["key_decisions"])

# #             st.subheader("❓ Open Questions")
# #             st.write(result["open_questions"])

# #             st.subheader("📝 Transcript")
# #             st.write(result["transcript"])

# #             # Save RAG Chain
# #             st.session_state.rag_chain = result["rag_chain"]

# # # Chat Section
# # if "rag_chain" in st.session_state:

# #     st.subheader("💬 Chat With Your Video")

# #     user_question = st.text_input("Ask Question About Video")

# #     if st.button("Ask"):

# #         if user_question:

# #             answer = ask_question(
# #                 st.session_state.rag_chain,
# #                 user_question
# #             )

# #             st.success(answer)


# # VOXEL AI — Modern Streamlit UI


# from dotenv import load_dotenv
# import streamlit as st

# from utils.audio_processor import process_input
# from core.transcriber import transcribe_all
# from core.summarizer import summarize, generate_title
# from core.extractor import (
#     extract_action_items,
#     extract_key_decisions,
#     extract_questions
# )
# from core.rag_engine import build_rag_chain, ask_question

# # ======================================
# # LOAD ENV
# # ======================================

# load_dotenv()

# # ======================================
# # PAGE CONFIG
# # ======================================

# st.set_page_config(
#     page_title="VOXEL AI",
#     page_icon="🎥",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ======================================
# # CUSTOM CSS
# # ======================================

# st.markdown(
#     """
#     <style>

#     @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;700&display=swap');

#     html, body, [class*="css"] {
#         font-family: 'DM Sans', sans-serif;
#         background-color: #07080f;
#         color: white;
#     }

#     .stApp {
#         background:
#             radial-gradient(circle at top left, rgba(99,102,241,0.20), transparent 25%),
#             radial-gradient(circle at bottom right, rgba(168,85,247,0.20), transparent 25%),
#             #07080f;
#     }

#     section[data-testid="stSidebar"] {
#         background: rgba(13,15,26,0.95);
#         border-right: 1px solid rgba(255,255,255,0.08);
#     }

#     .main-title {
#         font-family: 'Syne', sans-serif;
#         font-size: 3rem;
#         font-weight: 800;
#         color: white;
#         margin-bottom: 0.2rem;
#     }

#     .sub-title {
#         color: #9da3c4;
#         margin-bottom: 2rem;
#     }

#     .glass {
#         background: rgba(13,15,26,0.82);
#         border: 1px solid rgba(255,255,255,0.08);
#         border-radius: 24px;
#         padding: 24px;
#         margin-bottom: 20px;
#         backdrop-filter: blur(16px);
#     }

#     .metric-card {
#         background: rgba(13,15,26,0.82);
#         border: 1px solid rgba(255,255,255,0.08);
#         border-radius: 20px;
#         padding: 20px;
#         text-align: center;
#     }

#     .metric-value {
#         font-size: 2rem;
#         font-weight: 700;
#         color: white;
#     }

#     .metric-label {
#         color: #9da3c4;
#         font-size: 0.9rem;
#     }

#     .section-title {
#         font-family: 'Syne', sans-serif;
#         font-size: 1.3rem;
#         font-weight: 700;
#         margin-bottom: 1rem;
#         color: white;
#     }

#     .summary-box {
#         color: #d1d5db;
#         line-height: 1.8;
#         font-size: 1rem;
#     }

#     .item-box {
#         background: #131628;
#         border-radius: 14px;
#         padding: 12px 14px;
#         margin-bottom: 10px;
#         border: 1px solid rgba(255,255,255,0.05);
#         color: #d1d5db;
#     }

#     .stTextInput input,
#     .stTextArea textarea {
#         background: #0f1120 !important;
#         color: white !important;
#         border: 1px solid rgba(255,255,255,0.08) !important;
#         border-radius: 12px !important;
#     }

#     .stSelectbox div[data-baseweb="select"] {
#         background: #0f1120 !important;
#         border-radius: 12px !important;
#     }

#     .stButton>button {
#         width: 100%;
#         border: none;
#         border-radius: 14px;
#         background: linear-gradient(135deg,#6366f1,#8b5cf6);
#         color: white;
#         padding: 0.8rem 1rem;
#         font-weight: 700;
#         font-size: 1rem;
#     }

#     .stButton>button:hover {
#         opacity: 0.92;
#     }

#     .chat-box {
#         background: #131628;
#         border-radius: 16px;
#         padding: 14px;
#         margin-bottom: 12px;
#     }

#     .user-chat {
#         border-left: 4px solid #6366f1;
#     }

#     .bot-chat {
#         border-left: 4px solid #22c55e;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ======================================
# # SIDEBAR
# # ======================================

# with st.sidebar:

#     st.markdown("## 🎥 VOXEL AI")
#     st.caption("Meeting Intelligence")

#     source = st.text_input(
#         "Meeting Source",
#         placeholder="Paste YouTube URL or audio link"
#     )

#     language = st.selectbox(
#         "Language",
#         ["english", "hinglish"]
#     )

#     run_btn = st.button("🚀 Run Analysis")

# # ======================================
# # PIPELINE
# # ======================================

# def run_pipeline(source: str, language: str = "english"):

#     chunks = process_input(source)

#     transcript = transcribe_all(
#         chunks,
#         language
#     )

#     title = generate_title(transcript)

#     summary = summarize(transcript)

#     action_items = extract_action_items(transcript)

#     decisions = extract_key_decisions(transcript)

#     questions = extract_questions(transcript)

#     rag_chain = build_rag_chain(transcript)

#     return {
#         "title": title,
#         "transcript": transcript,
#         "summary": summary,
#         "action_items": action_items,
#         "key_decisions": decisions,
#         "questions": questions,
#         "rag_chain": rag_chain
#     }

# # ======================================
# # MAIN UI
# # ======================================

# st.markdown(
#     '<div class="main-title">VOXEL AI</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="sub-title">AI Meeting Intelligence Dashboard</div>',
#     unsafe_allow_html=True
# )

# # ======================================
# # PROCESS
# # ======================================

# if run_btn:

#     if not source:

#         st.warning(
#             "Please enter valid source"
#         )

#     else:

#         with st.spinner("Processing Meeting..."):

#             result = run_pipeline(
#                 source,
#                 language
#             )

#             st.session_state.result = result

#             st.session_state.rag_chain = result[
#                 "rag_chain"
#             ]

# # ======================================
# # SHOW RESULTS
# # ======================================

# if "result" in st.session_state:

#     result = st.session_state.result

#     # ================================
#     # TITLE
#     # ================================

#     st.markdown(
#         f"## {result['title']}"
#     )

#     # ================================
#     # METRICS
#     # ================================

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         st.markdown(
#             f'''
#             <div class="metric-card">
#                 <div class="metric-value">{len(result['action_items'])}</div>
#                 <div class="metric-label">Action Items</div>
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     with c2:
#         st.markdown(
#             f'''
#             <div class="metric-card">
#                 <div class="metric-value">{len(result['key_decisions'])}</div>
#                 <div class="metric-label">Key Decisions</div>
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     with c3:
#         st.markdown(
#             f'''
#             <div class="metric-card">
#                 <div class="metric-value">{len(result['questions'])}</div>
#                 <div class="metric-label">Open Questions</div>
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     # ================================
#     # SUMMARY
#     # ================================

#     st.markdown(
#         '<div class="glass">',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         '<div class="section-title">📋 Executive Summary</div>',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         f'<div class="summary-box">{result["summary"]}</div>',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         '</div>',
#         unsafe_allow_html=True
#     )

#     # ================================
#     # TWO COLUMNS
#     # ================================

#     col1, col2 = st.columns(2)

#     with col1:

#         st.markdown(
#             '<div class="glass">',
#             unsafe_allow_html=True
#         )

#         st.markdown(
#             '<div class="section-title">✅ Action Items</div>',
#             unsafe_allow_html=True
#         )

#         for item in result["action_items"]:
#             st.markdown(
#                 f'<div class="item-box">{item}</div>',
#                 unsafe_allow_html=True
#             )

#         st.markdown(
#             '</div>',
#             unsafe_allow_html=True
#         )

#     with col2:

#         st.markdown(
#             '<div class="glass">',
#             unsafe_allow_html=True
#         )

#         st.markdown(
#             '<div class="section-title">⭐ Key Decisions</div>',
#             unsafe_allow_html=True
#         )

#         for item in result["key_decisions"]:
#             st.markdown(
#                 f'<div class="item-box">{item}</div>',
#                 unsafe_allow_html=True
#             )

#         st.markdown(
#             '</div>',
#             unsafe_allow_html=True
#         )

#     # ================================
#     # QUESTIONS
#     # ================================

#     st.markdown(
#         '<div class="glass">',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         '<div class="section-title">❓ Open Questions</div>',
#         unsafe_allow_html=True
#     )

#     for item in result["questions"]:
#         st.markdown(
#             f'<div class="item-box">{item}</div>',
#             unsafe_allow_html=True
#         )

#     st.markdown(
#         '</div>',
#         unsafe_allow_html=True
#     )

#     # ================================
#     # TRANSCRIPT
#     # ================================

#     st.markdown(
#         '<div class="glass">',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         '<div class="section-title">📝 Transcript</div>',
#         unsafe_allow_html=True
#     )

#     st.text_area(
#         "Transcript",
#         result["transcript"],
#         height=350
#     )

#     st.markdown(
#         '</div>',
#         unsafe_allow_html=True
#     )

# # ======================================
# # CHAT SECTION
# # ======================================

# if "rag_chain" in st.session_state:

#     st.markdown(
#         '<div class="glass">',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         '<div class="section-title">💬 AI Assistant</div>',
#         unsafe_allow_html=True
#     )

#     user_question = st.text_input(
#         "Ask anything about the meeting"
#     )

#     if st.button("Ask AI"):

#         if user_question:

#             answer = ask_question(
#                 st.session_state.rag_chain,
#                 user_question
#             )

#             st.markdown(
#                 f'''
#                 <div class="chat-box user-chat">
#                     <b>You:</b><br>{user_question}
#                 </div>
#                 ''',
#                 unsafe_allow_html=True
#             )

#             st.markdown(
#                 f'''
#                 <div class="chat-box bot-chat">
#                     <b>VOXEL AI:</b><br>{answer}
#                 </div>
#                 ''',
#                 unsafe_allow_html=True
#             )

#     st.markdown(
#         '</div>',
#         unsafe_allow_html=True
#     )




from dotenv import load_dotenv
import streamlit as st

from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions
)
from core.rag_engine import build_rag_chain, ask_question

# =========================
# LOAD ENV
# =========================
load_dotenv()

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="MeetMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
    background:#050816;
    color:white;
}

.stApp{
    background:
    radial-gradient(circle at top left, rgba(99,102,241,0.18), transparent 25%),
    radial-gradient(circle at bottom right, rgba(168,85,247,0.18), transparent 25%),
    #050816;
}

section[data-testid="stSidebar"]{
    background:#070b18;
    border-right:1px solid rgba(255,255,255,0.06);
    padding-top:20px;
}

.main-title{
    font-family:'Syne',sans-serif;
    font-size:4rem;
    font-weight:800;
    color:white;
    margin-bottom:0.3rem;
}

.sub-title{
    color:#94a3b8;
    font-size:1.1rem;
    margin-bottom:2rem;
}

.glass{
    background:rgba(17,24,39,0.72);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:24px;
    padding:24px;
    margin-bottom:22px;
    backdrop-filter:blur(16px);
}

.metric-card{
    background:rgba(17,24,39,0.82);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:22px;
    padding:28px;
    text-align:center;
    transition:0.3s;
}

.metric-card:hover{
    transform:translateY(-5px);
    border:1px solid rgba(99,102,241,0.5);
}

.metric-value{
    font-size:2.7rem;
    font-weight:700;
    color:white;
}

.metric-label{
    color:#94a3b8;
    margin-top:8px;
    font-size:1rem;
}

.section-title{
    font-family:'Syne',sans-serif;
    font-size:1.4rem;
    font-weight:700;
    margin-bottom:1rem;
}

.item-box{
    background:#111827;
    border-radius:16px;
    padding:16px;
    margin-bottom:14px;
    border:1px solid rgba(255,255,255,0.05);
    color:#d1d5db;
    transition:0.3s;
}

.item-box:hover{
    border:1px solid rgba(99,102,241,0.4);
}

.summary-box{
    color:#d1d5db;
    line-height:1.9;
    font-size:1rem;
}

.chat-box{
    background:#111827;
    border-radius:16px;
    padding:16px;
    margin-bottom:14px;
}

.user-chat{
    border-left:4px solid #6366f1;
}

.bot-chat{
    border-left:4px solid #22c55e;
}

.stButton > button{
    width:100%;
    border:none;
    border-radius:14px;
    background:linear-gradient(135deg,#6366f1,#8b5cf6);
    color:white;
    font-weight:700;
    padding:0.9rem 1rem;
    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 24px rgba(99,102,241,0.4);
}

.stTextInput input,
.stTextArea textarea{
    background:#111827 !important;
    color:white !important;
    border-radius:12px !important;
    border:1px solid rgba(255,255,255,0.08) !important;
}

.stSelectbox div[data-baseweb="select"]{
    background:#111827 !important;
    border-radius:12px !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.markdown("""
    <div style="
        padding:22px;
        border-radius:24px;
        background:linear-gradient(
            145deg,
            rgba(99,102,241,0.20),
            rgba(139,92,246,0.12)
        );
        border:1px solid rgba(255,255,255,0.08);
        margin-bottom:25px;
        text-align:center;
    ">

    <h1 style="
        font-size:2rem;
        margin-bottom:5px;
        color:white;
        font-family:Syne;
        font-weight:800;
    ">
    🧠 MeetMind AI
    </h1>

    <p style="
        color:#cbd5e1;
        font-size:0.95rem;
    ">
    Smart AI Meeting Assistant
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎥 Meeting Source")

    source = st.text_input(
        "",
        placeholder="Paste YouTube URL or File Path"
    )

    st.markdown("### 🌐 Language")

    language = st.selectbox(
        "",
        ["english", "hinglish"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    run_btn = st.button("🚀 Run Analysis")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:rgba(17,24,39,0.75);
        border-radius:18px;
        padding:18px;
        border:1px solid rgba(255,255,255,0.06);
    ">

    <h4 style="margin-top:0;color:white;">
    ⚡ Features
    </h4>

    <ul style="
        color:#cbd5e1;
        padding-left:18px;
        line-height:1.9;
    ">
        <li>AI Meeting Summary</li>
        <li>Action Item Detection</li>
        <li>Key Decision Tracking</li>
        <li>Question Extraction</li>
        <li>Meeting Chat Assistant</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

# =========================
# CLEAN OUTPUT
# =========================
def clean_output(data):

    if isinstance(data, list):

        cleaned = []

        for item in data:

            if item and len(item.strip()) > 5:

                invalid_words = [
                    "none",
                    "no action",
                    "no questions",
                    "not mentioned",
                    "n/a",
                    "nothing"
                ]

                if not any(word in item.lower() for word in invalid_words):
                    cleaned.append(item)

        return cleaned

    return []

# =========================
# MAIN PIPELINE
# =========================
def run_pipeline(source, language="english"):

    chunks = process_input(source)

    transcript = transcribe_all(
        chunks,
        language
    )

    title = generate_title(transcript)

    summary = summarize(transcript)

    action_items = clean_output(
        extract_action_items(transcript)
    )

    decisions = clean_output(
        extract_key_decisions(transcript)
    )

    questions = clean_output(
        extract_questions(transcript)
    )

    rag_chain = build_rag_chain(transcript)

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": decisions,
        "questions": questions,
        "rag_chain": rag_chain
    }

# =========================
# HEADER
# =========================
st.markdown(
    '<div class="main-title">MeetMind AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI Powered Meeting Intelligence Dashboard</div>',
    unsafe_allow_html=True
)

# =========================
# RUN ANALYSIS
# =========================
if run_btn:

    if not source:

        st.warning("Please enter valid source")

    else:

        with st.spinner("Processing Meeting..."):

            result = run_pipeline(
                source,
                language
            )

            st.session_state.result = result
            st.session_state.rag_chain = result["rag_chain"]

# =========================
# DISPLAY RESULTS
# =========================
if "result" in st.session_state:

    result = st.session_state.result

    st.markdown(f'## "{result["title"]}"')

    c1, c2, c3 = st.columns(3)

    # Action Items
    with c1:

        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">
                {len(result['action_items'])}
            </div>
            <div class="metric-label">
                Action Items
            </div>
        </div>
        ''', unsafe_allow_html=True)

    # Key Decisions
    with c2:

        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">
                {len(result['key_decisions'])}
            </div>
            <div class="metric-label">
                Key Decisions
            </div>
        </div>
        ''', unsafe_allow_html=True)

    # Open Questions
    with c3:

        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">
                {len(result['questions'])}
            </div>
            <div class="metric-label">
                Open Questions
            </div>
        </div>
        ''', unsafe_allow_html=True)

    # =========================
    # SUMMARY
    # =========================
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📋 Executive Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="summary-box">{result["summary"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # ACTIONS & DECISIONS
    # =========================
    col1, col2 = st.columns(2)

    # Action Items
    with col1:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.markdown(
            '<div class="section-title">✅ Action Items</div>',
            unsafe_allow_html=True
        )

        if result["action_items"]:

            for item in result["action_items"]:

                st.markdown(
                    f'<div class="item-box">{item}</div>',
                    unsafe_allow_html=True
                )

        else:
            st.info("No action items found.")

        st.markdown('</div>', unsafe_allow_html=True)

    # Key Decisions
    with col2:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.markdown(
            '<div class="section-title">⭐ Key Decisions</div>',
            unsafe_allow_html=True
        )

        if result["key_decisions"]:

            for item in result["key_decisions"]:

                st.markdown(
                    f'<div class="item-box">{item}</div>',
                    unsafe_allow_html=True
                )

        else:
            st.info("No key decisions found.")

        st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # QUESTIONS
    # =========================
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">❓ Open Questions</div>',
        unsafe_allow_html=True
    )

    if result["questions"]:

        for item in result["questions"]:

            st.markdown(
                f'<div class="item-box">{item}</div>',
                unsafe_allow_html=True
            )

    else:
        st.info("No open questions found.")

    st.markdown('</div>', unsafe_allow_html=True)

    # =========================
    # TRANSCRIPT
    # =========================
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📝 Transcript</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Transcript",
        result["transcript"],
        height=350
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# AI CHAT ASSISTANT
# =========================
if "rag_chain" in st.session_state:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">💬 AI Assistant</div>',
        unsafe_allow_html=True
    )

    user_question = st.text_input(
        "Ask anything about the meeting"
    )

    if st.button("Ask AI"):

        if user_question:

            answer = ask_question(
                st.session_state.rag_chain,
                user_question
            )

            st.markdown(f'''
            <div class="chat-box user-chat">
                <b>You:</b><br>
                {user_question}
            </div>
            ''', unsafe_allow_html=True)

            st.markdown(f'''
            <div class="chat-box bot-chat">
                <b>MeetMind AI:</b><br>
                {answer}
            </div>
            ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
