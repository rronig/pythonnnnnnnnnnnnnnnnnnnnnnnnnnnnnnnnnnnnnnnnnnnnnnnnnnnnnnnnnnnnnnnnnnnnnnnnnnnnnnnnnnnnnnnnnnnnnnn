import datetime
import math
dt = datetime.datetime.now()
print(dt)
print("Year:", dt.year)
print("Month:", dt.month)
print("Day:", dt.day)
print("Hour:", dt.hour)
print("Minute:", dt.minute)
print("Second:", dt.second)
miliseconds = math.floor(dt.microsecond/1000)
print("Millisecond:", miliseconds)
microseconds = dt.microsecond-miliseconds*1000
print("Microsecond:", microseconds)


current_date=dt.date()
print(current_date)
print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)

current_time=dt.time()
print(current_time)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Millisecond:", miliseconds)
print("Microsecond:", microseconds)
specific_date=datetime.date(2024, 2, 29)
specific_time=datetime.time(12, 31)
print(specific_date)
print(specific_time)

duration=datetime.timedelta(days=36, hours=12, minutes=31)
new_date=current_date+duration
print(new_date)
previous_date=current_date-duration
print(previous_date)
utc_time=datetime.datetime.now(datetime.timezone.utc)
print(utc_time)

#custom_offset=datetime.timedelta(hours=5.3)
