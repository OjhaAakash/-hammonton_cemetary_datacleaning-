import pandas as pd
import numpy as np

# I imported panda and numpy, since I used all of them for specific purpose.

# Read in the csv file into the df using the concat function of pandas.
df = pd.concat(map(pd.read_csv, ["file/aakash11.csv","file/halloween2019b.csv","file/halloween2019c.csv"]))

print(df)

# I used this function to find all the column names, since some had a space before the column name.
df.columns

# Since some of the names were not spelled with the capital, I used the str function to make each word start with capital letter.
df["FirstName"] = df["FirstName"].str.capitalize()
df[" LastName"] = df[" LastName"].str.capitalize()
df[" Sex"] = df[" Sex"].str.capitalize()

# Since a lot of dates format was different, so ended up creating new column for years only, so that all the other function can run easily.
# I also had to convert them to integers, since some of them converted into strings.
df['Death Year'] = pd.to_datetime(df[' DOD']).dt.strftime('%Y')
df['Death Year'] = df['Death Year'].fillna(0)
df['Death Year'] = df['Death Year'].astype(int)

df['Birth Year'] = pd.to_datetime(df[' DOB'], errors='coerce').dt.strftime('%Y')
df['Birth Year'] = df['Birth Year'].fillna(0)
df['Birth Year'] =df['Birth Year'].astype(int)
print(df['Birth Year'])
# Computing the Life span for each person in data base.
df['Life Span'] = df['Death Year'] - df['Birth Year']
df1 = df[df['Life Span'] > 0]

df.columns
df[['FirstName', ' LastName', "Birth Year","Death Year","Life Span"]]
#calculate interquartile range 
q3, q1 = np.percentile(df1['Life Span'], [75 ,25])
iqr = q3 - q1

#display interquartile range 
iqr
#iqr for this database is 35.5, and I have decided to keep the data as it is.

#Computing the pivot table
pd.pivot_table(df1, index=['Birth Year'], columns=[' Sex'])
 








