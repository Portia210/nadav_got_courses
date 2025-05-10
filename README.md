# Trading View Returns Calculator

This script calculates and displays returns for SPY, QQQ, and SPMO over different time periods (1 week, 1 month, 1 year, 3 years, and 5 years).

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python trading_view.py
```

## Output

The script will display a table showing the returns for each ETF over the specified time periods. Returns are displayed as percentages.

## Notes

- The script uses trading days (not calendar days) for calculations
- Returns are calculated using closing prices
- Data is fetched from Yahoo Finance using the yfinance library
- If data is not available for a particular period, it will show as 'N/A' 