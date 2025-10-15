import os
from dotenv import load_dotenv
import streamlit as st
from services.ai import generate_draft

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="📝Your Draft Agent", page_icon="📝", layout="wide")

st.title("📝 Your Hindi Draft Generator")

with st.form("draft_form", clear_on_submit=False):
    cmd = st.text_area(
        "Your command",
        placeholder=(
            "e.g., Write a professional email to my professor requesting an extension for my assignment due to illness; "
            "include a polite apology and propose a new deadline of Friday."
        ),
        height=160
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        tone = st.selectbox("Tone", ["Professional", "Formal", "Friendly", "Casual", "Persuasive"], index=0)
    with col2:
        length_choice = st.select_slider("Length", options=["Short", "Medium", "Long"], value="Medium")
    with col3:
        bullets = st.checkbox("Also include key bullet points", value=False)
    submitted = st.form_submit_button("✨ Generate drafts")

if submitted:
    if not cmd or not cmd.strip():
        st.error("Please enter a command.")
        st.stop()
    with st.spinner("Generating drafts..."):
       drafts = generate_draft(
    cmd.strip(),
    tone=tone,
    length_choice=length_choice,
    bullets=bullets,
    model=os.getenv("GOOGLE_MODEL", "gemini-1.5-flash")
)


    en = drafts.get("english", "").strip()
    hi = drafts.get("hindi", "").strip()

    left, right = st.columns(2)
    with left:
        st.subheader("🇬🇧 English")
        if en:
            st.write(en)
            st.download_button("Download English (.txt)", data=en.encode("utf-8"), file_name="draft_english.txt")
        else:
            st.info("No English content returned. Try again or adjust the prompt.")
    with right:
        st.subheader("🇮🇳 हिंदी")
        if hi:
            st.write(hi)
            st.download_button("हिंदी डाउनलोड (.txt)", data=hi.encode("utf-8"), file_name="draft_hindi.txt")
        else:
            st.info("कोई हिंदी सामग्री नहीं मिली। कृपया फिर से प्रयास करें।")

st.markdown("---")
# st.markdown(
#     "⚙️ **Model:** "
#     f"`{os.getenv('OPENAI_MODEL', 'gpt-4o-mini')}` &nbsp;&nbsp;|&nbsp;&nbsp; "
#     "Change by setting `OPENAI_MODEL` in your `.env` file."
# )
