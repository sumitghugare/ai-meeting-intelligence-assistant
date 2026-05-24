# import streamlit as st
# import time
# from dotenv import load_dotenv
# from utils.audio_processor import process_input
# from core.transcriber import transcribe_all
# from core.summarizer import summarize, generate_title
# from core.extractor import extract_action_items, extract_key_decisions, extract_questions
# from core.rag_engine import build_rag_chain, ask_question

# load_dotenv()

# # ─── Page Config ────────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="AI Video Assistant",
#     page_icon="🎬",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # ─── Custom CSS ─────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

# /* ── Root Variables ── */
# :root {
#     --bg: #0a0a0f;
#     --surface: #111118;
#     --surface-2: #1a1a25;
#     --border: #2a2a3a;
#     --accent: #7c3aed;
#     --accent-glow: #9f67ff;
#     --accent-2: #06b6d4;
#     --text: #e8e8f0;
#     --text-muted: #7070a0;
#     --success: #10b981;
#     --warning: #f59e0b;
#     --danger: #ef4444;
# }

# /* ── Global Reset ── */
# html, body, [class*="css"] {
#     font-family: 'JetBrains Mono', monospace;
#     background-color: var(--bg) !important;
#     color: var(--text) !important;
# }

# .stApp {
#     background: var(--bg) !important;
# }

# /* Animated grid background */
# .stApp::before {
#     content: '';
#     position: fixed;
#     top: 0; left: 0;
#     width: 100%; height: 100%;
#     background-image:
#         linear-gradient(rgba(124, 58, 237, 0.03) 1px, transparent 1px),
#         linear-gradient(90deg, rgba(124, 58, 237, 0.03) 1px, transparent 1px);
#     background-size: 40px 40px;
#     pointer-events: none;
#     z-index: 0;
# }

# /* ── Sidebar ── */
# [data-testid="stSidebar"] {
#     background: var(--surface) !important;
#     border-right: 1px solid var(--border) !important;
# }

# [data-testid="stSidebar"] * {
#     color: var(--text) !important;
# }

# /* ── Headings ── */
# h1, h2, h3, h4, h5, h6 {
#     font-family: 'Syne', sans-serif !important;
#     color: var(--text) !important;
# }

# /* ── Hero Title ── */
# .hero-title {
#     font-family: 'Syne', sans-serif;
#     font-size: clamp(2rem, 5vw, 3.5rem);
#     font-weight: 800;
#     line-height: 1.1;
#     margin: 0;
#     background: linear-gradient(135deg, #ffffff 0%, var(--accent-glow) 50%, var(--accent-2) 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
# }

# .hero-sub {
#     font-family: 'JetBrains Mono', monospace;
#     font-size: 0.8rem;
#     color: var(--text-muted);
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     margin-top: 0.5rem;
# }

# /* ── Cards ── */
# .card {
#     background: var(--surface);
#     border: 1px solid var(--border);
#     border-radius: 12px;
#     padding: 1.5rem;
#     margin-bottom: 1rem;
#     position: relative;
#     overflow: hidden;
#     transition: border-color 0.2s;
# }

# .card:hover {
#     border-color: var(--accent);
# }

# .card::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 0;
#     width: 3px; height: 100%;
#     background: linear-gradient(180deg, var(--accent), var(--accent-2));
# }

# .card-title {
#     font-family: 'Syne', sans-serif;
#     font-size: 0.7rem;
#     font-weight: 700;
#     letter-spacing: 0.15em;
#     text-transform: uppercase;
#     color: var(--text-muted);
#     margin-bottom: 0.75rem;
#     display: flex;
#     align-items: center;
#     gap: 0.5rem;
# }

# .card-content {
#     font-size: 0.875rem;
#     line-height: 1.7;
#     color: var(--text);
# }

# /* ── Accent Badge ── */
# .badge {
#     display: inline-block;
#     padding: 0.2rem 0.6rem;
#     border-radius: 4px;
#     font-size: 0.65rem;
#     font-weight: 600;
#     letter-spacing: 0.1em;
#     text-transform: uppercase;
# }

# .badge-purple { background: rgba(124,58,237,0.2); color: var(--accent-glow); border: 1px solid rgba(124,58,237,0.3); }
# .badge-cyan   { background: rgba(6,182,212,0.15); color: var(--accent-2);    border: 1px solid rgba(6,182,212,0.3); }
# .badge-green  { background: rgba(16,185,129,0.15); color: var(--success);    border: 1px solid rgba(16,185,129,0.3); }

# /* ── Input & Buttons ── */
# .stTextInput > div > div > input,
# .stSelectbox > div > div {
#     background: var(--surface-2) !important;
#     border: 1px solid var(--border) !important;
#     border-radius: 8px !important;
#     color: var(--text) !important;
#     font-family: 'JetBrains Mono', monospace !important;
# }

# .stTextInput > div > div > input:focus {
#     border-color: var(--accent) !important;
#     box-shadow: 0 0 0 2px rgba(124,58,237,0.2) !important;
# }

