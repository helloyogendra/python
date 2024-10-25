# Timedelta function demonstration 

from datetime import datetime, timedelta, time
import os
import time as t

os.system('cls')

def parse_custom_datetime(date_str):
    # Replacing 'D' with 'T' to adhere to the ISO format
    standard_format_str = date_str.replace('D', ' ')

    # Parsing the string into a datetime object
    return datetime.fromisoformat(standard_format_str)

def convert_to_minutes(time_str):
    # Splitting the string into components
    parts = time_str.split(':')
    days_hours = parts[0].split('D')

    # Extracting days and hours
    days = int(days_hours[0])
    hours = int(days_hours[1])

    # Extracting minutes
    minutes = int(parts[1])

    # Calculating total minutes
    total_minutes = days * 24 * 60 + hours * 60 + minutes
    return total_minutes

# Test the function
time1 = "0D00:30:00.000000000"
time2 = "0D01:30:00.000000000"

aa1 = convert_to_minutes(time1)
aa2 = convert_to_minutes(time2)

print(aa1)  # Output: 30
print(aa2)  # Output: 90

date_str1 = "2023-10-27D15:17:24.220"
parsed_datetime1 = parse_custom_datetime(date_str1)
print("parsed_datetime = ", parsed_datetime1)

date_str2 = "2023-10-27D23:45:24.927"
parsed_datetime2 = parse_custom_datetime(date_str2)
print("parsed_datetime = ", parsed_datetime2)

window1 = parsed_datetime1 + timedelta(minutes = aa1)
window2 = parsed_datetime2 + timedelta(minutes = aa2)

print("window1 = ", window1, "type = ", type(window1))
print("window2 = ", window2, "type = ", type(window2))


batch = "23:59:59.999"
current_date = datetime.now().date()
parsed_time = datetime.strptime(batch, "%H:%M:%S.%f").time()
print("parsed_time=", parsed_time)
# Combine date and time to get a datetime object
result_datetime = datetime.combine(current_date, parsed_time)

print("result_datetime = ", result_datetime)

if window1 > result_datetime:
    print(result_datetime)
else:
    print(window1)

if window2 > result_datetime:
    print(result_datetime)
else:
    print(window2)

# Convert To Unix_Time() - approach-1
print("Window-1 : UnixTime : ", t.mktime(window1.timetuple()))
print("Window-1 : UnixTime : ", window1.timestamp())
print("Window-2 : UnixTime : ", t.mktime(window2.timetuple()))

#print("result_datetime : UnixTime : ", t.mktime(result_datetime.timetuple()))

unix_time = result_datetime.timestamp()
print("result_datetime : UnixTime : ",unix_time)

date_time = datetime.fromtimestamp(unix_time)
print("date_time : standard : ",date_time)





def parse_custom_datetime2(date_str):
    standard_format_str = date_str.replace('D', ' ')
    dt = datetime.strptime(standard_format_str, '%Y-%m-%d %H:%M:%S.%f')
    return dt.strftime('%Y-%m-%d %H:%M:%S.%f')


a1 = parse_custom_datetime2("2023-10-27D15:17:24.220")
print(type(a1))
print(a1)

# window3 = a1 + timedelta(minutes = aa1)
# print("window3 = ", window3)
# print("window3 = ", window3.timestamp())
# print("window3 = ", type(window3))

# Custom function
def convert_to_unix_time(date_str="2023-08-17D00:35:24.000"):
    standard_date_str = date_str.replace('D', ' ')
    dt = datetime.strptime(standard_date_str, '%Y-%m-%d %H:%M:%S.%f')
    unix_timestamp = dt.timestamp()
    return unix_timestamp



z1 = convert_to_unix_time("2023-10-27D23:45:24.927")
print(z1)

x1 = str(datetime.now().date())
x2 = "00:00:00.000"


x3 = x1 + ' ' + x2
print(x3)

x4 = parse_custom_datetime2(x3)
print(x4)

x5 = convert_to_unix_time(x4)
print(x5)

x6 = convert_to_unix_time(x3)
print(x6)

mins1 = 600 # 10 mins
mins2 = 900 # 15 mins
mins3 = 1200 # 20 mins

print(datetime.now())
print(datetime.now().timestamp())

time1 = datetime.now().timestamp() + mins1
print("time1 = ", time1)
print("time1 = ", time1 + mins2)
print("time1 = ", time1 + mins3)

time2 = datetime.fromtimestamp(time1)
print(time2)

data = [1698482417.99032, 1698483017.99032, 1698483917.99032, 1698484217.99032, 1698484817.99032, 1698485517.99032]
print("------------------")
for val in data:
    print(datetime.fromtimestamp(val))


from datetime import datetime

def custom_function4(value):
    
    dt = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f') if isinstance(value, str) else value

    # Format the datetime object as a string
    return dt.strftime('%Y-%m-%d %H:%M:%S.%f')
