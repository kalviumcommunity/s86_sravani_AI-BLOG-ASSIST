# s86_sravani_AI-BLOG-ASSIST

# **AI Blogging Assistant**

**AI Blogging Assistant** is an AI-powered platform that automatically generates **blog posts, summaries, and social media snippets**. It leverages Groq LLM to provide high-quality content based on user-provided topics. The project demonstrates multiple GenAI concepts, including prompt engineering, dynamic prompting, chain of thought, and advanced LLM features.

---

## **Features**

* Generate **full blog posts** from user topics
* Produce **summaries** and **social media snippets**
* Supports **Zero-Shot, One-Shot, Multi-Shot, and Dynamic prompting**
* Uses **Chain of Thought** for reasoning before generating content
* Logs **tokens used** and supports **temperature, Top P, Top K, and stop sequences**
* Returns **structured output** (JSON with title, summary, full post)
* **Cosine similarity** suggests related blog ideas for user inspiration

---

## **GenAI Concepts Covered**

1. **Create Project Readme** – This README explains project idea, setup, and usage.
2. **System and User Prompt** – Clear system instructions for the AI and user input prompts.
3. **Zero-Shot Prompting** – Generate content without prior examples.
4. **One-Shot Prompting** – Generate content with a single guiding example.
5. **Multi-Shot Prompting** – Generate content using multiple examples.
6. **Dynamic Prompting** – Prompt adapts based on blog type, tone, or word count.
7. **Chain of Thought Prompting** – AI explains reasoning before content generation.
8. **Tokens, Temperature, Top P/K, Stop Sequences, Structured Output** – Advanced LLM parameters to control creativity and output format.
9. **Cosine Similarity** – Match user topic prompts to related blog ideas.

---

## **Tech Stack**

* **Python 3.x**
* **Groq LLM** (llama-3.1-8b-instant or llama-3.1-70b-versatile)
* **Streamlit** for UI
* **NumPy / scikit-learn** for cosine similarity

---

## **Installation**

1. Clone the repository:

```bash
git clone <repo-url>
cd ai-blogging-assistant
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your **Groq API key** in `src/config.py`:

```python
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## **Usage**

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Open the app in your browser.

3. **Sidebar Options**:

   * Project Info
   * Sample blog topics for testing
   * Select **Prompt Type** (Zero/One/Multi-Shot)

4. **Main Page**:

   * Enter any topic or question
   * Click **Get Answer** to generate blog content

5. **Output**:

   * Blog title
   * Summary
   * Full post

---

## **Example Topics**

* Sustainable Fashion Trends
* Future of AI in Healthcare
* Remote Work Productivity Tips
* How to Save Energy at Home
* Blockchain Explained for Beginners

---

## **Advanced Features**

* Adjust **Temperature** to control creativity (0–1)
* Use **Top P / Top K** to modify randomness of responses
* **Stop sequences** ensure clean output
* **Structured output** returns JSON with fields like:

```json
{
  "title": "...",
  "summary": "...",
  "full_post": "..."
}
```

* **Cosine similarity** suggests similar blog topics to avoid duplicates

---

## **Folder Structure**

```
ai-blogging-assistant/
│-- app.py
│-- README.md
│-- requirements.txt
│-- concepts.md
│-- src/
    │-- config.py
    │-- groq_client.py
    │-- utils.py  # optional: cosine similarity functions
```

---

## **Contributing**

* Fork the repository
* Create a feature branch
* Submit a pull request

---

## **License**

MIT License