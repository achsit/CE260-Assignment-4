import pandas as pd

# Load the filtered CSV file
df = pd.read_csv('filtered_jfk_arrivals_20190820.csv')

# Keep only columns 20 and 66 (indexing starts from 0, so column 20 is index 19 and column 66 is index 65)
columns_to_keep = [19, 65]
df_filtered = df.iloc[:, columns_to_keep]

# Save the result to a new CSV file
df_filtered.to_csv('filtered_jfk_arrivals_20190820_Sequence_PlaneType_Time.csv', index=False)

# Display the first few rows of the filtered data
print(df_filtered.head())