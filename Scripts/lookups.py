from enum import Enum

class DataCategory(Enum):
    HISTORICAL = "historical_gold_prices"
    DAILY = "daily_gold_prices"
    PREDICTIONS = "gold_price_predictions"
    TRENDS = "gold_price_trends"

class DataSource(Enum):
    YAHOO_FINANCE = "yahoo_finance"
    LOCAL_CSV = "local_csv"

class ETLStatus(Enum):
    SUCCESS = "success"
    FAILED = "failed"

class ErrorType(Enum):
    CONNECTION_ERROR = "connection_error"
    DATA_ERROR = "data_error"
