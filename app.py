import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os
import re
import time

load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
gpt_model = "gpt-4o-mini"

# Cleaner
def clean_text(text):
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Remove bold formatting
    text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Remove italic formatting
    text = re.sub(r'\n\s*\n', '\n\n', text)          # Normalize newlines
    text = re.sub(r'^[\*\d\.\s]+', '', text, flags=re.MULTILINE)  # Remove list indicators
    text = re.sub(r'[^\w\s,.!?]', '', text)  # Remove unnecessary symbols
    text = text.strip()
    return text

# Generate response from GPT
def generate_response(prompt, max_retries=5):
    attempt = 0
    while attempt < max_retries:
        try:
            response = openai_client.chat.completions.create(
                model=gpt_model,
                messages=[
                    {"role": "system", "content": "You are Shura-bot, an expert assistant specialized in the game 'Sekiro: Shadows Die Twice'. "
                        "Your goal is to provide **concise and accurate** responses related to game mechanics, strategies, "
                        "and technical issues. Avoid unnecessary details and focus only on the core solution. If asked about "
                        "strategies or gameplay, provide only the **most essential tips and steps**, keeping it brief and practical"},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=600,
                temperature=0.4,
            )
            raw_text = response.choices[0].message.content
            cleaned_text = clean_text(raw_text)
            return cleaned_text
        except Exception as e:
            attempt += 1
            st.warning(f"Attempt {attempt} failed. Retrying...")
            time.sleep(2)  # Small delay between retries
            if attempt == max_retries:
                return f"Error: Failed to generate a response after {max_retries} attempts. Error details: {e}"

# Streamlit UI setup
st.set_page_config(layout="wide")

# Chat interface
st.title("Shura-bot: Sekiro Shadows Die Twice Assistant")
st.write("Ask me anything about the game! I can help with Game Mechanics, Lore, Combat Strategies, etc.")

# Suggestions for topics
suggestions = ["Game Mechanics", "Lore", "Combat Strategies", "Boss Fight Tips", "Fixing Game Errors"]
st.subheader("Suggestions:")
selected_suggestion = st.selectbox("Pick a topic to start", suggestions)

# User input and interaction
user_input = st.text_input("Type your question here...", value=selected_suggestion)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User query and generating response
if st.button("Send"):
    if user_input:
        # Add user query to chat history
        st.session_state.chat_history.append(("You", user_input))
        # Generate response from the bot with retry logic
        response = generate_response(user_input)
        # Add bot's response to chat history
        st.session_state.chat_history.append(("Shura-bot", response))

# Display chat history
chat_container = st.container()
with chat_container:
    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.write(f"**{sender}:** {message}")
        else:
            st.write(f"**{sender}:** {message}")

# Option to clear chat
if st.button("Clear Chat"):
    st.session_state.chat_history = []
