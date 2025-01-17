import streamlit as st
import pickle

tfidf=pickle.load(open('vector.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.header("Email/SMS Spam Classifier")
input_sms=st.text_area("Enter the message")

if st.button('Predict'):
    vector_input=tfidf.transform([input_sms])
    result=model.predict(vector_input)[0]

    if result==1:
        st.subheader("Spam")
    else:
        st.subheader("Not a Spam")