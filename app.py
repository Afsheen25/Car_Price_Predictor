import streamlit as st
import joblib
import pandas as pd

model = joblib.load("car_price_predictor.pkl")

st.title("🚗 Car Price Predictor")
st.markdown("Enter car details below to estimate MSRP:")

make = st.selectbox("Make", ["Ford", "BMW", "Audi", "Honda", "Toyota","Volkswagen"])
engine_hp = st.slider("Engine HP", 60, 1000, 200)
engine_cyl = st.selectbox("Engine Cylinders", [3, 4, 6, 8, 10, 12])
year = st.slider("Year", 1990, 2020, 2015)
highway = st.slider("Highway MPG", 10, 60, 30)
city = st.slider("City MPG", 5, 50, 20)
doors = st.selectbox("Number of Doors", [2.0, 4.0])
popularity = st.slider("Popularity", 0, 6000, 1000)


power_pc = engine_hp / engine_cyl
mpg_ratio = highway / city

input_df = pd.DataFrame({
    "Make": [make],
    "Engine HP": [engine_hp],
    "Engine Cylinders": [engine_cyl],
    "power_per_cylinder": [power_pc],
    "Year": [year],
    "mpg_ratio": [mpg_ratio],
    "Popularity": [popularity],
    "Number of Doors": [doors],
    "highway MPG": [highway],
    "city mpg": [city]
})

if st.button("Predict"):
    price = model.predict(input_df)[0]
    st.success(f"💰 Estimated MSRP: ${price:,.2f}")
