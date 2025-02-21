import pandas as pd
import numpy as np
import joblib # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.metrics import accuracy_score # type: ignore

# Load the dataset
file_path = "WineQT.csv"  # Change this to your actual CSV file path
df = pd.read_csv(file_path)

# Drop the 'Id' column as it's not useful for prediction
df.drop(columns=['Id'], inplace=True)

# Split features and target variable
X = df.drop(columns=['quality'])
y = df['quality']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model and scaler
joblib.dump((model, scaler), "wine_quality_model.pkl")
print("Model saved as 'wine_quality_model.pkl'")
