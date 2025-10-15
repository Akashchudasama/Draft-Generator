import google.generativeai as genai

# ⚠️ For production, store your API key in environment variables instead of hardcoding
GEMINI_API_KEY = "AIzaSyClWrx_ke-Uw30a02mxeBx1rQ5WldgE6XI"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Use the latest Gemini model
DEFAULT_MODEL = "gemini-2.5-flash"

def generate_draft(
    prompt: str,
    tone: str = "neutral",
    length_choice: str = "medium",
    model: str = DEFAULT_MODEL,
    bullets: bool = False,
):
    """
    Generate a draft using Gemini.
    Returns a dictionary with English, Hindi, and Gujarati versions.
    """

    # Base prompt
    full_prompt = f"Write in a {tone} tone.\n\n{prompt}"

    # Adjust length
    if length_choice == "short":
        full_prompt += "\n\nKeep it concise (2-3 sentences)."
    elif length_choice == "medium":
        full_prompt += "\n\nProvide a moderate-length response (1-2 paragraphs)."
    elif length_choice == "long":
        full_prompt += "\n\nProvide a detailed and extended response."

    # Add bullet formatting if needed
    if bullets:
        full_prompt += "\n\nFormat the answer using bullet points where possible."

    # Initialize model
    gen_model = genai.GenerativeModel(model)

    # Helper to safely generate in each language
    def safe_generate(prompt_text):
        try:
            resp = gen_model.generate_content(prompt_text)
            return resp.text.strip() if resp and resp.text else ""
        except Exception as e:
            print(f"Error generating response: {e}")
            return ""

    # Generate responses
    en_text = safe_generate(f"{full_prompt}\n\nRespond in English only.")
    hi_text = safe_generate(f"{full_prompt}\n\nRespond in Hindi only.")
    gu_text = safe_generate(f"{full_prompt}\n\nRespond in Gujarati only.")

    return {
        "english": en_text,
        "hindi": hi_text,
        "gujarati": gu_text,
    }
