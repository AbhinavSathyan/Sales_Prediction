import streamlit as st
import pandas as pd
import numpy as np



import matplotlib.pyplot as plt
import seaborn as sns
import pickle

#Calling the model we saved above:

pickle_in = open('linearRegr1.pkl', 'rb')
classifier = pickle.load(pickle_in)
#Creating the UI for the application:


st.title('Sales Prediction Using Linear Regression')
st.text('Enter value to get expected sales')
name = st.text_input("Name:")
tv = st.number_input("TV")
radio= st.number_input("RADIO")
news= st.number_input("NEWSPAPER")
submit = st.button('Predict')
if submit:
    prediction = classifier.predict([[tv,radio,news]])
    st.write('Possible Sales will be ',prediction)
