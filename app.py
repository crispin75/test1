import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit Demo", layout="wide")

st.title("Streamlit Demo App")
st.caption("A small interactive demo you can deploy.")

with st.sidebar:
    st.header("Controls")
    n = st.slider("Number of points", 50, 2000, 500, step=50)
    seed = st.number_input("Random seed", value=42, step=1)
    show_data = st.checkbox("Show raw data", value=False)

rng = np.random.default_rng(int(seed))
df = pd.DataFrame(
    {"x": rng.normal(size=n), "y": rng.normal(size=n), "group": rng.integers(1, 6, size=n)}
)

c1, c2 = st.columns(2)
with c1:
    st.subheader("Scatter plot")
    st.scatter_chart(df, x="x", y="y", color="group")

with c2:
    st.subheader("Summary")
    st.write(df.describe(include="all"))

if show_data:
    st.subheader("Raw data")
    st.dataframe(df, use_container_width=True)