def detect_intent(text: str) -> str:
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "greeting"
    if "?" in text:
        return "question"
    return "statement"
