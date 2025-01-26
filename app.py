import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("dataset/customer reviews.csv")
df_top100_books = pd.read_csv("dataset/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
# pegar maior valor e atribuir a variavel price_max

price_min = df_top100_books["book price"].min()
# pegar menor valor e atribuir a variavel price_min

max_price = st.sidebar.slider("Price Range", price_max, price_min, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

fig = px.bar(df_books["year of publication"].value_counts())
st.plotly_chart(fig)

fig2 = px.histogram(df_books["book price"])
st.plotly_chart(fig2)
