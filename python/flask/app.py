from flask import Flask, render_template, request
from joblib import load

# create app
app = Flask(__name__)

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
    print(data)
    if data:
        # making the data dictonary more readable
        car_data = {" ".join(key.split("_")[1:]).title(): str(val).title() for key, val in data.items()}

        # TODO: take the user's data, put it into the same form as the input data the model received, scale it, make a prediction, and then return the prediction to the user
        # MAKE SURE TO CONVERT MILEAGE TO KM FROM MILES BEFORE FEEDING TO MODEL

        # calculate price
        if data["submit_button"] == "smart":
            predicted_price = "smart"
        else:
            predicted_price = "dumb"
    else:
        # setting defaults for the first time the user opens the application
        car_data = {}
        predicted_price = ""
    return render_template("index.html", predicted_price=predicted_price, car_data=car_data)

# if this script is being run, open the webpage
if __name__ == "__main__":
    app.run()
