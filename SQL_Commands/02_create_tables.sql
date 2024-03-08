-- Create a table for daily gold prices
CREATE TABLE IF NOT EXISTS gold_prices.daily_gold_prices (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    open_price NUMERIC,
    high_price NUMERIC,
    low_price NUMERIC,
    close_price NUMERIC,
    volume INT
);

-- Create a table for historical gold prices
CREATE TABLE IF NOT EXISTS gold_prices.historical_gold_prices (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    price NUMERIC
);