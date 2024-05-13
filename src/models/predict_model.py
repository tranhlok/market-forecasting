import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load the scaler and model setup
scaler = MinMaxScaler(feature_range=(0, 1))
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(1, 1)),
    LSTM(50, return_sequences=False),
    Dense(1)
])
model.load_weights('nvidia.h5')

# Function to preprocess and predict
def predict(prices, model, scaler):
    prices = scaler.transform(prices.reshape(-1, 1))
    prices = np.reshape(prices, (prices.shape[0], 1, 1))
    predicted_prices = model.predict(prices)
    predicted_prices = scaler.inverse_transform(predicted_prices)
    return predicted_prices

# Example usage
data = pd.read_csv('data/processed/split_adjusted/NVDA_2006_12_29_to_2024_05_10.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
closing_prices = data['Split_Adjusted_Close'].values

predicted_prices = predict(closing_prices, model, scaler)
print(predicted_prices)




import matplotlib.pyplot as plt

# Actual vs. Predicted on the training data
trainPredictPlot = np.empty_like(closing_prices)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict) + look_back, :] = train_predict

# Actual vs. Predicted on the testing data
testPredictPlot = np.empty_like(closing_prices)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(train_predict) + (look_back * 2):len(closing_prices), :] = test_predict

# Plotting
plt.figure(figsize=(15, 6))
plt.plot(scaler.inverse_transform(closing_prices), label='Actual Price', color='blue')
plt.plot(trainPredictPlot, label='Train Predicted Price', color='orange')
plt.plot(testPredictPlot, label='Test Predicted Price', color='green')
plt.title('Stock Price Prediction')
plt.xlabel('Time in Days')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
