import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained Random Forest model
rf_model = joblib.load("/Users/puspakd/ideatoh/random_forest_model (1).pkl")

# Streamlit UI
st.title("Agri-Horticultural Price Prediction")

st.write("### Enter Last 7 Days' Prices (Comma-Separated):")
prices_input = st.text_input("Example: 100, 102, 101, 105, 107, 110, 112")

if st.button("Predict"):
    try:
        # Process user input
        recent_prices = prices_input.split(",")
        recent_prices = [float(price.strip()) for price in recent_prices]

        if len(recent_prices) != 7:
            st.error("Please enter exactly 7 values!")
        else:
            # Convert to array
            recent_prices = np.array(recent_prices).reshape(1, -1)

            # Predict next 30 days
            future_prices = []
            for _ in range(30):
                next_price = rf_model.predict(recent_prices)[0]
                future_prices.append(next_price)

                # Update input data
                recent_prices = np.append(recent_prices[:, 1:], next_price).reshape(1, -1)

            # Generate future dates
            future_dates = pd.date_range(start=pd.Timestamp.today(), periods=30, freq='D').strftime("%Y-%m-%d").tolist()

            # Display results
            st.write("## Predicted Prices for Next 30 Days")
            future_data = pd.DataFrame({"Date": future_dates, "Predicted Price": future_prices})
            st.dataframe(future_data)

            # Plot the predictions
            st.line_chart(future_data.set_index("Date"))

    except Exception as e:
        st.error(f"Error: {str(e)}")
