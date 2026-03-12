import streamlit as st

import joblib 
import pandas as pd
try:
 
   model = joblib.load("Mobile_price.joblib")
except:
    st.error("Model file not found! ")
df = pd.read_csv("Flipkart_Mobiles.csv")
df = df.dropna()

st.title("Mobile Price Prediction")
st.image("MOBILE_Photo.jpg", width=1000)
st.sidebar.header("Dataset Information")

st.sidebar.write("Total Mobiles:", df.shape[0])
st.sidebar.write("Total Brands:", df['Brand'].nunique())
st.sidebar.write("Total Models:", df['Model'].nunique())




brand = st.selectbox("Select Brand", sorted(df['Brand'].unique()))
df_brand = df[df['Brand'] == brand]

m = st.selectbox("Select Model", sorted(df_brand['Model'].unique()))
df_model = df_brand[df_brand['Model'] == m]

color = st.selectbox("Select Color", df_model['Color'].unique())
df_color = df_model[df_model['Color'] == color]

memory = st.selectbox("Select Ram", df_color['Memory'].unique())
df_memory = df_color[df_color['Memory'] == memory]

storage = st.selectbox("Select Storage", df_memory['Storage'].unique())
rating = st.slider("Select Rating",1.0, 5.0, 4.0, 0.2)

if st.button("Predict Price "):
    input_df = pd.DataFrame({ 
    "Brand":[brand],
    "Model":[m],
    "Color":[color],
    'Memory':[memory],
    'Storage':[storage],
    'Rating':[rating]
    })

    st.subheader("Selected Mobile")
    st.write("Brand:", brand)
    st.write("Model:", m)
    st.write("Color:", color)
    st.write("RAM:", memory)
    st.write("Storage:", storage)
    st.write("Rating:", rating)
    prediction = model.predict(input_df)
    st.success(f"Prediction Price : ₹ {prediction[0]:,.0f} " )
st.markdown("---")
st.markdown("Developed by **Arun Kumar** | Data Analyst Project") 