# .stButton > button {
#     background: linear-gradient(135deg, var(--accent), #5b21b6) !important;
#     color: white !important;
#     border: none !important;
#     border-radius: 8px !important;
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 0.875rem !important;
#     letter-spacing: 0.05em !important;
#     padding: 0.6rem 1.5rem !important;
#     transition: all 0.2s !important;
#     text-transform: uppercase !important;
# }

# .stButton > button:hover {
#     transform: translateY(-1px) !important;
#     box-shadow: 0 8px 25px rgba(124,58,237,0.4) !important;
# }

# /* Secondary button */
# .stButton > button[kind="secondary"] {
#     background: var(--surface-2) !important;
#     border: 1px solid var(--border) !important;
# }

# /* ── Progress / Status ── */
# .status-bar {
#     display: flex;
#     align-items: center;
#     gap: 0.75rem;
#     padding: 0.75rem 1rem;
#     background: var(--surface-2);
#     border-radius: 8px;
#     margin: 0.4rem 0;
#     border: 1px solid var(--border);
#     font-size: 0.8rem;
# }

# .status-dot {
#     width: 8px; height: 8px;
#     border-radius: 50%;
#     flex-shrink: 0;
# }

# .dot-active   { background: var(--accent-glow); box-shadow: 0 0 8px var(--accent-glow); animation: pulse 1.5s infinite; }
# .dot-done     { background: var(--success); }
# .dot-pending  { background: var(--border); }

# @keyframes pulse {
#     0%, 100% { opacity: 1; }
#     50%       { opacity: 0.4; }
# }

# /* ── Chat ── */
# .chat-container {
#     background: var(--surface);
#     border: 1px solid var(--border);
#     border-radius: 12px;
#     padding: 1.25rem;
#     max-height: 420px;
#     overflow-y: auto;
#     margin-bottom: 1rem;
# }

# .chat-msg {
#     margin-bottom: 1rem;
#     display: flex;
#     flex-direction: column;
#     gap: 0.2rem;
# }

# .chat-label {
#     font-size: 0.65rem;
#     font-weight: 700;
#     letter-spacing: 0.15em;
#     text-transform: uppercase;
# }

# .chat-bubble {
#     display: inline-block;
#     padding: 0.6rem 1rem;
#     border-radius: 10px;
#     font-size: 0.85rem;
#     line-height: 1.6;
#     max-width: 90%;
# }

# .user-label  { color: var(--accent-glow); }
# .bot-label   { color: var(--accent-2); }

# .user-bubble { background: rgba(124,58,237,0.15); border: 1px solid rgba(124,58,237,0.25); align-self: flex-end; }
# .bot-bubble  { background: rgba(6,182,212,0.1);  border: 1px solid rgba(6,182,212,0.2);   align-self: flex-start; }

# /* ── Divider ── */
# hr {
#     border: none !important;
#     border-top: 1px solid var(--border) !important;
#     margin: 1.5rem 0 !important;
# }

# /* ── Transcript box ── */
# .transcript-box {
#     background: var(--surface-2);
#     border: 1px solid var(--border);
#     border-radius: 8px;
#     padding: 1.25rem;
#     font-size: 0.82rem;
#     line-height: 1.8;
#     max-height: 300px;
#     overflow-y: auto;
#     color: var(--text-muted);
#     white-space: pre-wrap;
#     word-break: break-word;
# }

# /* ── Stale Streamlit elements ── */
# .stProgress > div > div > div { background: var(--accent) !important; }
# .stSpinner > div { border-top-color: var(--accent) !important; }
# [data-testid="stMarkdownContainer"] p { color: var(--text) !important; }
# label { color: var(--text-muted) !important; font-size: 0.8rem !important; }

# /* scrollbar */
# ::-webkit-scrollbar { width: 5px; height: 5px; }
# ::-webkit-scrollbar-track { background: var(--bg); }
# ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
# ::-webkit-scrollbar-thumb:hover { background: var(--accent); }
# </style>
# """, unsafe_allow_html=True)

# # ─── Session State Init ──────────────────────────────────────────────────────────
# for key, default in {
#     "result": None,
#     "chat_history": [],
#     "processing": False,
#     "pipeline_done": False,
#     "pipeline_steps": {},
# }.items():
#     if key not in st.session_state:
#         st.session_state[key] = default

# # ─── Helpers ────────────────────────────────────────────────────────────────────
# def step_status(steps: dict, key: str) -> str:
#     s = steps.get(key, "pending")
#     if s == "active":  return "dot-active"
#     if s == "done":    return "dot-done"
#     return "dot-pending"

# def render_step_bar(label: str, key: str, icon: str):
#     css = step_status(st.session_state.pipeline_steps, key)
#     st.markdown(f"""
#     <div class="status-bar">
#         <div class="status-dot {css}"></div>
#         <span>{icon} {label}</span>
#     </div>""", unsafe_allow_html=True)

# # ─── Sidebar ────────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown('<div class="hero-title" style="font-size:1.6rem">🎬 AI<br>Video</div>', unsafe_allow_html=True)
#     st.markdown('<div class="hero-sub">Meeting Intelligence</div>', unsafe_allow_html=True)
#     st.markdown("---")

#     st.markdown('<span class="badge badge-purple">Input</span>', unsafe_allow_html=True)
#     source = st.text_input("YouTube URL or File Path", placeholder="https://youtube.com/watch?v=... or /path/to/file.mp4")

