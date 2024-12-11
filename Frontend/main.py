import streamlit as st
import joblib
import pandas as pd
import os

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.regularizers import l1, l2
from tensorflow.keras.optimizers import SGD

N_FEATURES = 4
def build_model(num_layers, num_neurons, activation, momentum, reg_method, reg_rate, learning_rate):
    regularizer = l1(reg_rate) if reg_method=='l1' else l2(reg_rate)

    model = Sequential()

    # Input layer
    model.add(Input((N_FEATURES,)))
    # Hidden layers
    for _ in range(num_layers):
        model.add(Dense(num_neurons, activation=activation, kernel_regularizer=regularizer))
    # Output layer
    model.add(Dense(1, activation='sigmoid'))

    optimizer = SGD(learning_rate=learning_rate, momentum=momentum)
    loss_string = 'binary_crossentropy'
    model.compile(loss=loss_string, optimizer=optimizer, metrics=['accuracy'])
    return model

# Define input features and their constraints
st.title("Depression Prediction")

# Inputs
age = st.number_input("Age", min_value=16, max_value=35, step=1, format="%d")
cgpa = st.number_input("CGPA", min_value=0.0, max_value=4.0, step=0.01, format="%.2f")
semester_credit_load = st.number_input("Semester Credit Load", min_value=10, step=1, format="%d")

major = st.selectbox("Major", ["business", "engineering", "law", "medical", "others"])

if(major=="business"):
    modelName="Support Vector Machine"
    modelType= "SVC"
elif(major=="engineering"):
    modelName="Support Vector Machine"
    modelType="SVC"
elif(major=="law"):
    modelName="Naive Bayes"
    modelType="GaussianNB"
elif(major=="medical"):
    modelName="Neural Network"
    modelType="KerasClassifier"
elif(major=="others"):
    modelName="K-Nearest Neigbors Classifier"
    modelType="KNeighborsClassifier"
else:
    modelName="Error"
    modelType="Error"

# Load model parameters based on selected major
model_params_path = f"Frontend/{modelType}_{major}_model.pkl"
scaler_params_path = f"Frontend/{modelType}_{major}_scaler.pkl"

st.text(f"Model used for {major} major is {modelName}")

if os.path.exists(model_params_path) and os.path.exists(scaler_params_path):
    with open(model_params_path, 'rb') as model_file:
        model = joblib.load(model_file)
    with open(scaler_params_path, 'rb') as scaler_file:
        scaler = joblib.load(scaler_file)
else:
    st.error("Model or scaler parameters for the selected major are not available.")
    st.stop()

# Predict button
if st.button("Predict"):
    input_features = [[age, cgpa, semester_credit_load]]
    feature_names = ["Age", "CGPA", "Semester_Credit_Load"]

    input_df = pd.DataFrame(input_features, columns=feature_names)
    scaled_features = scaler.transform(input_df)

    prediction = model.predict(scaled_features)[0]

    if prediction == 0:
        st.success("The person is not depressed.")
    else:
        st.error("The person is depressed.")
