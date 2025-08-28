# app.py
import streamlit as st
from src.groq_client import get_ai_response, build_zero_shot_prompt, build_one_shot_prompt, build_multi_shot_prompt

# Streamlit page configuration
st.set_page_config(
    page_title="AI Blogging Assistant",
    page_icon=":memo:",
    layout="wide"
)

# ========================
# Sidebar
# ========================
with st.sidebar:
    st.title("Project Info")
    st.markdown("""
    **AI Blogging Assistant**  
    Generate high-quality blogs, summaries, and social media snippets automatically.
    """)

    st.markdown("---")
    st.subheader("Sample Topics / Test Inputs")
    st.markdown("""
    - Sustainable Fashion Trends  
    - Future of AI in Healthcare  
    - Remote Work Productivity Tips  
    - How to Save Energy at Home  
    - Blockchain Explained  
    """)

    st.markdown("---")
    st.subheader("Prompt Type")
    prompt_type = st.radio("Choose Prompt Type:", [
                           "Zero-Shot", "One-Shot", "Multi-Shot"])

    st.markdown("---")
    st.subheader("Streaming Mode")
    stream_mode = st.checkbox("Enable Streaming Output", value=True)

# ========================
# Main Page
# ========================
st.title("AI Blogging Assistant")
st.write("Enter any topic below to generate a detailed blog post with explanations, summaries, and social snippets!")

# User input
topic = st.text_input("Enter your topic or idea:")
submit = st.button("Generate Content")

# ========================
# Generate AI Content
# ========================
if submit and topic:
    # Build prompt based on selected type
    if prompt_type == "Zero-Shot":
        prompt = build_zero_shot_prompt(topic, topic)
    elif prompt_type == "One-Shot":
        prompt = build_one_shot_prompt(topic, topic)
    else:
        prompt = build_multi_shot_prompt(topic, topic)

    # Call Groq LLM
    with st.spinner("Generating content..."):
        try:
            answer = get_ai_response(prompt, stream=stream_mode)
        except Exception as e:
            st.error(f"Error generating content: {e}")
            answer = None

    # Display result
    if answer:
        st.markdown("---")
        st.markdown("### Generated Blog Content")
        st.write(answer)
        st.markdown("---")
        st.success("Content generation complete!")
