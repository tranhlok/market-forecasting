import argparse
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

from helper import data_prep, inverse, plot_train_and_test_predict
# from visualize import inverse, plot_train_and_test_predict

class LSTMModel:
    def __init__(self, trainX, testX, trainY, look_back, epochs, batch_size):
        self.trainX = trainX
        self.testX = testX
        self.trainY = trainY
        self.look_back = look_back
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential([
            Input((self.look_back, 1)),
            LSTM(50, return_sequences=True),
            LSTM(50, return_sequences=False),
            Dense(1)
        ])
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model
    
    def train(self):
        with tf.device('/CPU:0'):
            history = self.model.fit(self.trainX, self.trainY, epochs=self.epochs, batch_size=self.batch_size, verbose=2, validation_split=0.1)
        return history
    
    def save_weights(self):
        self.model.save_weights('/Users/lok/Developer/market-forecaster/models/nvidia.weights.h5')

    def predict(self):
        train_predict = self.model.predict(self.trainX)
        test_predict = self.model.predict(self.testX)
        return train_predict, test_predict
# Example usage:



def main(symbol):
    data_folder_path = "/Users/lok/Developer/market-forecaster/data/processed/split_adjusted"

    target_feature = 'Split_Adjusted_Close'
    split_ratio = 0.7
    look_back = 1
    trainX, testX, trainY, testY, closing_prices, scaler = data_prep(data_folder_path, symbol,target_feature, split_ratio, look_back)

    epochs = 100
    batch_size = 32
    lstm_model = LSTMModel(trainX,testX, trainY, look_back, epochs, batch_size)
    history = lstm_model.train()

    lstm_model.save_weights()

    train_predict, test_predict = lstm_model.predict()

    train_predict, test_predict, inverse_closing_prices = inverse(train_predict,test_predict,closing_prices, scaler)
    plot_train_and_test_predict(train_predict,test_predict, closing_prices,inverse_closing_prices, look_back)



main('NVDA')
# if __name__ == "__main__":
#     # Create the parser
#     parser = argparse.ArgumentParser(description='Process some integers.')

#     # Add arguments
#     parser.add_argument('batchfile', type=float, help='A floating point number for batchfile')
#     parser.add_argument('size', type=int, help='An integer for size')

#     # Parse arguments
#     args = parser.parse_args()

#     # Call the main function using parsed arguments
#     main(args.batchfile, args.size)




























def main(batchfile, size):
    print(f"Batchfile value: {batchfile}")
    print(f"Size value: {size}")

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Process some integers.')

    # Add arguments
    parser.add_argument('batchfile', type=float, help='A floating point number for batchfile')
    parser.add_argument('size', type=int, help='An integer for size')

    # Parse arguments
    args = parser.parse_args()

    # Call the main function using parsed arguments
    main(args.batchfile, args.size)

