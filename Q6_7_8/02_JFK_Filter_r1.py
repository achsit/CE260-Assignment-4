import pandas as pd

# Define the number of rows to read
nrows = 20000

# Define the column names based on the provided header
column_names = [
    "DEP_YYYYMM", "DEP_DAY", "DEP_HOUR", "DEP_QTR", "ARR_YYYYMM", "ARR_DAY", "ARR_HOUR", "ARR_QTR", "OFF_YYYYMM", "OFF_DAY", "OFF_HOUR", "OFF_QTR",
    "ON_YYYYMM", "ON_DAY", "ON_HOUR", "ON_QTR", "FAACARRIER", "FLTNO", "TAILNO", "ETMS_EQPT", "DEP_LOCID", "ARR_LOCID", "OOOI", "ETMS", "OAG",
    "FLT_TYPE", "OAG_ACID", "USER_CLASS", "OAG_S_DEP", "T_OAG_S_DE", "FILED_PTIM", "T_FIL_PTIM", "OOOI_DEP", "T_OOOI_DEP", "NOM_TO", "TAXI_OUT",
    "OAG_OFF", "T_OAG_OFF", "PTIM_OFF", "T_PTIM_OFF", "PLAN_OFF", "T_PLAN_OFF", "EDCT_OFF", "T_EDCT_OFF", "WHEELS_OFF", "T_WHLS_OFF", "ACT_DZ",
    "T_ACT_DZ", "GAP_DZ", "O_GATE_DEL", "GATE_DELAY", "EDCT_HOLD", "DELAY_TO", "OAG_ARPT_DEP", "PTM_ARPT_DEP", "FILED_ETE", "AIRBORNE", "ACT_DZ2AZ",
    "DELAY_AIR", "ACT_AZ", "T_ACT_AZ", "GAP_AZ", "EDCT_ON", "T_EDCT_ON", "WHEELS_ON", "T_WHLS_ON", "EDCT_ARR", "NOM_TI", "TAXI_IN", "OAG_S_G2G",
    "OOOI_G2G", "OAG_S_ARR", "T_OAG_S_AR", "ADJ_OAG_ARR", "T_ADJ_OAG_ARR", "OOOI_ARR", "T_OOOI_ARR", "DELAY_TI", "DIF_G2G", "O_ARR_DEL", "DELAY_ARR"
]

# Read the first 20,000 rows of the CSV file
df = pd.read_csv(r'C:\Users\Anson\OneDrive\002_UCB\05_CIVENG260\Assignment 4\2019_ASPM_FLIGHT_LEVEL.CSV', names=column_names, header=0, nrows=nrows)

# Print the first few rows of the DataFrame to inspect the data
print(df.head())

# Check if the required columns are present
if 'DEP_LOCID' in df.columns and 'ARR_LOCID' in df.columns:
    # Strip leading and trailing spaces from DEP_LOCID and ARR_LOCID columns
    df['DEP_LOCID'] = df['DEP_LOCID'].str.strip()
    df['ARR_LOCID'] = df['ARR_LOCID'].str.strip()
    
    # Print unique values in DEP_LOCID and ARR_LOCID columns after stripping spaces
    print("Unique DEP_LOCID values after stripping spaces:", df['DEP_LOCID'].unique())
    print("Unique ARR_LOCID values after stripping spaces:", df['ARR_LOCID'].unique())
    
    # Filter rows where either DEP_LOCID or ARR_LOCID is 'JFK'
    filtered_df = df[(df['DEP_LOCID'] == 'JFK') | (df['ARR_LOCID'] == 'JFK')]
    
    # Print the rows where 'JFK' is present
    print("Rows with JFK in DEP_LOCID or ARR_LOCID:")
    print(filtered_df)
    
    # Save the filtered data to a new CSV file
    filtered_df.to_csv('filtered_jfk_flights_sample.csv', index=False)
    
    # Display the first few rows of the filtered data
    print("Filtered data saved to 'filtered_jfk_flights_sample.csv'")
    print(filtered_df.head())
else:
    print("Required columns not found in the DataFrame")