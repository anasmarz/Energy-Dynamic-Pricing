# Energy Pricing Prediction App

## Overview

The **Energy Pricing Prediction App** is a web application designed to predict real-time energy prices based on various input parameters. This app leverages machine learning to provide dynamic pricing information that can help in optimizing energy trading and consumption decisions.

## Features

- **Real-time Predictions**: Provides up-to-date energy price predictions based on current supply, demand, and other relevant features.
- **Machine Learning Integration**: Utilizes a trained machine learning model to make accurate price predictions.
- **Simple API Endpoint**: Offers a RESTful API endpoint to facilitate easy integration with other applications and services.

## API Endpoints

### `/predict_price`

**Method**: POST  
**URL**: `http://127.0.0.1:5000/predict_price`

#### Request

- **Content-Type**: `application/json`
- **Body**: JSON object with the following fields:
  - `current_supply` (number): Current energy supply.
  - `current_demand` (number): Current energy demand.
  - `hour` (number): Hour of the day (0-23).
  - `day_of_week` (number): Day of the week (0-6, where 0 is Monday).
  - `historical_price` (number): Historical energy price.

**Example Request Body**:

```json
{
  "current_supply": 3500,
  "current_demand": 3000,
  "hour": 14,
  "day_of_week": 2,
  "historical_price": 0.25
}
Response
Content-Type: application/json
Body: JSON object containing the predicted price.
Example Response:
```
```json

{
  "prediction": 0.275
}
```
How It Works
Model Training: The app uses a pre-trained machine learning model, which has been trained on historical data to predict energy prices.
Data Input: Users send a POST request with relevant data features to the /predict_price endpoint.
Prediction: The app processes the input data using the trained model to generate a price prediction.
Response: The app returns the predicted price in JSON format.
Getting Started
Run the Flask Server:

```bash
python your_flask_app.py
Ensure the server is running and listening on http://127.0.0.1:5000.
```
Send a Request:
Use curl, Postman, or any HTTP client to send a POST request to the /predict_price endpoint with the necessary JSON body.

Requirements
Python 3.x
Flask
scikit-learn
pickle
