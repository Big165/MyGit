import streamlit as st
import pandas as pd

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image('./ing/Dog.jpg')
st.subheader("นายวงศกร สุขขันติราษฎร์")

col1, col2, col3 = st.columns(3)

with col1:
        st.header("black")
        st.image("./ing/black.jpg")

with col2:
        st.header("white")
        st.image("./ing/white.jpg")

with col3:
        st.header("yellow")
        st.image("./ing/yollow.jpg")
