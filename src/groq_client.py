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


def build_one_shot_prompt(topic, question):
    """One-Shot: AI is given a single example."""
    return f"""
You are a professional AI blogger. Write high-quality content about {topic}.
Explain reasoning step by step.

Example:
Topic: Benefits of Morning Exercise
Blog Post: Morning exercise improves mood, boosts energy, and enhances focus.

Question: {question}
"""


def build_multi_shot_prompt(topic, question):
    """Multi-Shot: AI is given multiple examples."""
    return f"""
You are a professional AI blogger. Write high-quality content about {topic}.
Explain reasoning step by step.

Examples:
1) Topic: How to save energy at home
   Blog Post: Simple tips like using LED bulbs and unplugging devices reduce energy consumption.
2) Topic: Remote Work Tips
   Blog Post: Establish a dedicated workspace, maintain schedule, and use productivity tools.
3) Topic: Blockchain Explained
   Blog Post: Blockchain is a decentralized ledger that records transactions securely.

Question: {question}
"""


def get_ai_response(prompt, stream=False):
    """
    Calls Groq LLM with prompt.
    Supports streaming if stream=True.
    Logs tokens if not streaming.
    """
    if stream:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=DEFAULT_TEMPERATURE,
            max_completion_tokens=DEFAULT_MAX_TOKENS,
            top_p=DEFAULT_TOP_P,
            stream=True,
            stop=DEFAULT_STOP_SEQUENCE
        )

        response_text = ""
        for chunk in completion:
            # Directly access .content attribute
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                response_text += content
        print()
        return response_text

    else:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=DEFAULT_TEMPERATURE,
            max_completion_tokens=DEFAULT_MAX_TOKENS,
            top_p=DEFAULT_TOP_P,
            stop=DEFAULT_STOP_SEQUENCE
        )

        # Non-streaming, access content safely
        tokens_used = getattr(response.usage, "total_tokens", None)
        if tokens_used:
            print(f"Tokens used: {tokens_used}")

        content = response.choices[0].message.content
        return content
