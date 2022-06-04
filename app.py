import streamlit as st
import pickle
import numpy as np
import sklearn

model_reg=pickle.load(open("model_class",'rb'))
model_class=pickle.load(open("model_reg",'rb'))
st.title("PREDICTION")
RH=st.text_input("Relative Humidity")
WS=st.text_input("Wind speed")
Rain=st.text_input(" Rain")
FFMC=st.text_input('Fine Fuel Moisture Code')
DMC=st.text_input("Duff Moisture Code")
DC=st.text_input("Drought Code")
ISI=st.text_input("Initial Spread Index")
BUI=st.text_input("Buildup Index ")
FWI= st.text_input("Fire Weather Index")
def predict_temp():
       return model_class.predict(np.array([float(RH), float(WS), float(Rain), float(FFMC), float(DMC),float(DC),float(ISI),float(BUI),float(FWI)]).reshape(1,-1))[0]
def predict_fire():
       return model_reg.predict(np.array([float(RH), float(WS), float(Rain), float(FFMC), float(DMC),float(DC),float(ISI),float(BUI),float(FWI)]).reshape(1,-1))[0]

if st.button("Predict_Temperature"):
       st.write(predict_temp())
if st.button("Predict_Chances_of_fire"):
       st.write(predict_fire())
