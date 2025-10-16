import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('weather_tokyo_data.csv')
temps = df['temperature'][0].split()  # Split the string into list of strings
temps = [float(t.replace('(', '').replace(')', '')) for t in temps if t.strip()]  # Clean and convert to float
# Remove any unwanted characters and whitespace
df['temperature'] = df['temperature'].astype(str).str.strip()

# Remove parentheses or other possible non-numeric chars
df['temperature'] = df['temperature'].str.replace('[^0-9.\-]', '', regex=True)

# Convert to numeric, coercing errors into NaN
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

avg_tmp = sum(temps) / len(temps)
print(f"Average temperatures are {avg_tmp:.2f}")
df['date_str'] = df['year'].astype(str) + '-' + df['day'].str.replace('/', '-')
df['date'] = pd.to_datetime(df['date_str'], format='%Y-%m-%d')
df['month'] = df['day'].str.split('/').str[0].astype(int)
daily_avg = df.groupby('date')['temperature'].mean().reset_index()
daily_avg['year_month'] = daily_avg['date'].dt.to_period('M')
monthly_avg = daily_avg.groupby('year_month')['temperature'].mean().reset_index()

# Assign seasons based on month
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'

df['season'] = df['month'].apply(get_season)

# Adjust the year so that Winter belongs to the year of December
def adjust_season_year(row):
    if row['month'] == 1 or row['month'] == 2:
        return row['year'] - 1
    else:
        return row['year']

df['season_year'] = df.apply(adjust_season_year, axis=1)

# Group by season only — ignore year
overall_seasonal_avg = df.groupby('season')['temperature'].mean().reset_index()

# Sort by natural season order
season_order = ['Winter', 'Spring', 'Summer', 'Autumn']
overall_seasonal_avg['season'] = pd.Categorical(overall_seasonal_avg['season'], categories=season_order, ordered=True)
overall_seasonal_avg = overall_seasonal_avg.sort_values('season')

print(overall_seasonal_avg)

print(monthly_avg)
hottest_temp_value = df['temperature'].max()
print("Hottest temps are", hottest_temp_value)
coldest_temp_value = df['temperature'].min()
print("Coldest temps are", coldest_temp_value)
plt.figure(figsize=(12,6))
plt.plot(daily_avg['date'], daily_avg['temperature'], marker='o', linestyle='-')
plt.title('Daily Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()