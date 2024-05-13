'''
Helper functions file
'''
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Input
import os

def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)


def find_symbol_file_path(data_folder, symbol):
    """
    Find the file path for a stock symbol in the specified data folder.
    The symbol's file is identified uniquely by the symbol in the filename, ignoring dates.

    Args:
    data_folder (str): The directory where CSV files are stored.
    symbol (str): The stock symbol to find. The symbol is expected to be capitalized.

    Returns:
    str: The full path to the symbol's data file if found, otherwise returns None indicating the file is not found.
    """
    try:
        # List all files in the specified directory
        files = os.listdir(data_folder)
        
        # Iterate over files to find the one that matches the symbol
        for file in files:
            # Check if the filename starts with the symbol and ends with '.csv'
            if file.startswith(symbol.upper() + "_") and file.endswith('.csv'):
                return os.path.join(data_folder, file)
                
        # If no file is found for the symbol, return None
        return None
    
    except Exception as e:
        return str(e)


def data_prep(data_folder_path = "data/processed/split_adjusted", symbol = 'NVDA',target_feature = 'Split_Adjusted_Close', split_ratio = 0.7, look_back=1):
    filepath = find_symbol_file_path(data_folder_path, symbol)
    data = pd.read_csv(filepath)
    # Ensure that the data is in chronological order
    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)
    # Selecting the closing prices as the feature to predict
    closing_prices = data[target_feature].values

    scaler = MinMaxScaler(feature_range=(0, 1))
    closing_prices = scaler.fit_transform(closing_prices.reshape(-1, 1))

    split = int(split_ratio * len(closing_prices))
    train_data = closing_prices[:split]
    test_data = closing_prices[split:]

    # look_back = 1  # Number of previous time steps to consider for predicting the next step
    trainX, trainY = create_dataset(train_data, look_back)
    testX, testY = create_dataset(test_data, look_back)

    trainX = np.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))  # Reshape for LSTM [samples, time steps, features]
    testX = np.reshape(testX, (testX.shape[0], testX.shape[1], 1))

    return trainX, testX, trainY, testY, closing_prices, scaler

def inverse(train_predict,test_predict,closing_prices, scaler):

    # Invert predictions
    train_predict = scaler.inverse_transform(train_predict)
    test_predict = scaler.inverse_transform(test_predict)
    inverse_closing_prices = scaler.inverse_transform(closing_prices)
    return train_predict, test_predict, inverse_closing_prices
    
# trainY = scaler.inverse_transform([trainY])
# testY = scaler.inverse_transform([testY])

def plot_train_and_test_predict(train_predict,test_predict,  closing_prices,inverse_closing_prices, look_back):
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
    plt.plot(inverse_closing_prices, label='Actual Price', color='blue')
    plt.plot(trainPredictPlot, label='Train Predicted Price', color='orange')
    plt.plot(testPredictPlot, label='Test Predicted Price', color='green')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time in Days')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

# Example usage commented out
data_folder_path = "data/processed/split_adjusted"
stock_symbol = "AAPL"
print(find_symbol_file_path(data_folder_path, stock_symbol))
