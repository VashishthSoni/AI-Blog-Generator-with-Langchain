# AI Blog Generator (LangChain + Streamlit)

A simple AI-powered Blog Generator built using LangChain and Streamlit.

The app:
- Takes Topic, Audience, Tone, and Word Count
- Generates 3 SEO-friendly titles
- Selects a title
- Generates structured blog content

---

## Setup

### 1. Clone the Repository
```
git clone <your-repo-url>
cd blog-generator-langchain
```

---

### 2. Create Virtual Environment (Recommended)

Windows:
```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```pip install -r requirements.txt```

---

### 4. Environment Variable Setup

Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

Do not push this file to GitHub.

---

### 5. Run the Application

```streamlit run app.py```

- The app will open in your browser.
---

## 🧠 How It Works

1. Generates 3 SEO blog titles
2. Selects one title
3. Generates structured blog content using Pydantic
4. Displays results in Streamlit UI

---

- ⚠ Never commit your API key.

---

## ✍🏼 Author
### <b>Vashishth</b>: <b>Certified AI Automation Expert</b> <br>
<a href="https://github.com/VashishthSoni" target="_blank">
  <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="40" height="40" style="padding:10px;">
</a>
<a href="https://www.linkedin.com/in/vashishthsoni/" target="_blank">
  <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="40" height="40" style="padding:10px; border-radius:50px">
</a>