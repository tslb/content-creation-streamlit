import streamlit as st
from llm_prompt_template import write_an_llm_article
from llm import LLMClient
from dotenv import load_dotenv
import config as CONFIG
import os
import concurrent.futures

# Load environment variables
load_dotenv()

# Get API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Title of the app
st.title("Content Processing with Multiple Inputs")

# Description and instructions
st.write("""
### Welcome to the Content Processor
Use this tool to generate content based on various input parameters. Enter your keywords, context, select the topic, writing style, and tone to get started.
""")

# Text inputs for keywords, prompt, architecture, and style
keywords = st.text_input("Enter keywords (comma-separated):")
context = st.text_area("Enter context:")
topic = st.selectbox("Select Topic:", ["Political", "Geography", "Economy", "History", "Miscellaneous"])
writing_style = st.selectbox("Choose the writing style:", ["Technical", "Expository", "Persuasive"])
tone = st.selectbox("Choose the Tone:", ["Formal", "Informal", "Optimistic", "Curious", "Assertive", "Surprised"])

if st.button("GO"):
    # Initialize LLM clients
    openai_llm_client = LLMClient(0.7, 60)
    anthropic_llm_client = LLMClient(0.7, 60)
    model = CONFIG.OPENAI_CHAT_MODEL
    llm_family = CONFIG.LLMFamily.OPEN_AI.value
    anthropic_model = CONFIG.ANTHROPIC_SONNET_3_5_MODEL
    llm_family_anthropic = CONFIG.LLMFamily.ANTHROPIC.value

    # Prepare prompt arguments
    prompt_args = {
        "keywords": keywords,
        "context": context,
        "topic": topic,
        "tone": tone,
        "writing_style": writing_style
    }

    # Function to fetch LLM output
    def fetch_llm_output(client, llm_family, model, prompt_args):
        return client.invoke(llm_family, model, 4000, write_an_llm_article, prompt_args)

    # Run both LLM invocations in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        openai_future = executor.submit(fetch_llm_output, openai_llm_client, llm_family, model, prompt_args)
        anthropic_future = executor.submit(fetch_llm_output, anthropic_llm_client, llm_family_anthropic, anthropic_model, prompt_args)
        
        # Get the results
        llm_output = openai_future.result()
        llm_output_anthropic = anthropic_future.result()
        
    col1, col2 = st.columns([2,2])

    with col1:
        st.subheader("Generated Article by OpenAI")
        st.text_area("OpenAI Article:", llm_output, height=400)

    with col2:
        st.subheader("Generated Article by Anthropic")
        st.text_area("Anthropic Article:", llm_output_anthropic, height=400)
