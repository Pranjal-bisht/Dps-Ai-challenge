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
![1](https://user-images.githubusercontent.com/58468853/225127497-05141808-c9f6-464b-870b-4821ad5f1763.png)
![2](https://user-images.githubusercontent.com/58468853/225127544-9c06e706-88de-4c23-b79f-9c818e77ed1e.png)

![3](https://user-images.githubusercontent.com/58468853/225127568-357ad0cc-0612-4707-956f-24566a1721a8.png)
![4](https://user-images.githubusercontent.com/58468853/225127593-5327502d-672e-4198-b53d-d81ec8f0365e.png)
![5](https://user-images.githubusercontent.com/58468853/225127609-7cbbafee-0a19-4f92-ae27-b59f7753cf8f.png)
![6](https://user-images.githubusercontent.com/58468853/225127628-18cf3a35-1f10-4dea-8158-497396f92f8e.png)

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
endpoint : http://ec2-13-50-14-108.eu-north-1.compute.amazonaws.com:5000/endpoint