#     language = st.selectbox("Language", ["english", "hinglish"], index=0)

#     run_btn = st.button("⚡  Analyse", use_container_width=True)

#     if st.session_state.pipeline_done:
#         st.markdown("---")
#         st.markdown('<span class="badge badge-green">Pipeline Status</span>', unsafe_allow_html=True)
#         for step, icon, label in [
#             ("audio",      "🔊", "Audio Processing"),
#             ("transcript", "📝", "Transcription"),
#             ("title",      "🏷️", "Title Generation"),
#             ("summary",    "📋", "Summarisation"),
#             ("extract",    "🔍", "Extraction"),
#             ("rag",        "🧠", "RAG Engine"),
#         ]:
#             render_step_bar(label, step, icon)

# # ─── Main Area ──────────────────────────────────────────────────────────────────
# st.markdown('<div class="hero-title">AI Video Assistant</div>', unsafe_allow_html=True)
# st.markdown('<div class="hero-sub">Transcribe · Summarise · Chat with your meetings</div>', unsafe_allow_html=True)
# st.markdown("---")

# # ── Run Pipeline ────────────────────────────────────────────────────────────────
# if run_btn:
#     if not source.strip():
#         st.error("Please enter a YouTube URL or file path.")
#     else:
#         st.session_state.pipeline_done = False
#         st.session_state.result = None
#         st.session_state.chat_history = []
#         st.session_state.pipeline_steps = {}

#         progress_placeholder = st.empty()

#         def update_step(key, state):
#             st.session_state.pipeline_steps[key] = state

#         try:
#             with progress_placeholder.container():
#                 st.info("⚙️ Pipeline running — see sidebar for live status…")

#             update_step("audio", "active")
#             chunks = process_input(source)
#             update_step("audio", "done")

#             update_step("transcript", "active")
#             transcript = transcribe_all(chunks, language)
#             update_step("transcript", "done")

#             update_step("title", "active")
#             title = generate_title(transcript)
#             update_step("title", "done")

#             update_step("summary", "active")
#             summary = summarize(transcript)
#             update_step("summary", "done")

#             update_step("extract", "active")
#             action_items  = extract_action_items(transcript)
#             decisions     = extract_key_decisions(transcript)
#             questions     = extract_questions(transcript)
#             update_step("extract", "done")

#             update_step("rag", "active")
#             rag_chain = build_rag_chain(transcript)
#             update_step("rag", "done")

#             st.session_state.result = {
#                 "title": title,
#                 "transcript": transcript,
#                 "summary": summary,
#                 "action_items": action_items,
#                 "key_decisions": decisions,
#                 "open_questions": questions,
#                 "rag_chain": rag_chain,
#             }
#             st.session_state.pipeline_done = True
#             progress_placeholder.success("✅ Analysis complete!")
#             time.sleep(0.5)
#             progress_placeholder.empty()
#             st.rerun()

#         except Exception as e:
#             for k in ["audio","transcript","title","summary","extract","rag"]:
#                 if st.session_state.pipeline_steps.get(k) == "active":
#                     st.session_state.pipeline_steps[k] = "pending"
#             progress_placeholder.error(f"❌ Error: {e}")

# # ── Results ──────────────────────────────────────────────────────────────────────
# if st.session_state.result:
#     r = st.session_state.result

#     # Title banner
#     st.markdown(f"""
#     <div class="card">
#         <div class="card-title">📌 Session Title</div>
#         <div style="font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:700;color:var(--text)">
#             {r['title']}
#         </div>
#     </div>""", unsafe_allow_html=True)

#     # Top row: summary + transcript
#     col1, col2 = st.columns([3, 2], gap="medium")

#     with col1:
#         st.markdown(f"""
#         <div class="card">
#             <div class="card-title">📋 Summary</div>
#             <div class="card-content">{r['summary']}</div>
#         </div>""", unsafe_allow_html=True)

#     with col2:
#         with st.expander("📝 Full Transcript", expanded=False):
#             st.markdown(f'<div class="transcript-box">{r["transcript"]}</div>', unsafe_allow_html=True)

#     # Second row: action items | decisions | questions
#     c1, c2, c3 = st.columns(3, gap="medium")

#     with c1:
#         st.markdown(f"""
#         <div class="card">
#             <div class="card-title">✅ Action Items</div>
#             <div class="card-content">{r['action_items']}</div>
#         </div>""", unsafe_allow_html=True)

#     with c2:
#         st.markdown(f"""
#         <div class="card">
#             <div class="card-title">🔑 Key Decisions</div>
#             <div class="card-content">{r['key_decisions']}</div>
#         </div>""", unsafe_allow_html=True)

#     with c3:
#         st.markdown(f"""
#         <div class="card">
#             <div class="card-title">❓ Open Questions</div>
#             <div class="card-content">{r['open_questions']}</div>
#         </div>""", unsafe_allow_html=True)

#     st.markdown("---")

#     # ── RAG Chat ──────────────────────────────────────────────────────────────
#     st.markdown('<div style="font-family:\'Syne\',sans-serif;font-size:1.2rem;font-weight:700;margin-bottom:1rem">💬 Chat with your Meeting</div>', unsafe_allow_html=True)

