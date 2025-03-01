from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load dataset to create mappings
df = pd.read_csv("/Users/puspakd/ideatoh/Price_Agriculture_commodities_Week (1).csv")

# Create mapping dictionaries
state_map = {state: i for i, state in enumerate(set(df["State"]))}
district_map = {district: i for i, district in enumerate(set(df["District"]))}
market_map = {market: i for i, market in enumerate(set(df["Market"]))}
commodity_map = {commodity: i for i, commodity in enumerate(set(df["Commodity"]))}
grade_map = {grade: i for i, grade in enumerate(set(df["Grade"]))}

# Load the trained model
model = joblib.load("/Users/puspakd/ideatoh/RandomForestReg.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_price = None
    error_message = None

    if request.method == "POST":
        try:
            # Get inputs from form
            state = request.form["state"]
            district = request.form["district"]
            market = request.form["market"]
            commodity = request.form["commodity"]
            grade = request.form["grade"]
            day = int(request.form["day"])
            month = int(request.form["month"])
            year = int(request.form["year"])
            min_price = float(request.form["min_price"])  # Convert min_price to float

            # Print received inputs
            print(f"Received Input -> State: {state}, District: {district}, Market: {market}, Commodity: {commodity}, Grade: {grade}, Date: {day}-{month}-{year}, Min_price: {min_price}")

            # Convert text inputs to numerical using the mapping dictionaries
            if state in state_map:
                state_num = state_map[state]
            else:
                error_message = f"Invalid State: {state}"
                return render_template("index.html", error_message=error_message)

            if district in district_map:
                district_num = district_map[district]
            else:
                error_message = f"Invalid District: {district}"
                return render_template("index.html", error_message=error_message)

            if market in market_map:
                market_num = market_map[market]
            else:
                error_message = f"Invalid Market: {market}"
                return render_template("index.html", error_message=error_message)

            if commodity in commodity_map:
                commodity_num = commodity_map[commodity]
            else:
                error_message = f"Invalid Commodity: {commodity}"
                return render_template("index.html", error_message=error_message)

            if grade in grade_map:
                grade_num = grade_map[grade]
            else:
                error_message = f"Invalid Grade: {grade}"
                return render_template("index.html", error_message=error_message)

            # Print converted numerical values
            print(f"Converted Values -> State: {state_num}, District: {district_num}, Market: {market_num}, Commodity: {commodity_num}, Grade: {grade_num}, Date: {day}-{month}-{year}, Min_price: {min_price}")

            # Prepare input array including min_price
            ip = np.array([[state_num, district_num, market_num, commodity_num, grade_num, day, month, year, min_price]])

            # Make prediction
            predicted_price = model.predict(ip)[0]

        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)

    return render_template("index.html", predicted_price=predicted_price, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
