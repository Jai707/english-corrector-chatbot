import streamlit as st
from openai import OpenAI

# Load API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="✍️ English Correction Chatbot")

st.title("✍️ English Correction Chatbot")
st.write("Type a sentence and get a grammatically correct version.")

user_input = st.text_input("Enter your English sentence:")

if user_input:
    with st.spinner("Correcting..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful English tutor. Please correct grammar and spelling errors."},
                    {"role": "user", "content": f"Correct this sentence: {user_input}"}
                ]
            )
            corrected = response.choices[0].message.content.strip()
            st.success("✅ Corrected Sentence:")
            st.write(corrected)
        except Exception as e:
            st.error(f"❌ Error: {e}")