#     # Chat history display
#     if st.session_state.chat_history:
#         chat_html = '<div class="chat-container">'
#         for msg in st.session_state.chat_history:
#             if msg["role"] == "user":
#                 chat_html += f"""
#                 <div class="chat-msg" style="align-items:flex-end">
#                     <span class="chat-label user-label">You</span>
#                     <div class="chat-bubble user-bubble">{msg['content']}</div>
#                 </div>"""
#             else:
#                 chat_html += f"""
#                 <div class="chat-msg" style="align-items:flex-start">
#                     <span class="chat-label bot-label">🤖 Assistant</span>
#                     <div class="chat-bubble bot-bubble">{msg['content']}</div>
#                 </div>"""
#         chat_html += '</div>'
#         st.markdown(chat_html, unsafe_allow_html=True)
#     else:
#         st.markdown("""
#         <div class="card" style="text-align:center;padding:2rem">
#             <div style="font-size:2rem;margin-bottom:0.5rem">💬</div>
#             <div style="color:var(--text-muted);font-size:0.85rem">Ask anything about your meeting transcript</div>
#         </div>""", unsafe_allow_html=True)

#     # Chat input
#     chat_col1, chat_col2 = st.columns([5, 1], gap="small")
#     with chat_col1:
#         user_input = st.text_input("Your question", placeholder="What were the main decisions made?", label_visibility="collapsed")
#     with chat_col2:
#         send_btn = st.button("Send →", use_container_width=True)

#     if send_btn and user_input.strip():
#         with st.spinner("Thinking…"):
#             answer = ask_question(r["rag_chain"], user_input.strip())
#         st.session_state.chat_history.append({"role": "user",      "content": user_input.strip()})
#         st.session_state.chat_history.append({"role": "assistant", "content": answer})
#         st.rerun()

#     if st.session_state.chat_history:
#         if st.button("🗑️ Clear Chat", type="secondary"):
#             st.session_state.chat_history = []
#             st.rerun()

# else:
#     # Empty state
#     st.markdown("""
#     <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding:5rem 2rem;text-align:center">
#         <div style="font-size:4rem;margin-bottom:1rem">🎬</div>
#         <div style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;color:var(--text);margin-bottom:0.5rem">
#             Ready to Analyse
#         </div>
#         <div style="color:var(--text-muted);font-size:0.85rem;max-width:380px;line-height:1.7">
#             Paste a YouTube URL or local file path in the sidebar, choose your language, and hit <strong>Analyse</strong> to get started.
#         </div>
#         <div style="margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
#             <span class="badge badge-purple">Transcription</span>
#             <span class="badge badge-cyan">Summarisation</span>
#             <span class="badge badge-green">RAG Chat</span>
#         </div>
#     </div>""", unsafe_allow_html=True)

import streamlit as st
import time
from dotenv import load_dotenv
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import extract_action_items, extract_key_decisions, extract_questions
from core.rag_engine import build_rag_chain, ask_question

load_dotenv()

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="VOXEL — AI Meeting Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

/* ══════════════════════════════════════════
   ROOT TOKENS
══════════════════════════════════════════ */
:root {
    --ink:        #08080d;
    --ink-2:      #0f0f18;
    --ink-3:      #16161f;
    --ink-4:      #1e1e2a;
    --line:       #25253a;
    --line-hi:    #38385a;
    --frost:      rgba(255,255,255,0.035);
    --frost-hi:   rgba(255,255,255,0.07);

    --gold:       #e8c96d;
    --gold-dim:   #c4a44a;
    --gold-glow:  rgba(232,201,109,0.15);
    --gold-glow2: rgba(232,201,109,0.06);

    --teal:       #4dd9c0;
    --teal-dim:   #2ab09a;
    --teal-glow:  rgba(77,217,192,0.12);

    --rose:       #f06e8a;
    --rose-glow:  rgba(240,110,138,0.12);

    --slate:      #8888aa;
    --snow:       #f0f0f8;

    --font-display: 'Bebas Neue', sans-serif;
    --font-body:    'DM Sans', sans-serif;
    --font-mono:    'DM Mono', monospace;

    --r-sm: 6px;
    --r-md: 10px;
    --r-lg: 16px;
}

/* ══════════════════════════════════════════
   RESET + BASE
══════════════════════════════════════════ */
html, body, [class*="css"] {
    font-family: var(--font-body) !important;
    background: var(--ink) !important;
    color: var(--snow) !important;
}

.stApp {
    background: var(--ink) !important;
}

/* Layered depth background */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 50% at 10% 0%, rgba(232,201,109,0.04) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 90% 100%, rgba(77,217,192,0.03) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
}

/* Fine grid texture */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.012) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.012) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
    z-index: 0;
}

/* ══════════════════════════════════════════
   SIDEBAR
══════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: var(--ink-2) !important;
    border-right: 1px solid var(--line) !important;
}

[data-testid="stSidebar"] > div {
    padding: 2rem 1.5rem !important;
}

[data-testid="stSidebar"] * {
    color: var(--snow) !important;
}

/* Sidebar brand mark */
.brand-mark {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin-bottom: 2rem;
}

