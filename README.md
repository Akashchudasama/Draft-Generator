# 📝 Bilingual Draft AI (English + Hindi)

A minimal Streamlit app that takes a **command** and generates clean drafts in **English and Hindi** using OpenAI's **Responses API**.

## ✨ Features
- Single command ➜ two drafts (English + Hindi) with consistent meaning
- Optional **Key Points** bullets under each draft
- Configurable **tone** and **length**
- Simple UI + one-click **download** of each draft
- Uses the official `openai` Python SDK and the **Responses API**

## 🧰 Tech
- Python 3.10+
- Streamlit
- OpenAI Python SDK
- python-dotenv

## 🚀 Quickstart

1) **Clone / unzip** this project.

2) **Create a virtual environment** (Windows PowerShell):
```pwsh
python -m venv .venv
.\.venv\Scripts\activate
```
Mac/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3) **Install deps**:
```bash
pip install -r requirements.txt
```

4) **Set your API key**:
- Copy `.env.example` to `.env`
- Put your OpenAI key:
  ```env
  OPENAI_API_KEY=sk-your-api-key-here
  # optional; default is gpt-4o-mini
  OPENAI_MODEL=gpt-4o-mini
  ```

5) **Run the app**:
```bash
streamlit run app.py
```
The app will open in your browser (usually http://localhost:8501).

## 🧪 Try a command
- *"Write a professional leave application to my manager for two days due to a family event. Keep it polite, propose covering tasks after return."*
- *"Draft a startup idea pitch for a healthcare app connecting patients with nearby pharmacies; include problem, solution, features, and CTA."*
- *"Create a LinkedIn post about launching my portfolio website; friendly tone, 200–250 words."*

## 🔧 Configuration
- Change the default model by setting `OPENAI_MODEL` in `.env` (e.g., `gpt-4.1` or `gpt-4o`).
- Proxy/enterprise setups can set `OPENAI_BASE_URL` and other advanced options; see OpenAI docs.

## 📚 References
- OpenAI **Responses API** examples + `response.output_text`: official SDK README.
- Official **Models** docs for `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`.
- Production best practices: use env vars for keys.

## ❓ Troubleshooting
- **Invalid API key**: ensure `.env` is loaded and the key is correct.
- **ImportError: No module named openai**: `pip install openai` (ensure v1.x+).
- **Firewall/Proxy**: set `OPENAI_BASE_URL` or use a proxy per docs.

---
Made with ❤️ using Streamlit + OpenAI.
