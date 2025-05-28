import streamlit as st
from backend import answer_question

# Set page configuration
st.set_page_config(
    page_title="Knowledge Assistant",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS for minimalist styling
st.markdown("""
    <style>
        /* Hide Streamlit branding and menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Customize input box */
        .stTextInput > div > div > input {
            font-size: 18px;
            padding: 10px;
        }

        /* Customize button */
        .stButton > button {
            font-size: 18px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
        }

        /* Customize answer box */
        .answer-box {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            margin-top: 20px;
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💬 Knowledge Assistant")
st.markdown("Ask a question to explore the knowledge base.")

# Input form
with st.form(key='question_form'):
    question = st.text_input("Your question:")
    submit_button = st.form_submit_button(label='Submit')

# Display answer
if submit_button and question:
    with st.spinner("Fetching answer..."):
        answer = answer_question(question)
    st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)