import google.generativeai as genai

# ⚠️ For testing only — better to use environment variables later
GEMINI_API_KEY = "AIzaSyBKQe8zaCZ9ZPCuXbEZmVCIoadHHW79_-0"

genai.configure(api_key=GEMINI_API_KEY)

DEFAULT_MODEL = "gemini-1.5-flash"

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

    # Add bullets if requested
    if bullets:
        full_prompt += "\n\nFormat the answer using bullet points where possible."

    # Create model
    gen_model = genai.GenerativeModel(model)

    # Generate English
    en_resp = gen_model.generate_content(f"{full_prompt}\n\nRespond in English only.")
    en_text = en_resp.text if en_resp and en_resp.text else ""

    # Generate Hindi
    hi_resp = gen_model.generate_content(f"{full_prompt}\n\nRespond in Hindi only.")
    hi_text = hi_resp.text if hi_resp and hi_resp.text else ""

    # Generate Gujarati
    gu_resp = gen_model.generate_content(f"{full_prompt}\n\nRespond in Gujarati only.")
    gu_text = gu_resp.text if gu_resp and gu_resp.text else ""

    return {
        "english": en_text.strip(),
        "hindi": hi_text.strip(),
        "gujarati": gu_text.strip(),
    }
