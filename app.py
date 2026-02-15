import streamlit as st
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    PydanticOutputParser,
    StrOutputParser,
)

# Environment Setup
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY not found")
    st.stop()


# Pydantic Schema
class Blog(BaseModel):
    titles: list[str] = Field(
        min_length=3,
        description="List of Blog Titles, minimum 3 titles"
    )
    content: str = Field(description="Blog Content")


# Model Initialization
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8,
)

pyd_parser = PydanticOutputParser(pydantic_object=Blog)
strparser = StrOutputParser()


# Prompts
title_prompt = PromptTemplate(
    template="""
Generate exactly 3 engaging and SEO-friendly blog titles.
Topic: {topic}
Target Audience: {audience}

Rules:
Titles must be clear and catchy
Maximum 60 characters each
Do not number them
Return only the titles (each on a new line)
""",
    input_variables=["topic", "audience"],
)

content_prompt = PromptTemplate(
    template="""
Write a well-structured blog article using the details below.
Titles: {titles}
Selected Title: {selected_title}
Topic: {topic}
Target Audience: {audience}
Tone: {tone}
Word Count: {word_count}

Instructions:
- Start with an engaging introduction
- Use Selected Title to generate Blog content.
- Do not write titles.
- Include 3–5 clear subheadings
- Use simple and readable language
- Maintain the requested tone throughout
- Keep content close to the requested word count
- End with a strong conclusion
- Do not include meta commentary
- Return only the blog content.

Format Instructions:
{format_instructions}
""",
    input_variables=[
        "titles",
        "selected_title",
        "topic",
        "audience",
        "tone",
        "word_count",
        "format_instructions",
    ],
)

title_chain = title_prompt | model | strparser
content_chain = content_prompt | model | pyd_parser


# Streamlit UI
st.title("AI Blog Generator")

with st.form("blog_form"):
    topic = st.text_input("Topic")
    audience = st.text_input("Target Audience")
    tone = st.selectbox(
        "Tone",
        ["Professional", "Casual", "Friendly", "Formal", "Informative"]
    )
    word_count = st.number_input(
        "Word Count",
        min_value=200,
        max_value=2000,
        value=500,
        step=100
    )

    submit = st.form_submit_button("Generate Blog")

if submit:
    with st.spinner("Generating blog..."):

        # Step 1: Generate Titles
        res = title_chain.invoke({
            "topic": topic,
            "audience": audience,
        })

        titles = [t.strip() for t in res.split("\n") if t.strip()]

        # Step 2: Generate Blog Content
        blog_content = content_chain.invoke({
            "titles": titles,
            "selected_title": titles[0],
            "topic": topic,
            "audience": audience,
            "tone": tone,
            "word_count": word_count,
            "format_instructions": pyd_parser.get_format_instructions()
        })

        # Display Output
        st.subheader("Generated Titles")
        for t in blog_content.titles:
            st.write(f"- {t}")

        st.subheader("Blog Content")
        st.write(blog_content.content)
