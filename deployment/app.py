import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image


# Create a function to display the UI
def run():
    st.title("Accident prediction system")

    # Add inputs for the user to specify values
    st.header("Enter the input values")

    options_for_category = st.selectbox(
    "Category", ("Alkoholunf√§lle","Fluchtunf√§lle","Verkehrsunf√§lle")
    )

    options_for_accident = st.selectbox(
        "Accident_type", ("insgesamt","mit Personensch√§den","Verletzte und Get√∂tete")
    )

    year = st.number_input("JAHR")

    options_for_month = st.selectbox(
         "Monat", (1,2,3,4,5,6,7,8,9,10,11,12)
    )

    en_cat = 2
    if options_for_category == 'Alkoholunf√§lle':
       en_cat = 0
    elif options_for_category == 'Fluchtunf√§lle':
       en_cat = 1
    
    en_type = 2
    if options_for_accident == 'insgesamt':
       en_type = 0
    elif options_for_accident == 'mit Personensch√§den':
       en_type = 1

    # Create a Pandas dataframe with the inputs
    input_data = [[en_cat, en_type, int(year),int(options_for_month)]]
    
    input_data = np.array(input_data)
     
    
    with open('C:/files/Dps-Ai-challenge/deployment/model.pkl', 'rb') as f:
         model = pickle.load(f)

    

    # Display the prediction
    st.subheader("Prediction")

    if st.button("forecast"):
       print(input_data)  
       # Make a prediction
       prediction = model.predict(input_data)
       if input_data[0][0]== 0:
          st.image(Image.open('C:/files/Dps-Ai-challenge/Alkoholunfalle.png'))
       elif input_data[0][1] == 1:
          st.image(Image.open('C:/files/Dps-Ai-challenge/Fluchtunfälle.png'))
       else :
          st.image(Image.open('C:/files/Dps-Ai-challenge/Verkehrsunfälle.png'))

       st.write('The forecasted number of accidents are' , int(prediction[0]))



if __name__ == '__main__':
    run()