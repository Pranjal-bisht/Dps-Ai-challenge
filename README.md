# Dps-Ai-challenge
# Task:

To Use Machine Learning to predict No. of accidents, vizualize historical trends and Create a web app to take inputs and display the predicted no. of accidents and also create an endpoint for the same accepting a post request.

# How to get started
     You should have access to this private repository
     
     Clone this repository in your local PC.
     You should have python version 3.9 or below because , Nagisa library function only for those versions. After that type followings codes in the terminal ( you root directory should be ./boq-AI)
     pip install -r requirements.txt
     streamlit run app.py
  
# Index

- [Problem Description](#Problem-description)
- [Data and Features](#Data-and-Features)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Approach](#Approach)
- [Architecture](#Architecture)
- [Model Training & Evaluation](#Architecture)
- [Model deployment using Flask](#Model-deployment-using-Flask)
v

# Technologies Used:
<div align="center">
<code><img height="100" src="https://camo.githubusercontent.com/fc4cab9ccd5e6e62ac62dbb5aab11a9e5507b438c42cc82363ce184cbe1ccdaa/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e7376672f3230303070782d507974686f6e2d6c6f676f2d6e6f746578742e7376672e706e67" /></code>
<code><img height="80" src="https://www.kdnuggets.com/wp-content/uploads/jupyter-logo.jpg" /></code>
<code><img height="80" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" /></code>
 </div>
 <code><img height="80" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBRvVI-sI9TOKK-rUH_brvWmIzadLVcPM2s7YbjXuvcROdbKUkBLdk03fR5XURuYGzQ7E&usqp=CAU" /></code>
 </div>
 
## Problem Description ##
Download the “Monatszahlen Verkehrsunfälle” Dataset from the München Open Data Portal. Here you see the number of accidents for specific categories per month. Important are the first 5 columns:
Category
Accident-type (insgesamt means total for all subcategories)
Year
Month
Value

Your goal would be to visualise historically the number of accidents per category (column1). The dataset currently contains values until the end of 2020. Create an application that forecasts the values for:

Category: 'Alkoholunfälle'
Type: 'insgesamt
Year: '2021'
Month: '01'

## Data and Features ##
![image]()

The files consist of a list of product listings in csv format with 9 columns. We dont need to do feature selection here as the important features are already mentioned to be used, i.e. first 5.
1. MONATSZAHL - accident category
2. AUSPRÃ„GUNG - accident type.
3. JAHR - Year.
4. MONAT - date of accident
5. WERT - value


## Exploratory Data Analysis ##
![image](https://user-images.githubusercontent.com/58468853/225210375-e9b6ff1a-b7c1-452e-baf2-5ac01fde51d4.png)
![image](https://user-images.githubusercontent.com/58468853/225210418-31300d6d-0e51-4953-8f12-3fd3f70dfada.png)

![image](https://user-images.githubusercontent.com/58468853/225210491-80e749b7-78f4-4640-8972-6c006057c778.png)
![image](https://user-images.githubusercontent.com/58468853/225210532-f6a5cc93-2b19-4863-a502-a69a193801a0.png)
![image](https://user-images.githubusercontent.com/58468853/225210587-5e0662e0-8964-4d7a-8b21-64bcc40cfd04.png)
![image](https://user-images.githubusercontent.com/58468853/225210617-69fea38b-25fb-43ee-9af4-a4b4b40032ed.png)

## Approach ##
<br/>

# Application of Data:

![image]()
<br/>

# Machine Learning Work Flow:


 ![flow](https://user-images.githubusercontent.com/58468853/225127835-051ff3fe-5e8d-4488-9424-4beee0bf42d5.JPG)


## Architecture ##

![model architecture](https://user-images.githubusercontent.com/58468853/225127876-2951cd53-478d-4953-bd74-58102a145b7b.JPG)


## Model Training & Evaluation ##


## Model deployment using Flask ##
![website](https://user-images.githubusercontent.com/58468853/225128058-6913ae4e-f934-4f6c-9c2b-dcacafe80eb4.JPG)


# Website deployed on Streamlit:
![webapp](https://user-images.githubusercontent.com/58468853/225128038-01597c5f-0f09-4a62-b332-455a9d03ac6f.JPG)

# Links:
website : https://pranjal-bisht-dps-ai-challenge-app-pe1c2h.streamlit.app/
<br/>
endpoint : http://ec2-13-50-14-108.eu-north-1.compute.amazonaws.com:5000/endpoint
