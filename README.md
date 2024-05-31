Market Forecaster
==============================

Project to apply Deep Learning Models on Stock Market Data with Python and TensorFlow



Dataset
------------
The dataset for this project encompasses comprehensive daily stock price information for all companies listed in the S&P 500 index. The dataset includes stock prices for each trading day beginning from the year 2006. For companies founded post-2006, the dataset commences from the first available trading day, ensuring a complete historical profile from the point of their introduction to the market.

<a href="https://iexcloud.io">Data provided by IEX Cloud</a>

The data is automatically fetched and updated from the IEX API using a Python script that leverages the API key for authentication. Execute the script run daily after market close ensures that the dataset remains current with the latest trading data. Users can access this script in the [src/data](https://github.com/tranhlok/market-forecaster/tree/main/src/data) directory of the project repository.


Project Organization
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
    ├── docs                                            <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models                                          <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks                                       <- Jupyter notebooks. Naming convention is a number (for ordering), the creator's initials, and a short `-` delimited 
    │   ├── lstm.ipynx                                      description, e.g. `1.0-jqp-initial-data-exploration`.
    │   └──  x                    
    │
    ├── references                                      <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                                         <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures                                     <- Generated graphics and figures to be used in reporting
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
    │   ├── models                                      <- Scripts to train models and then use trained models to make               
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization                               <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini                                         <- tox file with settings for running tox; see tox.readthedocs.io
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