.brand-name {
    font-family: var(--font-display);
    font-size: 3rem;
    line-height: 1;
    letter-spacing: 0.06em;
    background: linear-gradient(135deg, var(--gold) 0%, #fff 60%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.brand-tag {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--slate) !important;
    margin-top: 2px;
    padding-left: 2px;
}

/* Section label */
.sb-section {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--slate) !important;
    margin: 1.5rem 0 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.sb-section::before {
    content: '';
    display: block;
    width: 16px;
    height: 1px;
    background: var(--gold-dim);
}

/* ══════════════════════════════════════════
   INPUTS
══════════════════════════════════════════ */
.stTextInput > div > div > input {
    background: var(--ink-3) !important;
    border: 1px solid var(--line) !important;
    border-radius: var(--r-md) !important;
    color: var(--snow) !important;
    font-family: var(--font-mono) !important;
    font-size: 0.82rem !important;
    padding: 0.65rem 0.9rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}

.stTextInput > div > div > input::placeholder {
    color: var(--slate) !important;
    opacity: 0.7;
}

.stTextInput > div > div > input:focus {
    border-color: var(--gold-dim) !important;
    box-shadow: 0 0 0 3px var(--gold-glow) !important;
    outline: none !important;
}

.stSelectbox > div > div {
    background: var(--ink-3) !important;
    border: 1px solid var(--line) !important;
    border-radius: var(--r-md) !important;
    color: var(--snow) !important;
    font-family: var(--font-mono) !important;
    font-size: 0.82rem !important;
}

label {
    font-family: var(--font-mono) !important;
    font-size: 0.65rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--slate) !important;
}

/* ══════════════════════════════════════════
   BUTTONS
══════════════════════════════════════════ */
.stButton > button {
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dim) 100%) !important;
    color: var(--ink) !important;
    border: none !important;
    border-radius: var(--r-md) !important;
    font-family: var(--font-display) !important;
    font-size: 1rem !important;
    letter-spacing: 0.12em !important;
    padding: 0.55rem 1.5rem !important;
    transition: all 0.25s !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 20px rgba(232,201,109,0.2) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(232,201,109,0.35) !important;
    filter: brightness(1.08) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

.stButton > button[kind="secondary"] {
    background: var(--ink-3) !important;
    color: var(--slate) !important;
    box-shadow: none !important;
    border: 1px solid var(--line) !important;
}

.stButton > button[kind="secondary"]:hover {
    color: var(--snow) !important;
    border-color: var(--line-hi) !important;
    box-shadow: none !important;
}

/* ══════════════════════════════════════════
   PIPELINE STATUS BARS
══════════════════════════════════════════ */
.pipeline-step {
    display: grid;
    grid-template-columns: 28px 1fr auto;
    align-items: center;
    gap: 0.6rem;
    padding: 0.6rem 0.8rem;
    background: var(--frost);
    border-radius: var(--r-sm);
    margin: 3px 0;
    border: 1px solid transparent;
    transition: all 0.3s;
}

.pipeline-step.done   { border-color: rgba(77,217,192,0.2);  background: rgba(77,217,192,0.05); }
.pipeline-step.active { border-color: rgba(232,201,109,0.3); background: rgba(232,201,109,0.06); }

.step-icon {
    width: 26px; height: 26px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem;
    flex-shrink: 0;
}

.step-icon.pending { background: var(--ink-4); color: var(--slate); }
.step-icon.active  { background: rgba(232,201,109,0.2); color: var(--gold); animation: spin-glow 2s ease-in-out infinite; }
.step-icon.done    { background: rgba(77,217,192,0.2); color: var(--teal); }

.step-label {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.04em;
    color: var(--slate);
}

.step-label.active { color: var(--gold); }
.step-label.done   { color: var(--snow); }

.step-state {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 2px 6px;
    border-radius: 3px;
}

.step-state.pending { color: var(--line-hi); }
.step-state.active  { color: var(--gold); background: var(--gold-glow2); }
.step-state.done    { color: var(--teal); }

@keyframes spin-glow {
    0%, 100% { box-shadow: 0 0 0 0 rgba(232,201,109,0); }
    50%       { box-shadow: 0 0 12px 2px rgba(232,201,109,0.3); }
}

/* ══════════════════════════════════════════
   HERO + MASTHEAD
══════════════════════════════════════════ */
.masthead {
    display: flex;
    align-items: flex-end;
    gap: 1.5rem;
    margin-bottom: 0.5rem;
}

.masthead-title {
    font-family: var(--font-display);
    font-size: clamp(3rem, 7vw, 5.5rem);
    line-height: 0.92;
    letter-spacing: 0.04em;
    color: var(--snow);
    margin: 0;
}

.masthead-title span {
    background: linear-gradient(90deg, var(--gold) 0%, var(--teal) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.masthead-sub {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--slate);
    margin-bottom: 0.6rem;
    padding-left: 3px;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, var(--gold-dim) 0%, var(--line) 40%, transparent 100%);
    margin: 1.5rem 0;
}

