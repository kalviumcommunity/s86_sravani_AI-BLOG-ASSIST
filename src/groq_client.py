# src/groq_client.py
from groq import Groq
from src.config import GROQ_API_KEY, DEFAULT_MODEL, DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS, DEFAULT_TOP_P, DEFAULT_STOP_SEQUENCE

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def build_zero_shot_prompt(topic, question):
    """Zero-Shot: AI answers directly without examples."""
    return f"""
You are a professional AI blogger. Write high-quality content about {topic}.
Explain your reasoning step by step before generating the blog post.

Question: {question}
"""