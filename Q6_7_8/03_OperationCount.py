import pandas as pd

# Load the filtered CSV file
filtered_df = pd.read_csv('filtered_jfk_flights.csv')

# Initialize a dictionary to hold the counts
operation_counts = {}

# Iterate over the rows of the DataFrame
for index, row in filtered_df.iterrows():
    if row['DEP_LOCID'] == 'JFK':
        date_key = (row['DEP_YYYYMM'], row['DEP_DAY'])
    elif row['ARR_LOCID'] == 'JFK':
        date_key = (row['ARR_YYYYMM'], row['ARR_DAY'])
    else:
        continue
    
    if date_key in operation_counts:
        operation_counts[date_key] += 1
    else:
        operation_counts[date_key] = 1

# Convert the dictionary to a DataFrame
operation_counts_df = pd.DataFrame(list(operation_counts.items()), columns=['Date', 'Count'])

# Split the 'Date' column into 'YYYYMM' and 'DAY'
operation_counts_df[['YYYYMM', 'DAY']] = pd.DataFrame(operation_counts_df['Date'].tolist(), index=operation_counts_df.index)
operation_counts_df.drop(columns=['Date'], inplace=True)

# Save the results to a new CSV file
operation_counts_df.to_csv('jfk_operations_count.csv', index=False)

# Display the first few rows of the result
print(operation_counts_df.head())