#ex1
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days = 5)
print("Current Date:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("Date after subtracting five days:", new_date.strftime("%Y-%m-%d %H:%M:%S"))
#ex2
from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d %H:%M:%S"))
print("Today:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d %H:%M:%S"))
#ex3
from datetime import datetime, timedelta
current_date = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Current DateTime with Microseconds:", current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f"))
print("DateTime without Microseconds:", datetime_without_microseconds.strftime("%Y-%m-%d %H:%M:%S"))
#ex4
from datetime import datetime
date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
time_difference = abs((date2 - date1).total_seconds())
print(f"The difference between the two dates is {time_difference} seconds.")
