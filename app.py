import streamlit as st
import pickle
import re
 
# Load trained SVM model & vectorizer
 
model = pickle.load(open("text_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
 
# Text cleaning function
 
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', str(text))
    text = text.lower()
    return text
 
# Streamlit UI setup 
st.set_page_config(
    page_title="Fake News Detection System",
    layout="centered"
)

st.title("📰 Fake News Detection System")
st.write(
    "This application uses **Machine Learning (TF-IDF + Linear SVM)** "
    "to classify news articles as **Real or Fake**."
)

st.markdown("---")

news_input = st.text_area(
    "✍️ Enter News Article Text",
    height=220,
    placeholder="Paste the full news article here..."
)
 
# Prediction 
if st.button("🔍 Check News"):
    if news_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        cleaned_text = clean_text(news_input)
        vect = vectorizer.transform([cleaned_text])

        # SVM prediction (NO probabilities)
        prediction = model.predict(vect)[0]

        st.markdown("---")

        if prediction == 1:
            st.error("❌ **Fake News Detected**")
        else:
            st.success("✅ **Real News Detected**")

 
# Footer 

st.markdown("---")
st.caption(
    "📌 Note: This system analyzes linguistic patterns in news articles. "
    "It does not verify factual correctness."
)
