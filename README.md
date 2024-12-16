# car-price-estimator

#### main.py
Main program that runs the Flask website on the local server.

## python/

### models/

#### optimized_model.ipynb
Notebook that contains the exploration and cleaning of the dataset used to create the neural network model. Also includes the creation of the neural network model and standard scaler.

#### smart_model.keras
The smart model itself.

#### smart_model_history/
The save date of the training history of the smart model.

#### unoptimized_model.ipynb
Notebook that contains a completely unoptimized model. This model is not used elsewhere in the project and is to show the importance of data cleaning and tuning the parameters of a neural network model.

#### stupid_model.keras
The unoptimized model itself.

### flask/

#### app.py
Contains the logic for the Flask application. This includes loading the smart model and predicting the user's car's value from their inputs on the webpage.

#### templates/index.hmtl
HTML for the singular webpage in the Flask application.

#### static/style.css
CSS stying for the singular webpage in the Flask application.

## data/

#### car_price_prediction.csv
The data used to create both the smart and stupid models. Source: https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge/data

#### X_scaler.bin
Input scaler for the smart model.

#### y_scaler.bin
Prediction scaler for the smart model.

#### stupid_X_scaler.bin
Input scaler for the stupid model.

#### stupid_y_scaler.bin
Prediction scaler for the stupid model.

All code included in this project is entirely my own. Any help received from the internet was cited in comments near the related code.