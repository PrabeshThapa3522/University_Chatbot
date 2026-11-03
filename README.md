# 🎓 College Regulation Chatbot

A **Domain-Specific Chatbot** developed using **Large Language Models (LLMs)** and **Prompt Engineering**. The chatbot answers only questions related to **college regulations** such as attendance, examinations, grading, library rules, hostel policies, and scholarships.

This project was developed as part of the **Domain-Specific Chatbot** final project.

---

# Project Objective

The objective of this project is to build a chatbot that can answer questions within a specific domain using a Large Language Model (LLM) **without Retrieval-Augmented Generation (RAG)**.

The chatbot relies entirely on carefully designed prompts and a curated knowledge base rather than external document retrieval.

---

# Features

- Domain-specific chatbot
- Uses GPT (OpenAI)
- Zero-shot prompting
- Few-shot prompting
- Chain-of-Thought prompting (internal reasoning)
- Structured prompt engineering
- Streamlit web interface
- Chat history
- Domain restriction
- Professional UI

---

# Technologies Used

- Python 3.10+
- Streamlit
- OpenAI API
- python-dotenv
- Pandas

---

# Project Structure

```
university_chatbot/
│
├── app.py
├── chatbot.py
├── prompts.py
├── requirements.txt
├── README.md
├── .env
│
├── dataset/
│   └── college_regulations.txt
│
└── evaluation/
    └── sample_queries.csv
```

---

# Dataset Description

The chatbot uses a manually curated dataset stored in:

```
dataset/college_regulations.txt
```

The dataset contains information related to:

- Attendance Policy
- Examination Rules
- Library Rules
- Hostel Rules
- Scholarship Policy
- Grading System

The dataset is loaded at application startup and injected into the LLM prompt. Since the assignment specifies **no retrieval**, the application does **not** use vector databases or semantic search.

---

# Model Architecture

```
                User Question
                       │
                       ▼
             Streamlit Interface
                       │
                       ▼
          Prompt Engineering Module
     (Zero-shot + Few-shot + CoT)
                       │
                       ▼
             OpenAI GPT Model
                       │
                       ▼
              Domain-Specific Answer
```

---

# Prompt Engineering Techniques

## 1. Zero-shot Prompting

The chatbot receives clear instructions to answer only questions related to college regulations.

Example:

```
You are a College Regulation Assistant.

Answer only questions related to college regulations.
```

---

## 2. Few-shot Prompting

Example conversations are included in the system prompt.

Example:

**User**

```
How many books can I borrow?
```

**Assistant**

```
Students can borrow a maximum of 3 books for 14 days.
```

These examples help guide the model toward consistent responses.

---

## 3. Chain-of-Thought Prompting

The chatbot is instructed to reason internally before generating an answer.

The reasoning process is **not exposed** to the user.

Example instruction:

```
Think step by step internally before answering.
Provide only the final answer.
```

---

# Domain Restriction

The chatbot only answers questions related to:

- Attendance
- Examinations
- Library
- Hostel
- Scholarships
- Grading
- Academic Regulations

Questions outside this domain receive the following response:

```
Sorry, I can only answer questions related to college regulations.
```

---

# Installation

Clone the repository.

```
git clone https://github.com/yourusername/DomainChatbot.git
```

Move into the project directory.

```
cd university_chatbot
```

Install dependencies.

```
pip install -r requirements.txt
```

Create a `.env` file.

```
OPENAI_API_KEY=your_api_key_here
```

Run the application.

```
python -m streamlit run app.py
```

---

# Example Queries

### Attendance

```
What is the minimum attendance requirement?
```

---

### Library

```
How many books can I borrow?
```

---

### Hostel

```
What are the visitor timings?
```

---

### Examination

```
Can I use my mobile phone during exams?
```

---

### Scholarship

```
Who is eligible for scholarships?
```

---

### Out-of-Domain

```
Who won the IPL 2025?
```

Expected Response

```
Sorry, I can only answer questions related to college regulations.
```

---

# Evaluation

The chatbot was evaluated using a curated set of sample questions stored in:

```
evaluation/sample_queries.csv
```

The evaluation includes:

- Domain-specific questions
- Unknown-information questions
- Out-of-domain questions

Example evaluation table:

| Query | Expected | Output | Correct |
|-------|----------|--------|---------|
| Attendance | 75% | 75% | Yes |
| Library | 3 books | 3 books | Yes |
| Hostel | 5–7 PM | 5–7 PM | Yes |

Accuracy can be calculated as:

```
Accuracy =
Correct Responses / Total Responses × 100
```

---

# Coding Standards

The project follows good software engineering practices:

- Modular code
- Separate prompt module
- Clear comments
- Reusable functions
- Environment variable management
- Organized folder structure

---

# Limitations

- Depends on OpenAI API availability.
- Knowledge is limited to the curated regulations.
- Does not retrieve or update information dynamically.

---

# Future Improvements

Possible future enhancements include:

- Multi-college support
- Voice input/output
- PDF regulation import
- Authentication for students
- Conversation memory
- Admin panel for updating regulations
- Support for multiple languages
- Local deployment using Llama 3 or Mistral

---

# Learning Outcomes

Through this project, the following concepts were implemented:

- Large Language Models (LLMs)
- Prompt Engineering
- Zero-shot Prompting
- Few-shot Prompting
- Chain-of-Thought Prompting
- Domain-Specific Chatbots
- Streamlit Application Development
- OpenAI API Integration
- Software Project Organization

---

# References

1. OpenAI API Documentation: https://platform.openai.com/docs
2. Streamlit Documentation: https://docs.streamlit.io/
3. Python Documentation: https://docs.python.org/3/
4. Prompt Engineering Guide: https://www.promptingguide.ai/

---

# Author

**Name:** Prabesh Thapa

**Course:** Artificial Intelligence / Machine Learning

**Project:** Domain-Specific Chatbot Using Prompt Engineering and LLM

**Year:** 2026

---
<!-- python3 -m pip install -r requirements.txt 
python3 -m streamlit run app.py -->