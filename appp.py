import streamlit as st
import spacy
from spacy import displacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Set up the app title and layout
st.set_page_config(page_title="NLP with spaCy", page_icon="🔍", layout="wide")
st.title("🔍 NLP with spaCy")
st.write("Enter a sentence below to analyze its parts of speech and named entities:")

# User input
text = st.text_area("✏️ Enter text here", "Mark Zuckerberg found Facebook and renamed it as Meta")

# Process input
if text:
    doc = nlp(text)

    # Named Entities
    st.subheader("🧠 Named Entities")
    if doc.ents:
        for ent in doc.ents:
            st.write(f"• **{ent.text}** | {ent.label_} | {spacy.explain(ent.label_)}")
    else:
        st.write("No named entities found.")

    # Part-of-Speech Tags
    st.subheader("🔤 Part-of-Speech Tags")
    pos_data = [(token.text, token.pos_, token.tag_, spacy.explain(token.tag_)) for token in doc]
    st.table(pos_data)

    # Dependency Parse
    st.subheader("🧩 Dependency Parse")
    html = displacy.render(doc, style="dep", page=True)
    st.components.v1.html(html, height=300, scrolling=True)

# Footer
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    </style>
    <div style="text-align: center; margin-top: 50px;">
        <p style="font-size: 18px; color: #888;">made by SARTHAK</p>
    </div>
    """, unsafe_allow_html=True)
