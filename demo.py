import joblib # type: ignore
import numpy as np

# Load the saved model and scaler
model, scaler = joblib.load("wine_quality_model.pkl")

# Hardcoded sample data (fixed acidity, volatile acidity, ..., alcohol)
sample_data = np.array([
    [7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4],
    [8.5, 0.28, 0.56, 1.8, 0.092, 35.0, 103.0, 0.9969, 3.3, 0.75, 10.5],
    [6.7, 0.58, 0.08, 1.8, 0.097, 15.0, 65.0, 0.9959, 3.28, 0.54, 9.2]
])

# Scale the sample data
sample_data_scaled = scaler.transform(sample_data)

# Predict wine quality
predictions = model.predict(sample_data_scaled)

# Display results
for i, quality in enumerate(predictions):
    print(f"Sample {i+1} - Predicted Wine Quality: {quality}")
