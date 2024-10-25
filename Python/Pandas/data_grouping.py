from datetime import datetime, timedelta
import pandas as pd

# Sample DataFrame
data = {'timestamp': ['12:00', '12:05', '12:10', '12:15', '12:20']}
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Parameters
period = timedelta(minutes=10)
group = 1
threshold = None

def assign_groups(row):
    global group, threshold
    if threshold is None or row['timestamp'] > threshold:
        threshold = row['timestamp'] + period
        group += 1
    return group

df['group'] = df.apply(assign_groups, axis=1)

print(df)