/* ══════════════════════════════════════════
   RESULT CARDS
══════════════════════════════════════════ */
.panel {
    background: var(--ink-2);
    border: 1px solid var(--line);
    border-radius: var(--r-lg);
    padding: 1.5rem 1.6rem;
    margin-bottom: 0;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, box-shadow 0.25s;
}

.panel:hover {
    border-color: var(--line-hi);
    box-shadow: 0 8px 40px rgba(0,0,0,0.4);
}

/* Gold left accent bar */
.panel.gold::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 2px; height: 100%;
    background: linear-gradient(180deg, var(--gold) 0%, transparent 100%);
}

/* Teal accent */
.panel.teal::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 2px; height: 100%;
    background: linear-gradient(180deg, var(--teal) 0%, transparent 100%);
}

/* Rose accent */
.panel.rose::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 2px; height: 100%;
    background: linear-gradient(180deg, var(--rose) 0%, transparent 100%);
}

.panel-eyebrow {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--slate);
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.panel-eyebrow .dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    flex-shrink: 0;
}

.dot-gold { background: var(--gold); }
.dot-teal { background: var(--teal); }
.dot-rose { background: var(--rose); }

.panel-body {
    font-family: var(--font-body);
    font-size: 0.875rem;
    line-height: 1.75;
    color: #c8c8e0;
    font-weight: 300;
}

/* Session title panel */
.title-panel {
    background: linear-gradient(135deg, var(--ink-2) 0%, var(--ink-3) 100%);
    border: 1px solid var(--line);
    border-radius: var(--r-lg);
    padding: 1.4rem 1.8rem;
    display: flex;
    align-items: center;
    gap: 1.2rem;
    margin-bottom: 1.5rem;
}

.title-glyph {
    font-size: 2rem;
    flex-shrink: 0;
    opacity: 0.8;
}

.title-label {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--gold-dim);
    margin-bottom: 0.3rem;
}

.title-text {
    font-family: var(--font-display);
    font-size: 1.6rem;
    letter-spacing: 0.05em;
    color: var(--snow);
    line-height: 1.1;
}

/* ══════════════════════════════════════════
   TRANSCRIPT EXPANDER
══════════════════════════════════════════ */
[data-testid="stExpander"] {
    background: var(--ink-2) !important;
    border: 1px solid var(--line) !important;
    border-radius: var(--r-lg) !important;
}

[data-testid="stExpander"] summary {
    font-family: var(--font-mono) !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: var(--slate) !important;
    padding: 1rem 1.2rem !important;
}

.transcript-scroll {
    background: var(--ink-3);
    border: 1px solid var(--line);
    border-radius: var(--r-md);
    padding: 1.2rem 1.4rem;
    font-family: var(--font-mono);
    font-size: 0.78rem;
    line-height: 1.9;
    max-height: 320px;
    overflow-y: auto;
    color: var(--slate);
    white-space: pre-wrap;
    word-break: break-word;
    font-weight: 300;
}

/* ══════════════════════════════════════════
   CHAT INTERFACE
══════════════════════════════════════════ */
.chat-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
}

.chat-header-title {
    font-family: var(--font-display);
    font-size: 1.5rem;
    letter-spacing: 0.06em;
    color: var(--snow);
}

.chat-badge {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 3px;
    background: var(--teal-glow);
    color: var(--teal);
    border: 1px solid rgba(77,217,192,0.2);
    margin-bottom: 2px;
}

.chat-viewport {
    background: var(--ink-2);
    border: 1px solid var(--line);
    border-radius: var(--r-lg);
    padding: 1.2rem;
    max-height: 440px;
    overflow-y: auto;
    margin-bottom: 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
}

.msg-row {
    display: flex;
    flex-direction: column;
}

.msg-sender {
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 4px;
    padding: 0 4px;
}

.msg-sender.you { color: var(--gold); text-align: right; }
.msg-sender.bot { color: var(--teal); }

.msg-bubble {
    font-family: var(--font-body);
    font-size: 0.875rem;
    line-height: 1.65;
    padding: 0.75rem 1rem;
    border-radius: 10px;
    max-width: 88%;
    font-weight: 300;
}

.msg-bubble.you {
    background: rgba(232,201,109,0.1);
    border: 1px solid rgba(232,201,109,0.18);
    color: #e8e0c8;
    align-self: flex-end;
    border-bottom-right-radius: 3px;
}

.msg-bubble.bot {
    background: rgba(77,217,192,0.07);
    border: 1px solid rgba(77,217,192,0.15);
    color: #c0e8e0;
    align-self: flex-start;
    border-bottom-left-radius: 3px;
}

.chat-empty {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3rem 2rem;
    gap: 0.75rem;
}

.chat-empty-glyph {
    font-size: 2.5rem;
    opacity: 0.4;
}

.chat-empty-text {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--slate);
}

/* ══════════════════════════════════════════
   CHIPS / BADGES
══════════════════════════════════════════ */
.chip {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    border-radius: 4px;
    font-family: var(--font-mono);
    font-size: 0.62rem;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.chip-gold { background: rgba(232,201,109,0.12); color: var(--gold);  border: 1px solid rgba(232,201,109,0.25); }
.chip-teal { background: rgba(77,217,192,0.1);  color: var(--teal);  border: 1px solid rgba(77,217,192,0.22); }
.chip-rose { background: rgba(240,110,138,0.1); color: var(--rose);  border: 1px solid rgba(240,110,138,0.22); }

/* ══════════════════════════════════════════
   EMPTY STATE
══════════════════════════════════════════ */
.welcome-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 60vh;
    gap: 1.25rem;
    text-align: center;
}

