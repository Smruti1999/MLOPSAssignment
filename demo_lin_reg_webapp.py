import streamlit as st
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web app
st.header("Streamlit demo")

st.sidebar.header("This is a web app")

age = st.sidebar.slider("Select Age to get Salary", 1, 50, 5)

st.write("Age is:", age)

salary = model.predict([[age]])

st.write("Salary is", salary)
