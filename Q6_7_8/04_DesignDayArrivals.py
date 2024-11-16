import pandas as pd

# Load the original CSV file
df = pd.read_csv(r'C:\Users\Anson\OneDrive\002_UCB\05_CIVENG260\Assignment 4\filtered_jfk_flights.csv')

# Strip leading and trailing spaces from ARR_LOCID column
df['ARR_LOCID'] = df['ARR_LOCID'].str.strip()

# Filter rows based on the conditions
filtered_df = df[(df['ARR_YYYYMM'] == 201908) & (df['ARR_DAY'] == 20) & (df['ARR_LOCID'] == 'JFK')]

# Export the result to a new CSV file
filtered_df.to_csv('filtered_jfk_arrivals_20190820.csv', index=False)

# Display the first few rows of the filtered data
print(filtered_df.head())