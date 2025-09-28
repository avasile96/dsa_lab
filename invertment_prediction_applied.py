import pandas as pd

# Load the bond data
file_path = "data/obligatiuni_titluri_stat.csv"
bonds = pd.read_csv(file_path)

# Parameters
investment_amount = 15000  # EUR
holding_period_years = 1

# Function to calculate 1-year return
def calculate_1_year_return(row):
    ask_price = row['Ask']
    coupon_rate = row['dobanda'] / 100
    ytm_ask = row['YTM Ask']
    
    # Coupon payment for 1 year
    coupon_payment = coupon_rate * 100  # Assuming face value is 100 EUR
    
    # Estimate price change (simplified assumption: no significant price change)
    price_change = 0  # Conservative estimate
    
    # Total return
    total_return = coupon_payment + price_change
    annualized_return = (total_return / ask_price) * 100  # Percentage return
    return annualized_return

# Filter bonds with maturity > 1 year
bonds['Maturitate'] = pd.to_datetime(bonds['Maturitate'])
filtered_bonds = bonds[bonds['Maturitate'] > pd.Timestamp.now() + pd.DateOffset(years=1)]

# Calculate 1-year return for each bond
filtered_bonds['1_Year_Return'] = filtered_bonds.apply(calculate_1_year_return, axis=1)

# Sort bonds by 1-year return
sorted_bonds = filtered_bonds.sort_values(by='1_Year_Return', ascending=False)

# Select the best bond(s)
best_bonds = sorted_bonds.head()

# Display results
print("Top Investment Options:")
print(best_bonds[['simbol', 'NUME', 'Ask', 'dobanda', 'YTM Ask', '1_Year_Return']])

# Save results to a CSV file
output_path = "data/best_bond_investments.csv"
best_bonds.to_csv(output_path, index=False)
print(f"Results saved to {output_path}")