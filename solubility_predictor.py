from sklearn.linear_model import LinearRegression
import numpy as np

# Temperature (°C)
X = np.array([[10], [20], [30], [40], [50]])

# Solubility (example data)
y = np.array([20, 30, 45, 65, 90])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Input temperature
temp = float(input("Enter temperature (°C): "))

# Predict solubility
prediction = model.predict([[temp]])

print("Predicted Solubility:", round(prediction[0], 2), "g/100mL")
