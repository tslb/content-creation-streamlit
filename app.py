import streamlit as st 
from llm_prompt_template import write_an_llm_article
from llm import LLMClient
from dotenv import load_dotenv
import config as CONFIG
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Title of the app
st.title("Content Processing with Multiple Inputs")

# Text inputs for keywords, prompt, architecture, and style
keywords = st.text_input("Enter keywords (comma-separated):")
context = st.text_input("Enter context:")
topic = st.selectbox("Enter Topic:", ["Political", "Geography", "Economy", "History", "Miscellaneous"])
writing_style = st.selectbox("Choose the writing style:", ["Technical", "Expository", "Persuasive"])
tone = st.selectbox("Choose the Tone:", ["Formal", "Informal", "Optimistic", "Curious", "Assertive", "Surprised"])

if st.button("GO"):
    openai_llm_client = LLMClient(0.7, 60)
    anthropic_llm_client = LLMClient(0.7, 60)
    model = CONFIG.OPENAI_CHAT_MODEL
    llm_family = CONFIG.LLMFamily.OPEN_AI.value
    anthropic_model = CONFIG.ANTHROPIC_SONNET_3_5_MODEL
    llm_family_anthropic = CONFIG.LLMFamily.ANTHROPIC.value
    prompt_args = {
        "keywords": keywords,
        "context": context,
        "topic": topic,
        "tone": tone,
        "writing_style": writing_style
    }
    llm_output = openai_llm_client.invoke(llm_family, model, 4000, write_an_llm_article, prompt_args)
    st.text_area("Article is:",f"{llm_output}", height=200)