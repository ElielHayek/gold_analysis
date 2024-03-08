import schedule
import time
from data_handler import fetch_gold_prices, transform_data, load_data_to_db

def job():
    print("Starting the ETL process.")
    # Define your date range for fetching gold prices
    start_date = '2000-01-01'
    end_date = '2024-03-04'
    # Fetch gold prices
    gold_prices = fetch_gold_prices(start_date, end_date)
    # Transform data
    transformed_data = transform_data(gold_prices)
    # Load data to database
    load_data_to_db(transformed_data, 'gold_prices.daily_gold_prices') 
    print("ETL process completed.")

# Schedule the job every day at 19:30
schedule.every().day.at("15:05").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
