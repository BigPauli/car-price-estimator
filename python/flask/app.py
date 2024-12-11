from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import tensorflow as tf
from joblib import load

# create app
app = Flask(__name__)
print(__name__)
# general help from: 
# https://www.geeksforgeeks.org/how-to-use-css-in-python-flask/
# https://stackoverflow.com/questions/19794695/flask-python-buttons
# https://www.geeksforgeeks.org/how-to-use-web-forms-in-a-flask-application/
# https://www.w3schools.com/tags/tag_select.asp
# https://getbootstrap.com/docs/5.3/getting-started/introduction/
# https://flask.palletsprojects.com/en/stable/
# https://python-web.teclado.com/section07/lectures/06_jinja2_conditional_statements/

# we need to get these from the user:
# Levy: positive int
# Production year: positive int
# Leather interior: boolean
# Engine volume: positive float
# Mileage: positive int
# Cylinders: positive int
# Airbags: positive int
# Turbo: boolean
# Manufacturer: checklist containing HYUNDAI, TOYOTA, MERCEDES-BENZ, CHEVROLET, FORD, BMW, HONDA, LEXUS, NISSAN, VOLKSWAGEN, SSANGYONG, KIA, OPEL, Other, MITSUBISHI, SUBARU, AUDI, MAZDA, JEEP, DAEWOO, DODGE, SUZUKI, FIAT, PORSCHE, LAND ROVER, VAZ
# Category: checklist containing Sedan, Jeep, Hatchback, Minivan, Coupe, Universal, Microbus, Goods wagon, Pickup, Cabriolet, Limousine
# Fuel type: checklist containing Petrol, Diesel, Hybrid, LPG, CNG
# Gear box type: checklist containing Automatic, Tiptronic, Manual, Variator
# Drive wheels: checklist containing Front, 4x4, Rear
# Color: Black, White, Silver, Grey, Blue, Other



@app.route("/", methods=["GET", "POST"])
def index():

    data = request.form
    if data:
        # making the data dictonary to be shown to the user more readable
        display_data = {key[5].upper() + " ".join(key.split("_")[1:])[1:]: val for key, val in data.items()}
        
        # remove accidental argument that was added
        if "Tutton" in display_data:
            del display_data["Tutton"]

        # manually go through each of the necessary columns to create the pandas DataFrame and put the relevant information into a dictionary
        car_data = []

        car_data.append(int(data["user_levy"]))
        car_data.append(int(data["user_production_year"]))
        car_data.append(int(data["user_leather_interior"]))
        car_data.append(float(data["user_engine_volume"]))
        car_data.append(int(int(data["user_mileage"]) * 1.60934)) # convert from miles to km
        car_data.append(int(data["user_cylinders"]))
        car_data.append(int(data["user_airbags"]))
        car_data.append(int(data["user_turbo"]))

        # get the user's car manufacturer
        for manufacturer in ['AUDI', 'BMW', 'CHEVROLET', 'DAEWOO', 'DODGE', 'FIAT', 'FORD', 'HONDA', 'HYUNDAI', 'JEEP',
       'KIA', 'LAND ROVER', 'LEXUS', 'MAZDA', 'MERCEDES-BENZ', 'MITSUBISHI', 'NISSAN', 'OPEL', 'Other', 'PORSCHE', 'SSANGYONG',
       'SUBARU', 'SUZUKI', 'TOYOTA', 'VAZ', 'VOLKSWAGEN']:
            if data["user_manufacturer"] == manufacturer:
                car_data.append(1)
            else:
                car_data.append(0)

        # get the user's car category
        for category in ['Cabriolet', 'Coupe', 'Goods wagon', 'Hatchback', 'Jeep', 'Limousine', 'Microbus', 'Minivan', 'Pickup', 'Sedan', 'Universal']:
            if data["user_category"] == category:
                car_data.append(1)
            else:
                car_data.append(0)

        # get the user's fuel type
        for fuel_type in ['CNG', 'Diesel', 'Hybrid', 'LPG', 'Petrol']:
            if data["user_fuel_type"] == fuel_type:
                car_data.append(1)
            else:
                car_data.append(0)

        # get the user's gear box type
        for gear_box_type in ['Automatic', 'Manual', 'Tiptronic', 'Variator']:
            if data["user_gear_box_type"] == gear_box_type:
                car_data.append(1)
            else:
                car_data.append(0)

        # get the user's drive wheels
        for drive_wheel in ['4x4', 'Front', 'Rear']:
            if data["user_drive_wheels"] == drive_wheel:
                car_data.append(1)
            else:
                car_data.append(0)

        # get the user's color
        for color in ['Black', 'Blue', 'Grey', 'Other', 'Silver', 'White']:
            if data["user_color"] == color:
                car_data.append(1)
            else:
                car_data.append(0)

        # reshape car_data
        car_data = np.array(car_data).reshape(1, -1)

        # load the smart model and scalers
        nn = tf.keras.models.load_model("../models/smart_model.keras")
        X_scaler = load("../../data/X_scaler.bin")
        y_scaler = load("../../data/y_scaler.bin")


        print("Number of features expected by scaler:", X_scaler.n_features_in_)
        print("Mean shape:", X_scaler.mean_.shape)
        print("Var shape:", X_scaler.var_.shape)

        # scale the data
        scaled_data = X_scaler.transform(car_data)

        # make prediction using scaled data
        predicted_price_scaled = nn.predict(scaled_data)

        # inverse transform prediction to make it resemble dollars
        predicted_price = round(y_scaler.inverse_transform(predicted_price_scaled)[0][0], 2)

    else:
        # setting defaults for the first time the user opens the application
        display_data = {}
        predicted_price = ""
    return render_template("index.html", predicted_price=predicted_price, display_data=display_data)

# if this script is being run, open the webpage
if __name__ == "__main__":
    app.run()
