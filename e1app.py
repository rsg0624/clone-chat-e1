import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import streamlit as st
from intent import detect_intent
from emotion detect_emotion
from map map_to_action
from personality get_personality

st.set_page_config(page_title="Clone Chat – E1", layout="centered")

st.title("🤖 Clone Chat – Evolution E1")
st.caption("Thought → Emotion → Action (Avatar Simulation)")

user_text = st.text_input("Type a message")

if user_text:
    intent = detect_intent(user_text)
    emotion = detect_emotion(user_text)
    personality = get_personality("funny")
    action = map_to_action(intent, emotion, personality)

    st.subheader("AI Interpretation")
    st.write(f"**Intent:** {intent}")
    st.write(f"**Emotion:** {emotion}")
    st.write(f"**Personality:** {personality['name']}")
    st.success(f"🎬 Avatar Action: {action}")
