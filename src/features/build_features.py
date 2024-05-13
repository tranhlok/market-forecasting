import pandas as pd
import os
from tqdm import tqdm


def process_stock_files(input_dir, output_dir, columns=None, new_column_names=None):
    """
    input_dir (str): The directory containing the CSV files to process.
    output_dir (str): The directory where the processed files will be saved.
    columns (list of str): List of column names to select from the CSV files.
    new_column_names (list of str): New column names to apply to the selected columns.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in tqdm(os.listdir(input_dir), desc="Getting The Desired Columns ..."):   
    # for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):  # Check if the file is a CSV
            file_path = os.path.join(input_dir, filename)
            stock_data = pd.read_csv(file_path)
            # Select and rename columns if specified
            if columns and new_column_names:
                stock_data = stock_data[columns]
                stock_data.columns = new_column_names

            # Save to new CSV file
            output_file_path = os.path.join(output_dir, filename)
            stock_data.to_csv(output_file_path, index=False)

    print("Processing complete. Modified files are saved in:", output_dir)

# Usage example:
input_dir = 'data/raw'

split_adjusted_dir = 'data/processed/split_adjusted'
fully_adjusted_dir = 'data/processed/fully_adjusted'
unadjusted_dir = 'data/processed/unadjusted'
all_dir = 'data/processed/all'

split_adjusted_cols = ["date","symbol","open", "high", "low", "close", "volume"]
split_adjusted_names = ["Date","Symbol","Split_Adjusted_Open", "Split_Adjusted_High", "Split_Adjusted_Low", "Split_Adjusted_Close", "Split_Adjusted_Volume"]
process_stock_files(input_dir, split_adjusted_dir, split_adjusted_cols, split_adjusted_names)

fully_adjusted_cols = ["date","symbol","fOpen", "fHigh", "fLow", "fClose", "fVolume"]
fully_adjusted_names = ["Date","Symbol","Fully_Adjusted_Open", "Fully_Adjusted_High", "Fully_Adjusted_Low", "Fully_Adjusted_Close", "Fully_Adjusted_Volume"]
process_stock_files(input_dir, fully_adjusted_dir, fully_adjusted_cols, fully_adjusted_names)

unadjusted_cols = ["date","symbol","uOpen", "uHigh", "uLow", "uClose", "uVolume"]
unadjusted_names = ["Date","Symbol","Unadjusted_Open", "Unadjusted_High", "Unadjusted_Low", "Unadjusted_Close", "Unadjusted_Volume"]
process_stock_files(input_dir, unadjusted_dir, unadjusted_cols, unadjusted_names)       

all_cols = ["date","symbol","open", "high", "low", "close", "volume" ,"fOpen", "fHigh", "fLow", 
            "fClose", "fVolume","uOpen", "uHigh", "uLow", "uClose", "uVolume", "changeOverTime", "marketChangeOverTime", "change", "changePercent"]
all_names = ["Date","Symbol","Split_Adjusted_Open", "Split_Adjusted_High", "Split_Adjusted_Low",  
             "Split_Adjusted_Close", "Split_Adjusted_Volume","Fully_Adjusted_Open", "Fully_Adjusted_High",  
             "Fully_Adjusted_Low", "Fully_Adjusted_Close", "Fully_Adjusted_Volume","Unadjusted_Open", "Unadjusted_High", 
             "Unadjusted_Low", "Unadjusted_Close", "Unadjusted_Volume", "Change_Over_Time", "Market_Change_Over_Time", "Change", "Change_Percent"]
process_stock_files(input_dir, all_dir, all_cols, all_names)
