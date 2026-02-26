import streamlit as st
import pandas as pd

st.title("📚 Book Recommendation System")

# Load data
books = pd.read_csv("books_small.csv")

# Use correct column names
TITLE_COL = "Book-Title"
IMAGE_COL = "Image-URL-M"

# Dropdown
selected_book = st.selectbox("Choose a book", books[TITLE_COL].dropna().unique())

# Show recommendations
if st.button("Recommend"):
    st.subheader("Recommended Books")

    # Simple random recommendations (replace later with model)
    recs = books.sample(5)

    cols = st.columns(5)

    for col, (_, row) in zip(cols, recs.iterrows()):
        with col:
            if IMAGE_COL in row and pd.notna(row[IMAGE_COL]):
                st.image(row[IMAGE_COL], use_container_width=True)
            st.caption(row[TITLE_COL])
