from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

# =========================
# YOUR AI IMPORTS
# =========================

from utils.audio_processor import process_input

from core.transcriber import transcribe_all

from core.summarizer import (
    summarize,
    generate_title
)

from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions
)

from core.rag_engine import (
    build_rag_chain,
    ask_question
)

# =========================
# LOAD ENV
# =========================

load_dotenv()

# =========================
# FASTAPI APP
# =========================

app = FastAPI()

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# GLOBAL STORAGE
# =========================

rag_chain_global = None

# =========================
# REQUEST MODELS
# =========================

class MeetingRequest(BaseModel):

    source: str
    language: str


class ChatRequest(BaseModel):

    question: str

# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():

    return {
        "message": "VOXEL AI Backend Running"
    }

# =========================
# ANALYZE API
# =========================

@app.post("/analyze")
async def analyze(data: MeetingRequest):

    global rag_chain_global

    try:

        source = data.source
        language = data.language

        print("\n=========================")
        print("STARTING ANALYSIS")
        print("=========================")

        # =========================
        # AUDIO PROCESSING
        # =========================

        print("Processing audio...")

        chunks = process_input(source)

        # =========================
        # TRANSCRIPTION
        # =========================

        print("Transcribing audio...")

        transcript = transcribe_all(
            chunks,
            language
        )

        # =========================
        # TITLE
        # =========================

        print("Generating title...")

        title = generate_title(
            transcript
        )

        # =========================
        # SUMMARY
        # =========================

        print("Generating summary...")

        summary = summarize(
            transcript
        )

        # CLEAN SUMMARY

        summary = (
            summary
            .replace("**", "")
            .replace("##", "")
            .replace("- ", "• ")
        )

        # =========================
        # EXTRACTION
        # =========================

        print("Extracting meeting insights...")

        action_items = (
            extract_action_items(transcript)
            .split("\n")
        )

        decisions = (
            extract_key_decisions(transcript)
            .split("\n")
        )

        questions = (
            extract_questions(transcript)
            .split("\n")
        )

        # REMOVE EMPTY LINES

        action_items = [
            item.strip()
            for item in action_items
            if item.strip()
        ]

        decisions = [
            item.strip()
            for item in decisions
            if item.strip()
        ]

        questions = [
            item.strip()
            for item in questions
            if item.strip()
        ]

        # =========================
        # BUILD RAG
        # =========================

        print("Building RAG pipeline...")

        rag_chain_global = build_rag_chain(
            transcript
        )

        print("Analysis completed.")

        # =========================
        # RESPONSE
        # =========================

        return {

            "success": True,

            "title": title,

            "summary": summary,

            "transcript": transcript,

            "action_items": action_items,

            "key_decisions": decisions,

            "questions": questions

        }

    except Exception as e:

        print("\nERROR:")
        print(e)

        return {

            "success": False,

            "title": "Error",

            "summary": str(e),

            "transcript": "",

            "action_items": [],

            "key_decisions": [],

            "questions": []

        }

# =========================
# CHAT API
# =========================

@app.post("/chat")
async def chat(data: ChatRequest):

    global rag_chain_global

    try:

        question = data.question

        print(f"\nQuestion: {question}")

        # =========================
        # CHECK RAG
        # =========================

        if rag_chain_global is None:

            return {
                "answer":
                "Please run meeting analysis first."
            }

        # =========================
        # ASK QUESTION
        # =========================

        answer = ask_question(
            rag_chain_global,
            question
        )

        return {
            "answer": answer
        }

    except Exception as e:

        print("\nCHAT ERROR:")
        print(e)

        return {
            "answer": str(e)
        }