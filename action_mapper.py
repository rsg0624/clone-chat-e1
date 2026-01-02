def map_to_action(intent, emotion, personality):
    if intent == "greeting":
        return f"{personality['style']} wave with smile"
    if intent == "question":
        return f"{personality['style']} confused look"
    return f"{personality['style']} neutral nod"
