import pandas as pd
from yahoo_fin import stock_info as si
import datetime
import psycopg2
from file_handler import read_config
import os
from database_handler import create_connection

def fetch_gold_prices(start_date, end_date):
    """Fetch historical gold prices from Yahoo Finance."""
    gold_prices = si.get_data('GC=F', start_date=start_date, end_date=end_date)
    return gold_prices

def transform_data(df):
    """Transform data to fit the gold_prices schema."""
    connection = None

    df.reset_index(inplace=True)
    df.rename(columns={
        'index': 'date', 
        'open': 'open_price', 
        'high': 'high_price', 
        'low': 'low_price', 
        'close': 'close_price', 
        'volume': 'volume'
    }, inplace=True)
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df[['date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']]

def load_data_to_db(df, table_name):
    connection = None
    try:
        connection = create_connection('../config.json')
        cursor = connection.cursor()
        
        for index, row in df.iterrows():
            # Check if row contains NaN values
            if row.isnull().any():
                print(f"Skipping row with NaN values: {row}")
                continue  # Skip this row
            
            # Proceed with insertion
            cursor.execute(
                f"INSERT INTO {table_name} (date, open_price, high_price, low_price, close_price, volume) VALUES (%s, %s, %s, %s, %s, %s)",
                (row['date'], row['open_price'], row['high_price'], row['low_price'], row['close_price'], row['volume'])
            )
        
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection is not None:
            cursor.close()
            connection.close()