.welcome-sigil {
    font-family: var(--font-display);
    font-size: 5rem;
    line-height: 1;
    color: var(--line-hi);
    letter-spacing: 0.1em;
}

.welcome-title {
    font-family: var(--font-display);
    font-size: 2.2rem;
    letter-spacing: 0.08em;
    color: var(--snow);
}

.welcome-desc {
    font-family: var(--font-body);
    font-size: 0.875rem;
    line-height: 1.7;
    color: var(--slate);
    max-width: 420px;
    font-weight: 300;
}

.chip-row {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 0.5rem;
}

/* ══════════════════════════════════════════
   STREAMLIT OVERRIDES
══════════════════════════════════════════ */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--gold), var(--teal)) !important;
}

.stSpinner > div {
    border-top-color: var(--gold) !important;
}

[data-testid="stMarkdownContainer"] p {
    color: var(--snow) !important;
}

.stAlert {
    border-radius: var(--r-md) !important;
    font-family: var(--font-mono) !important;
    font-size: 0.8rem !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--line-hi); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold-dim); }

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─── Session State ───────────────────────────────────────────────────────────────
for key, default in {
    "result": None,
    "chat_history": [],
    "processing": False,
    "pipeline_done": False,
    "pipeline_steps": {},
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ─── Helpers ────────────────────────────────────────────────────────────────────
STEP_CONFIG = [
    ("audio",      "🔊", "Audio",         "Extraction"),
    ("transcript", "◈",  "Transcript",    "Generation"),
    ("title",      "◤",  "Title",         "Inference"),
    ("summary",    "▣",  "Summary",       "Synthesis"),
    ("extract",    "◉",  "Extraction",    "Analysis"),
    ("rag",        "⬡",  "RAG",           "Indexing"),
]

def render_step(key, icon, label, sublabel):
    state = st.session_state.pipeline_steps.get(key, "pending")
    state_txt = {"pending": "–", "active": "Running", "done": "Done"}.get(state, "–")
    st.markdown(f"""
    <div class="pipeline-step {state}">
        <div class="step-icon {state}">{icon}</div>
        <span class="step-label {state}">{label} <span style="opacity:0.55;font-size:0.65rem">{sublabel}</span></span>
        <span class="step-state {state}">{state_txt}</span>
    </div>""", unsafe_allow_html=True)

# ─── SIDEBAR ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="brand-mark">
        <div class="brand-name">VOXEL</div>
        <div class="brand-tag">Meeting Intelligence · v2</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sb-section">Source</div>', unsafe_allow_html=True)
    source = st.text_input(
        "URL or file path",
        placeholder="https://youtube.com/watch?v=… or /path/file.mp4",
        label_visibility="collapsed"
    )

    st.markdown('<div class="sb-section">Language</div>', unsafe_allow_html=True)
    language = st.selectbox("Language", ["english", "hinglish"], index=0, label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("⚡  Run Analysis", use_container_width=True)

    if st.session_state.pipeline_done:
        st.markdown('<div class="sb-section">Pipeline</div>', unsafe_allow_html=True)
        for key, icon, label, sublabel in STEP_CONFIG:
            render_step(key, icon, label, sublabel)

    # Footer
    st.markdown("""
    <div style="position:absolute;bottom:1.5rem;left:1.5rem;right:1.5rem">
        <div style="height:1px;background:var(--line);margin-bottom:1rem"></div>
        <div style="font-family:var(--font-mono);font-size:0.58rem;letter-spacing:0.1em;
                    text-transform:uppercase;color:var(--slate)">
            Powered by Whisper · GPT-4 · LangChain
        </div>
    </div>""", unsafe_allow_html=True)

# ─── MAIN ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="masthead">
    <div>
        <div class="masthead-sub">◈ AI Meeting Intelligence Platform</div>
        <div class="masthead-title">VOXEL <span>INTEL</span></div>
    </div>
</div>""", unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─── PIPELINE RUN ────────────────────────────────────────────────────────────────
if run_btn:
    if not source.strip():
        st.error("◈ Please enter a YouTube URL or file path.")
    else:
        st.session_state.pipeline_done = False
        st.session_state.result = None
        st.session_state.chat_history = []
        st.session_state.pipeline_steps = {}

        placeholder = st.empty()

        def update_step(key, state):
            st.session_state.pipeline_steps[key] = state

        try:
            with placeholder.container():
                st.info("◈ Pipeline initialised — monitor progress in the sidebar.")

            update_step("audio", "active")
            chunks = process_input(source)
            update_step("audio", "done")

            update_step("transcript", "active")
            transcript = transcribe_all(chunks, language)
            update_step("transcript", "done")

            update_step("title", "active")
            title = generate_title(transcript)
            update_step("title", "done")

            update_step("summary", "active")
            summary = summarize(transcript)
            update_step("summary", "done")

            update_step("extract", "active")
            action_items = extract_action_items(transcript)
            decisions    = extract_key_decisions(transcript)
            questions    = extract_questions(transcript)
            update_step("extract", "done")

            update_step("rag", "active")
            rag_chain = build_rag_chain(transcript)
            update_step("rag", "done")

            st.session_state.result = {
                "title": title, "transcript": transcript,
                "summary": summary, "action_items": action_items,
                "key_decisions": decisions, "open_questions": questions,
                "rag_chain": rag_chain,
            }
            st.session_state.pipeline_done = True
            placeholder.success("✓ Analysis complete — all systems nominal.")
            time.sleep(0.6)
            placeholder.empty()
            st.rerun()

        except Exception as e:
            for k in ["audio","transcript","title","summary","extract","rag"]:
                if st.session_state.pipeline_steps.get(k) == "active":
                    st.session_state.pipeline_steps[k] = "pending"
            placeholder.error(f"◈ Pipeline error: {e}")

# ─── RESULTS ─────────────────────────────────────────────────────────────────────
if st.session_state.result:
    r = st.session_state.result

    # Session title
    st.markdown(f"""
    <div class="title-panel">
        <div class="title-glyph">◈</div>
        <div>
            <div class="title-label">Session Title</div>
            <div class="title-text">{r['title']}</div>
        </div>
    </div>""", unsafe_allow_html=True)

    # ── Row 1: Summary + Transcript ──────────────────────────────────────────
    col_l, col_r = st.columns([3, 2], gap="medium")

    with col_l:
        st.markdown(f"""
        <div class="panel gold">
            <div class="panel-eyebrow">
                <div class="dot dot-gold"></div> Executive Summary
            </div>
            <div class="panel-body">{r['summary']}</div>
        </div>""", unsafe_allow_html=True)

    with col_r:
        with st.expander("◈  Full Transcript", expanded=False):
            st.markdown(f'<div class="transcript-scroll">{r["transcript"]}</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ── Row 2: Three-column extractions ─────────────────────────────────────
    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        st.markdown(f"""
        <div class="panel teal">
            <div class="panel-eyebrow">
                <div class="dot dot-teal"></div> Action Items
            </div>
            <div class="panel-body">{r['action_items']}</div>
        </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="panel gold">
            <div class="panel-eyebrow">
                <div class="dot dot-gold"></div> Key Decisions
            </div>
            <div class="panel-body">{r['key_decisions']}</div>
        </div>""", unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="panel rose">
            <div class="panel-eyebrow">
                <div class="dot dot-rose"></div> Open Questions
            </div>
            <div class="panel-body">{r['open_questions']}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Chat ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="chat-header">
        <div class="chat-header-title">CHAT</div>
        <div class="chat-badge">RAG · Contextual</div>
    </div>""", unsafe_allow_html=True)

    # Render messages or empty state
    if st.session_state.chat_history:
        msgs_html = '<div class="chat-viewport">'
        for msg in st.session_state.chat_history:
            role = msg["role"]
            cls  = "you" if role == "user" else "bot"
            sender = "You" if role == "user" else "◈ Assistant"
            msgs_html += f"""
            <div class="msg-row">
                <span class="msg-sender {cls}">{sender}</span>
                <div class="msg-bubble {cls}">{msg['content']}</div>
            </div>"""
        msgs_html += '</div>'
        st.markdown(msgs_html, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="panel" style="border-style:dashed">
            <div class="chat-empty">
                <div class="chat-empty-glyph">◈</div>
                <div class="chat-empty-text">Ask anything about your meeting</div>
            </div>
        </div>""", unsafe_allow_html=True)

    # Input row
    inp_col, btn_col = st.columns([6, 1], gap="small")
    with inp_col:
        user_input = st.text_input(
            "question", label_visibility="collapsed",
            placeholder="e.g. What decisions were made about the product roadmap?"
        )
    with btn_col:
        send = st.button("Send", use_container_width=True)

    if send and user_input.strip():
        with st.spinner(""):
            answer = ask_question(r["rag_chain"], user_input.strip())
        st.session_state.chat_history.append({"role": "user",      "content": user_input.strip()})
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.rerun()

    if st.session_state.chat_history:
        if st.button("Clear conversation", type="secondary"):
            st.session_state.chat_history = []
            st.rerun()

# ─── EMPTY STATE ─────────────────────────────────────────────────────────────────
else:
    st.markdown("""
    <div class="welcome-wrap">
        <div class="welcome-sigil">◈</div>
        <div class="welcome-title">READY TO ANALYSE</div>
        <div class="welcome-desc">
            Paste a YouTube URL or local file path in the sidebar, select your language, and hit <strong>Run Analysis</strong> to begin.
        </div>
        <div class="chip-row">
            <span class="chip chip-gold">◈ Transcription</span>
            <span class="chip chip-teal">▣ Summarisation</span>
            <span class="chip chip-rose">◉ RAG Chat</span>
            <span class="chip chip-gold">◤ Action Items</span>
            <span class="chip chip-teal">⬡ Key Decisions</span>
        </div>
    </div>""", unsafe_allow_html=True)