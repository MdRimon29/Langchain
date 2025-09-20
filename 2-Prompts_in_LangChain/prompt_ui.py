from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

st.header("Research Tool")

# Asking prompt to user.
# user_input=st.text_input("Enter your prompt: ")

# Instead of prompt now we do it dynamically by asking select dropdown options.
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

if st.button("Summarize"):
    st.write("Hello")
