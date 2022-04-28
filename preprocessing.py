import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize(data):
    """
    Normalises the data values using MinMaxScaler from sklearn
    :param data: a DataFrame with columns as  ['index','Open','Close','Volume']
    :return: a DataFrame with normalised value for all the columns except index
    """
    # Initialize a scaler, then apply it to the features
    scaler = MinMaxScaler()
    num_col = list(data.columns)
    data[num_col] = scaler.fit_transform(data[num_col])

    return data

def drop_cols(data):
    #removing unncessary columns
    stocks=data
    stocks.insert(0, 'Item', range(0, 0 + len(stocks)))

    stocks.drop(['High', 'Low', 'Date'], axis = 1)
    return stocks