def detect_emotion(text: str) -> str:
    text = text.lower()
    if "lol" in text or "haha" in text:
        return "humor"
    if "angry" in text:
        return "anger"
    return "neutral"
