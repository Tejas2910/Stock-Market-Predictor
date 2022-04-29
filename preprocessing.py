import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize(data):
   
    # Initialize a scaler, then apply it to the features
    scaler = MinMaxScaler()
    num_col = list(data.columns)
    num_col.remove('Item')
    data[num_col] = scaler.fit_transform(data[num_col])

    return data

def drop_cols(data):
    #removing unncessary columns
    stocks=pd.DataFrame()
    stocks=data[['Open','Close','Volume']].copy()

    stocks.insert(0, 'Item', range(0, 0 + len(stocks)))

    return stocks