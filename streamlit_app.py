import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simple Streamlit Demo", layout="centered")
st.title("Simple Streamlit Demo")
st.write("Use the slider to choose the number of points and see a live chart.")

n = st.slider("Number of points", min_value=10, max_value=200, value=50)
seed = st.number_input("Random seed (optional)", value=42)
if st.button("Regenerate"):
    seed += 1

np.random.seed(seed)
data = pd.DataFrame({
    "x": np.arange(n),
    "y": np.random.randn(n).cumsum(),
})

st.line_chart(data.set_index("x"))
st.write("Data preview:")
st.dataframe(data.head())

st.download_button("Download CSV", data.to_csv(index=False), file_name="demo_data.csv")
