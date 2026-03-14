import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate a sample financial trading dataset

def generate_trading_data(num_records=1000):
    # Generate a date range
    start_date = datetime.now() - timedelta(days=num_records)
    date_range = [start_date + timedelta(days=i) for i in range(num_records)]

    # Generate random trading data
    data = {
        'timestamp': date_range,
        'open_price': np.random.uniform(100, 500, num_records),
        'close_price': np.random.uniform(100, 500, num_records),
        'high_price': np.random.uniform(500, 600, num_records),
        'low_price': np.random.uniform(50, 100, num_records),
        'trading_volume': np.random.randint(1000, 10000, num_records),
        'asset_symbol': np.random.choice(['AAPL', 'GOOGL', 'TSLA', 'AMZN'], num_records),
        'market_sentiment': np.random.choice(['Bullish', 'Bearish'], num_records)
    }

    # Create a DataFrame
    trading_df = pd.DataFrame(data)
    return trading_df

# Generate the dataset and save to CSV
if __name__ == '__main__':
    trading_data = generate_trading_data(1000)
    trading_data.to_csv('sample_trading_data.csv', index=False)
    print('Sample trading data generated and saved to sample_trading_data.csv')
