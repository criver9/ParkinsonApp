
# -*- coding: utf-8 -*-



import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
pickle_in = open("classifierTap.pkl","rb")
classifierTap=pickle.load(pickle_in)


#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predictionParkinson(age,Male,MemoryPerformance,TapPerform):
    
    
    prediction=classifier.predict([[age,Male,MemoryPerformance]])
    predictionTap=classifierTap.predict([[TapPerform, age,Male]])
    
    if prediction==1 & predictionTap==0:
        pred=0
    elif prediction==0 & predictionTap==0:
        pred=1
    elif prediction==1 & predictionTap==0:
        pred=2
    else:
        pred=3            
    return pred



def main():
    st.title("AM Parkinson")
    #html_temp = """
    #<div style="background-color:tomato;padding:10px">
    #<h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    #</div>
    #"""
    #st.markdown(html_temp,unsafe_allow_html=True)
    Im=Image.open("PicApp.jpg")
    st.image(Im,width=300)
    
    age = st.text_input("Age","Type Here")
    Male = st.text_input("Gender: 1 if Male, 0 if Female","Type Here")
    MemoryPerformance = st.text_input("Memory Performance","Type Here")
    TapPerform = st.text_input("Tapping Performance","Type Here")
    result=""
    if st.button("Should I stay alert?"):
        result=predictionParkinson(int(age),int(Male),int(MemoryPerformance),int(TapPerform))
        if result==0:
            st.success('You do not present Parkinson related symptoms')
        elif result==1:
            st.success('Based on your Tap performance, you should stay alert and visit your doctor')
        elif result==2:
            st.success('Based on your Memory performance, you should stay alert and visit your doctor') 
        else:       
            st.success('Based on your general performance, you should stay alert and visit your doctor')

if __name__=='__main__':
    main()