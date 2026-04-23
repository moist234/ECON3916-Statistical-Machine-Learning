import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

RMSE = 1.95
FEATURES = ["MIN", "FGA", "FG_PCT", "FG3M", "REB", "AST", "STL", "BLK", "PLUS_MINUS"]

st.title("NBA Player Points Predictor")
st.write(
    "Predict how many points an NBA player will score based on their "
    "shooting and game statistics. Adjust the sliders in the sidebar to "
    "explore different stat combinations."
)

st.sidebar.header("Player Stats")
MIN        = st.sidebar.slider("MIN – Minutes Played",   0,    48,  28)
FGA        = st.sidebar.slider("FGA – Field Goal Attempts", 0, 30,  10)
FG_PCT     = st.sidebar.slider("FG_PCT – Field Goal %", 0.0, 1.0, 0.45, step=0.01)
FG3M       = st.sidebar.slider("FG3M – 3-Pointers Made", 0,   10,   2)
REB        = st.sidebar.slider("REB – Rebounds",          0,   20,   4)
AST        = st.sidebar.slider("AST – Assists",           0,   20,   3)
STL        = st.sidebar.slider("STL – Steals",            0,    5,   1)
BLK        = st.sidebar.slider("BLK – Blocks",            0,    5,   0)
PLUS_MINUS = st.sidebar.slider("PLUS_MINUS",            -30,  30,   0)

input_data = pd.DataFrame(
    [[MIN, FGA, FG_PCT, FG3M, REB, AST, STL, BLK, PLUS_MINUS]],
    columns=FEATURES,
)

model = joblib.load(os.path.join(os.path.dirname(__file__), "model_small.pkl"))
prediction = float(model.predict(input_data)[0])

low  = round(prediction - RMSE, 1)
high = round(prediction + RMSE, 1)

st.metric(label="Predicted Points", value=f"{prediction:.1f} PTS")

st.info(f"Prediction interval (±1 RMSE): **{low} – {high} points**")

st.subheader("Input Feature Values")
chart_data = pd.DataFrame(
    input_data.values.flatten(),
    index=FEATURES,
    columns=["Value"],
)
st.bar_chart(chart_data)
