import streamlit as st
st.title("MEDICAL DIAGNOSIC WEB APP")
st.subheader('is the patient Diabetic?')
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

#step1: load the pickled model
model=open('rfc.pickle','rb')
clf=pickle.load(model)
model.close()
#step2: get the input from the frontend user
pregs=st.number_input('Pregnancies',0,170)
glucose=st.slider('Glucose',40,200,40)
BP=st.slider('BloodPressure',20,140,20) 
skin_thickness=st.slider('SkinThickness',7.0,99.0,7.0) 
insulin=st.slider('Insulin',14,850,14)
BMI=st.slider('BMI',18,67,18)
DPF=st.slider('DiabetesPedigreeFunction',0.05,2.5,0.05) 
age=st.slider('Age',20,90,20)

#step3: collect the fromend user input as model input data
data={
    'Pregnancies':pregs,'Glucose':glucose,
    'BloodPressure':BP,'SkinThickness':skin_thickness,
    "Insulin":insulin,'BMI':BMI,'DiabetesPedigreeFunction':DPF,
    'Age':age
}
input_data=pd.DataFrame([data])
#step 4 get the predictions and print the result
preds=clf.predict(input_data)[0]
if st.button("predict"):
    if preds==1:
        st.error("diabetic")
    if preds==0:
        st.success("non diabetic")
