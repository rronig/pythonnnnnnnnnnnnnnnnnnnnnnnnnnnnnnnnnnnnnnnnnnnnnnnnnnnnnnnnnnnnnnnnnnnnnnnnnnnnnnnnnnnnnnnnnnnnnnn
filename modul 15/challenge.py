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