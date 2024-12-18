import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# Read the CSV file for arrivals data
df = pd.read_csv('updated_with_weight_class.csv')

# Convert T_WHLS_ON to datetime
def convert_time(time_str):
    # Handle potential empty strings
    if pd.isna(time_str) or time_str.strip() == '':
        return None
    
    # Split hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    
    # Create a datetime object (using a base date)
    return datetime(2000, 1, 1, hours, minutes)

# Convert T_WHLS_ON to datetime and sort by arrival time
df['arrival_time'] = df['T_WHLS_ON'].apply(convert_time)
df_sorted = df.sort_values('arrival_time')

# Create cumulative count of arrivals
df_sorted['cumulative_arrivals'] = range(1, len(df_sorted) + 1)

# Define time periods and capacities for runway capacity data
time_periods = [
    {'start': 0, 'end': 6, 'capacity': 32.03},  # 0:00-5:59
    {'start': 6, 'end': 10, 'capacity': 34.97}, # 6:00-9:59
    {'start': 10, 'end': 14, 'capacity': 31.56}, # 10:00-13:59
    {'start': 14, 'end': 18, 'capacity': 31.58}, # 14:00-17:59
    {'start': 18, 'end': 19, 'capacity': 32.15}  # 18:00-23:59
]

# Calculate cumulative capacity for each hour starting at y=0
cumulative_capacity = [{'hour': 0, 'cumulative': 0}]  # Start with y=0 at hour=0
current_cumulative = 0

for period in time_periods:
    for hour in range(period['start'], period['end']):
        current_cumulative += period['capacity']
        cumulative_capacity.append({
            'hour': hour + 1,   # Increment the hour properly for the next entry
            'cumulative': current_cumulative
        })

# Extract hours and cumulative values for plotting runway capacity data
hours = [entry['hour'] for entry in cumulative_capacity]
cumulative_capacity_values = [entry['cumulative'] for entry in cumulative_capacity]

# Convert hours to datetime format (same base date as arrivals)
hours_as_datetime = [datetime(2000, 1, 1) + timedelta(hours=hour) for hour in hours]

# Create the combined plot with smooth lines (no markers)
plt.figure(figsize=(15, 6))

# Plot cumulative aircraft arrivals (from code 1) with a solid line and no markers
plt.plot(df_sorted['arrival_time'], df_sorted['cumulative_arrivals'], linestyle='-', color='red',linewidth=2, label='Cumulative Arrivals')

# Plot cumulative runway capacity (from code 2) with a solid line and no markers
plt.plot(hours_as_datetime, cumulative_capacity_values, linestyle='-', color='blue', linewidth=2, label='Cumulative Runway Capacity')

# Formatting the plot
plt.title('Cumulative Runway Capacity and Aircraft Arrivals under VFC', fontsize=15)
plt.xlabel('Time (HH:MM)', fontsize=12)
plt.ylabel('Cumulative Count', fontsize=12)

# Format x-axis to show HH:MM for both datasets
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gcf().autofmt_xdate()  # Rotate and align the tick labels

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend to distinguish between the two curves
plt.legend()

# Tight layout to prevent cutting off labels
plt.tight_layout()

# Show the combined plot with smooth lines
plt.show()

# Find the hour where cumulative capacity is closest to 630
target_capacity = 630
closest_entry = min(cumulative_capacity, key=lambda x: abs(x['cumulative'] - target_capacity))

# Extract the hour
x_axis_value = closest_entry['hour']
print(x_axis_value)

# Ensure both datasets are aligned in time
arrival_times = df_sorted['arrival_time'].values
arrival_counts = df_sorted['cumulative_arrivals'].values

# Interpolate cumulative runway capacity to match the arrival times
capacity_interpolated = np.interp(
    mdates.date2num(arrival_times), 
    mdates.date2num(hours_as_datetime), 
    cumulative_capacity_values
)

# Calculate the area between the two curves using the trapezoidal rule
area_between_curves = np.trapz(capacity_interpolated - arrival_counts, mdates.date2num(arrival_times))

print("Area between the curves:", area_between_curves)