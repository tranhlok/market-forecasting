# Market Forecasting

Comprehensive dataset of daily stock price information for all companies listed in the S&P 500 index from 12/29/2006 to 05/10/2024.

Apply Deep Learning models on the newly created dataset with Python and TensorFlow.

## Dataset

### Introduction

The dataset for this project encompasses comprehensive daily stock price information for all companies listed in the S&P 500 index. The dataset includes stock prices for each trading day beginning from the year 2006. For companies founded post-2006, the dataset commences from the first available trading day, ensuring a complete historical profile from the point of their introduction to the market.

<a href="https://iexcloud.io">Data provided by IEX Cloud</a>

### Data Processing
The data is automatically fetched and updated from the IEX API using a Python script that leverages the API key for authentication. Execute the script run daily after market close ensures that the dataset remains current with the latest trading data. Users can access this script in the [src/data](/src/data/) directory of the project repository.

- The list of all SP 500 companies scraped from wikipedia is in  [data/interim](/data/interim/). Source for the scraping can be found in [src/data](/src/data/).
- The processed dataset can be found in [data/processed](/data/processed/), which is divided into 4 smaller datasets for different use cases:
    + `all` consists of all price types.
    + `fully_adjusted` consists of fully adjusted prices.
    + `split_adjusted` consists of split adjusted prices.
    + `unadjusted` consists of unadjusted prices.
- The raw dataset can be found in [data/raw](/data/raw/).

## Forecasting
I used my own stock dash board to catch the patterns of different tickers. The stock dashboard built on streamlit can be found here: https://github.com/tranhlok/stock-dashboard
The initial results with LSTM models on NVDA ticker can be seen in the jupyter notebook [`lstm`](/notebooks/lstm.ipynb).


## Installation

### 1. Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/tranhlok/market-forecaster.git`

`cd market-forecaster`

### 2. Set Up a Virtual Environment (optional but recommended)

Create a new virtual environment by running:

`python -m venv venv`

OR

`python3 -m venv venv`

Activate the virtual environment:
- On Windows:

  `.\venv\Scripts\activate`

- On macOS and Linux:

  `source venv/bin/activate`


### 3. Install Dependencies

Install the required Python packages with pip: 

`pip install -r requirements.txt`

## Configuration

To run the data processing pipeline, you will need to set up your IEX Cloud API credentials. Create a file named `config.json` in your project directory and add your API key as follows:

```json
{
    "api": {
          "iex_key": "your_iex_key",
          "base_url": "https://cloud.iexapis.com/stable/"
    }
}
```


## Project Organization
------------

    ├── LICENSE
    ├── Makefile                                        <- Makefile with commands like `make data` or `make train`
    ├── README.md                                       <- The top-level README for developers using this project.
    ├── data
    │   ├── external                                    <- Data from third party sources.
    │   │   
    │   ├── interim                                     <- Intermediate data that has been transformed.
    │   │   ├── sp500_list.csv                              <- SP 500 companies dataset
    │   │ 
    │   ├── processed                                   <- The final, canonical data sets for modeling. Filetype: .CSV
    │   │   ├── all                                     <- Data will all price types, along with change percentages.
    │   │   ├── fully_adjusted                          <- Data with fully adjusted close price, open price, high price, low price, close price and volume
    │   │   ├── split_adjusted                          <- Data with split adjusted close price, open price, high price, low price, close price and volume
    │   │   └── unadjusted                              <- Data with unadjusted close price, open price, high price, low price, close price and volume
    │   │
    │   ├── raw                                         <- The original, immutable data dump. Filetype: .CSV
    │   │
    │   └── raw_data_variables.txt                      <- The original data variables' descriptions.
    │
    ├── models                                          <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks                                       <- Jupyter notebooks. Naming convention is a number (for ordering), the creator's initials, and a short `-` delimited 
    │   ├── lstm.ipynx                                      description, e.g. `1.0-jqp-initial-data-exploration`.
    │               
    │
    ├── requirements.txt                                <- The requirements file for reproducing the analysis environment, e.g.
    │                                                      generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                                        <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                                             <- Source code for use in this project.
    │   ├── __init__.py                                 <- Makes src a Python module
    │   │
    │   ├── data           
    │   │   ├── make_dataset.py                         <- Scripts to download or generate data
    │   │   └── sp500_list_scraping.py                  <- Scripts to download the list of all SP 500 symbol     
    │   │
    │   ├── features                                    <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   └── models                                      <- Scripts to train models and then use trained models to make               
    │       ├── predict_model.py
    │       └── train_model.py
       

--------



```

 (                                     
 )\ )             *   )                
(()/(           ` )  /((      )        
 /(_)) (    (    ( )(_))(  ( /(  (     
(_))   )\   )\  (_(_()|()\ )(_)) )\ )  
| |   ((_) ((_) |_   _|((_|(_)_ _(_/(  
| |__/ _ \/ _|    | | | '_/ _` | ' \)) 
|____\___/\__|    |_| |_| \__,_|_||_|  
                                       
                                                                                                                                                         
```
