import streamlit as st
from chatbot import get_chatbot_response

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="College Regulation Chatbot",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    color: #1E88E5;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 30px;
}
.user-msg {
    background-color: #DCF8C6;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
}
.bot-msg {
    background-color: #F1F0F0;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown(
    "<div class='main-title'>🎓 College Regulation Chatbot</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>Domain-Specific Chatbot using Prompt Engineering and LLM</div>",
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("📌 Project Information")

    st.write("### Domain")
    st.info("College Regulations")

    st.write("### Prompting Techniques")
    st.success("✅ Zero-shot")
    st.success("✅ Few-shot")
    st.success("✅ Chain-of-Thought")

    st.write("### Supported Topics")

    st.markdown("""
- Attendance
- Examination Rules
- Grading System
- Library Rules
- Hostel Rules
- Scholarships
- Internship Policies
""")

    st.divider()

    st.write("### Instructions")

    st.write("""
Ask questions related to:

- Attendance
- Exams
- Hostel
- Library
- Scholarship
- Grading

The chatbot will only answer questions related to college regulations.
""")

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f"<div class='user-msg'><b>👤 You:</b><br>{message['content']}</div>",
            unsafe_allow_html=True,
        )

    else:
        st.markdown(
            f"<div class='bot-msg'><b>🤖 Assistant:</b><br>{message['content']}</div>",
            unsafe_allow_html=True,
        )

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Ask a question about college regulations...")

if user_input:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    st.markdown(
        f"<div class='user-msg'><b>👤 You:</b><br>{user_input}</div>",
        unsafe_allow_html=True,
    )

    # Generate response
    with st.spinner("Thinking..."):

        response = get_chatbot_response(user_input)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Display assistant response
    st.markdown(
        f"<div class='bot-msg'><b>🤖 Assistant:</b><br>{response}</div>",
        unsafe_allow_html=True,
    )

# -----------------------------
# Example Questions
# -----------------------------
st.divider()

st.subheader("💡 Example Questions")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- What is the minimum attendance requirement?
- Can I use a mobile phone during exams?
- How many books can I borrow from the library?
- What is the hostel visitor timing?
""")

with col2:
    st.markdown("""
- What is the grading system?
- Who is eligible for scholarships?
- What happens if attendance is below 60%?
- Can I enter the exam hall after 30 minutes?
""")

st.divider()

st.caption(
    "Final Year Project • Domain-Specific Chatbot using Prompt Engineering • Streamlit + LLM"
)