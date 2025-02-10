import streamlit as st
import pandas as pd 
import pickle
import numpy as np
from PIL import Image

# load the file 
   
with open(r"F:\Cardheko project\random_forest_model.pkl", 'rb') as file:
    model = pickle.load(file)

car_data = pd.read_csv(r"F:\Cardheko project\cardata.csv")
cardeatils = pd.read_csv(r"F:\Cardheko project\cardeatils.csv")

#setting up streamlit page
brand_dict = {'Kia':13, 'Maruti':20, 'Nissan':24, 'Hyundai':9, 'Honda':8, 'Mercedes-Benz':21, 'BMW':1, 'Ford':6, 'Tata':29, 'Jeep':12,
              'Toyota':30, 'Audi':0, 'Mahindra':17, 'Renault':27, 'Cherovolt':2, 'Volkswagen':31, 'Datsun':4, 'Fiat':5, 'Land Rover':14,
               'MG':16, 'Skoda':28, 'Isuzu':10, 'Mini':22, 'Volvo':32, 'Jaguar':11, 'Citroen':3, 'Mitsubishi':23, 'Mahindra Renault':18,
                'Mahindra Ssangyong': 19, 'Lexus':15, 'Opel':25, 'Hindustan Motors':7, 'Porsche':26}
transs_dict = {'Automatic':0, 'Manual':1 }
city_dict = {'Banglore':0, 'Chennai':1, 'Delhi':2, 'Hyderabad':3, 'Jaipur':4, 'Kolkata':5}
fuel_dict = {'Cng':0, 'Diesel':1, 'Electric':2, 'Lpg':3, 'Petrol':4}

st.set_page_config(layout="wide")
st.title(":blue[PheoniX Used Car Price Predction App]")
st.markdown('''
            Welcome to Car Value Predictor! Let's help you find accurate car prices quickly and easily... 
            * :red[Let's find your car's true value today!]
            ''')

brand_inp= st.sidebar.selectbox('Brand 🚗',car_data["Brand"].value_counts().index)
brand = brand_dict[brand_inp]

trans_inp = st.sidebar.selectbox('Transmission',car_data["transmission"].value_counts().index)
transmission = transs_dict[trans_inp]

city_inp = st.sidebar.selectbox('City', car_data["City"].value_counts().index )
City = city_dict[city_inp]

fuel_inp = st.sidebar.selectbox('Fuel_type', car_data["Fuel_Type"].value_counts().index)
fuel = fuel_dict[fuel_inp]

Registration_Year = st.sidebar.slider('Year', cardeatils["Registration_Year"].min(),cardeatils["Registration_Year"].max())
Mileage = st.sidebar.slider('Mileage', cardeatils["Mileage"].min(),cardeatils["Mileage"].max())
Km = st.sidebar.slider('Km', cardeatils['km'].min(), cardeatils["km"].max())
Engine = st.sidebar.slider('Engine', cardeatils['Engine'].min(), cardeatils["Engine"].max())
Max_power = st.sidebar.slider('Max Power',cardeatils['Max_Power'].min(), cardeatils["Max_Power"].max())
Seating_Capacity = st.sidebar.slider('Seating Capacity', cardeatils["Seats"].min(),cardeatils["Seats"].max())
OwnerNo = st.sidebar.slider('Owner', cardeatils["ownerNo"].min(), cardeatils["ownerNo"].max())


input_arry = np.array([brand, transmission,City,Registration_Year,fuel,Mileage,Km,Engine,Max_power,Seating_Capacity,OwnerNo]).reshape(1, -1) 


col1 , col2, col3 = st.columns(3)
with col1:
    image1 = Image.open("E:\cardheko\download.jpg")
    st.image(image1)
with col2:
    image2 = Image.open("E:\cardheko\images.jpg")
    st.image(image2)
with col3:
    image3 = Image.open("E:\cardheko\images (1).jpg")
    st.image(image3)

predict = st.button("Predict the Price")


if predict:
    prediction = model.predict(input_arry)
    price = float(prediction)
    write = f'The predicted price of the car {brand_inp} is ₹ {price:.2f} lakhs 🚙' # showing the price prediction.
    st.success(write)
    st.balloons()