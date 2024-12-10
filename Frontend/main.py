import streamlit as st
import joblib
import os

# Define input features and their constraints
st.title("Depression Prediction")

# Inputs
age = st.number_input("Age", min_value=16, max_value=35, step=1, format="%d")
cgpa = st.number_input("CGPA", min_value=0.0, max_value=4.0, step=0.01, format="%.2f")
semester_credit_load = st.number_input("Semester Credit Load", min_value=10, step=1, format="%d")
anxiety_score = st.slider("Anxiety Score", min_value=1, max_value=5, step=1)

major = st.selectbox("Major", ["business", "engineering", "law", "medical", "others"])

# Load model parameters based on selected major
model_params_path = f"Frontend/logistic_regression_{major}.pkl"

if os.path.exists(model_params_path):
    with open(model_params_path, 'rb') as file:
        model = joblib.load(file)
else:
    st.error("Model parameters for the selected major are not available.")
    st.stop()

# Predict button
if st.button("Predict"):
    # Prepare input data
    input_features = [[age, cgpa, semester_credit_load, anxiety_score]]

    # Make prediction
    prediction = model.predict(input_features)[0]

    # Display result
    if prediction == 0:
        st.success("The person is not depressed.")
    else:
        st.error("The person is depressed.")
