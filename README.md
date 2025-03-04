# Vegetable Price Prediction in India 🥦📈

### A Machine Learning Model for Predicting Vegetable Prices in India

![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)

---

## 📝 Model Description

This model predicts vegetable prices in India based on various factors such as **seasonality, market trends, demand, supply, and historical pricing data**. It is designed to assist **farmers, retailers, and policymakers** in understanding market fluctuations and optimizing their decisions.

---

## 📂 Model Details

- **Model Name:** Vegetable Price Prediction in India  
- **Architecture:** Random Forest  
- **Framework:** Scikit-learn  
- **Trained on:** CPU with dataset of 23091 rows  

---

## 🗂 Model Usage

You can use this model directly with Hugging Face’s `transformers` or via `pickle` if it's a scikit-learn model.

### ➡️ Using the Model in Python

```python
import pickle

# Load the model
with open("vegetable_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example input (Replace with actual data)
sample_input = [[2025, "Tomato", "Delhi", "Winter", 3000]]  # Year, Vegetable, Location, Season, Supply

# Predict price
predicted_price = model.predict(sample_input)
print(f"Predicted Price: {predicted_price[0]}")
```

---

## 📊 Training Information

- **Feature Engineering:** Handled missing values, normalized price variations, one-hot encoded categorical variables.  
- **Hyperparameter Tuning:** Used GridSearchCV for optimal parameter selection.  
- **Performance Metrics:**  
  - **Mean Absolute Error (MAE):** X.XX  
  - **Root Mean Squared Error (RMSE):** X.XX  
  - **R² Score:** X.XX  

---

## 📌 How to Use This Model on Hugging Face Hub?

1️⃣ **Clone the Repository:**  
```sh
git clone https://huggingface.co/AKing-283/Vegetable-price-prediction-in-India
```

2️⃣ **Install Dependencies:**  
```sh
pip install -r requirements.txt
```

3️⃣ **Load the Model & Run Predictions** (See Python code snippet above)  

---

## 💅 Download Model Files

You can download the model files directly from **Hugging Face**:  
📞 **[Vegetable Price Prediction Model](https://huggingface.co/AKing-283/Vegetable-price-prediction-in-India)**  

---

## 📝 Model Card Metadata

```yaml
---
language: en
tags:
  - machine-learning
  - regression
  - price-prediction
license: mit
datasets: custom
model-index:
  - name: Vegetable Price Prediction in India
    results:
      - task:
          type: regression
        dataset:
          name: Custom Dataset
          type: custom
---
```

---

## 👨‍💻 Author & Contributions

- **Author:** Puspak Dakkata,, Vijay Madiwal, Pranal  Vernekar, Prasad Kotian  
- **GitHub Repo:**  
- **Contact:** dpreddy294@gmail.com  

If you find this model useful, feel free to ⭐ the repo and share your feedback! 😊  

---

## 💚 License

This project is released under the **MIT License**.

