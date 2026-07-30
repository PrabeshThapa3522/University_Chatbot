# Using OpenAI API Key 
# """
# chatbot.py

# Domain-Specific College Regulation Chatbot
# Uses:
# - OpenAI GPT
# - Prompt Engineering
# - Streamlit

# Author: Final Year Project
# """

# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# from prompts import build_system_prompt

# # ==========================================================
# # Load Environment Variables
# # ==========================================================

# load_dotenv()

# API_KEY = os.getenv("OPENAI_API_KEY")

# if not API_KEY:
#     raise ValueError(
#         "OPENAI_API_KEY not found.\n"
#         "Create a .env file and add:\n"
#         "OPENAI_API_KEY=your_api_key"
#     )

# # ==========================================================
# # Initialize OpenAI Client
# # ==========================================================

# client = OpenAI(api_key=API_KEY)

# # ==========================================================
# # Load College Regulations Dataset
# # ==========================================================

# DATASET_PATH = "dataset/college_regulations.txt"

# try:
#     with open(DATASET_PATH, "r", encoding="utf-8") as file:
#         COLLEGE_RULES = file.read()

# except FileNotFoundError:
#     raise FileNotFoundError(
#         "dataset/college_regulations.txt not found."
#     )

# # ==========================================================
# # Build System Prompt
# # ==========================================================

# SYSTEM_PROMPT = build_system_prompt(COLLEGE_RULES)

# # ==========================================================
# # Chat Function
# # ==========================================================

# def get_chatbot_response(question: str) -> str:
#     """
#     Generates a response from the LLM.

#     Parameters
#     ----------
#     question : str
#         User's question.

#     Returns
#     -------
#     str
#         Chatbot response.
#     """

#     try:

#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             temperature=0.2,
#             messages=[
#                 {
#                     "role": "system",
#                     "content": SYSTEM_PROMPT
#                 },
#                 {
#                     "role": "user",
#                     "content": question
#                 }
#             ]
#         )

#         return response.choices[0].message.content.strip()

#     except Exception as e:

#         return f"❌ Error:\n\n{str(e)}"


# # ==========================================================
# # Command Line Test
# # ==========================================================

# if __name__ == "__main__":

#     print("=" * 60)
#     print("College Regulation Chatbot")
#     print("=" * 60)
#     print("Type 'exit' to quit.\n")

#     while True:

#         question = input("You: ")

#         if question.lower() in ["exit", "quit"]:
#             print("\nGoodbye!")
#             break

#         answer = get_chatbot_response(question)

#         print("\nAssistant:")
#         print(answer)
#         print("-" * 60)

"""
chatbot.py

Domain-Specific College Regulation Chatbot
Using Ollama + Llama 3

Author: Final Year Project
"""

from pathlib import Path
import ollama
from prompts import build_system_prompt

# ==========================================================
# Load College Regulations
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "dataset" / "college_regulations.txt"

if not DATASET_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found:\n{DATASET_PATH}"
    )

with open(DATASET_PATH, "r", encoding="utf-8") as file:
    COLLEGE_RULES = file.read()

# ==========================================================
# Build Prompt
# ==========================================================

SYSTEM_PROMPT = build_system_prompt(COLLEGE_RULES)

# ==========================================================
# Chat Function
# ==========================================================

def get_chatbot_response(question: str) -> str:
    """
    Generate a response using Ollama (Llama 3).
    """

    try:

        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"""
❌ Unable to connect to Ollama.

Possible reasons:

• Ollama is not installed
• Ollama is not running
• Llama3 model has not been downloaded

Error:

{e}
"""


# ==========================================================
# Local Testing
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("College Regulation Chatbot")
    print("Powered by Llama 3 (Ollama)")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = get_chatbot_response(question)

        print("\nAssistant:")
        print(answer)