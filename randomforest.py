# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load the dataset (replace 'your_data.csv' with the actual dataset file)
# Ensure that your dataset file includes columns for features and target variables (speed, steering angle)
data = pd.read_csv('./dbnet_dataset.csv')

# Extract features and target variables
X = data[['video_feature1', 'video_feature2']]  # Replace 'feature1', 'feature2', ... with actual feature names
y_speed = data['vehicle_speed']
y_angle = data['steering_angle']

# Split the dataset into training and testing sets
X_train_speed, X_test_speed, y_train_speed, y_test_speed = train_test_split(X, y_speed, test_size=0.2, random_state=42)
X_train_angle, X_test_angle, y_train_angle, y_test_angle = train_test_split(X, y_angle, test_size=0.2, random_state=42)

# Initialize Random Forest models for speed and steering angle
rf_speed = RandomForestRegressor(n_estimators=100, random_state=42)
rf_angle = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the models
rf_speed.fit(X_train_speed, y_train_speed)
rf_angle.fit(X_train_angle, y_train_angle)

# Make predictions
predictions_speed = rf_speed.predict(X_test_speed)
predictions_angle = rf_angle.predict(X_test_angle)

# Evaluate the models
mse_speed = mean_squared_error(y_test_speed, predictions_speed)
mae_speed = mean_absolute_error(y_test_speed, predictions_speed)

mse_angle = mean_squared_error(y_test_angle, predictions_angle)
mae_angle = mean_absolute_error(y_test_angle, predictions_angle)

# Print the evaluation metrics
print(f"Speed Mean Squared Error: {mse_speed}")
print(f"Speed Mean Absolute Error: {mae_speed}")
print(f"Angle Mean Squared Error: {mse_angle}")
print(f"Angle Mean Absolute Error: {mae_angle}")
