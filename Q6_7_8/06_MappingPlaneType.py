import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/Anson/OneDrive/002_UCB/05_CIVENG260/Assignment 4/filtered_jfk_arrivals_20190820_Sequence_PlaneType_Time.csv')

# Define a dictionary to map airplane models to their FAA weight classification
faa_weight_classifications = {
    "CRJ9": "M",
    "B738": "M",
    "B752": "H",
    "E190": "M",
    "A320": "M",
    "A321": "M",
    "B739": "M",
    "B764": "H",
    "A21N": "M",
    "B789": "H",
    "A319": "M",
    "B744": "H",
    "B763": "H",
    "A333": "H",
    "MD11": "H",
    "A306": "H",
    "B77W": "H",
    "B712": "M",
    "A332": "H",
    "E135": "M",
    "E170": "M",
    "E75L": "M",
    "CRJ2": "M",
    "E145": "M",
    "E75S": "M",
    "BCS1": "M",
    "A35K": "H",
    "A343": "H",
    "A388": "S",
    "B748": "H",
    "A359": "H",
    "A346": "H",
    "LJ35": "M",
    'E55P': 'M',
    'B788': 'H', 
    'B772': 'H', 
    'B350': 'H', 
    'B737': 'M', 
    'B753': 'H', 
    'A339': 'H', 
    'B733': 'M', 
    'B787': 'H', 
    'B77L': 'H', 
    'C56X': 'L'
}

# Map the ETMS_EQPT (airplane model) column to FAA weight classifications
df['FAA_Weight_Class'] = df['ETMS_EQPT'].map(faa_weight_classifications)

# For rows where ETMS_EQPT is missing or empty, assume a default weight class of Heavy (H)
df['FAA_Weight_Class'].fillna('H', inplace=True)

# Save the updated DataFrame to a new CSV file (optional)
df.to_csv('updated_with_weight_class.csv', index=False)

# Display the first few rows of the updated DataFrame (optional)
print(df.head())