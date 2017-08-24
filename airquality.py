import pandas as pd  
#(1.) Download the dataset from https://archive.ics.uci.edu/ml/datasets/Air+quality and save .csv file into /data


#(2.) Load the dataset into pandas data frame
df = pd.read_csv('data/AirQualityUCI.csv',sep=";")

#(3.) Create a timeseries data frame
df['Date'] = pd.to_datetime(df['Date'])
df.index = df['Date']
del df['Date']

#(4.) Remove all the values of NO2(GT) greater than 100 from march 2005 till june 2005
#df = df[(df['Date'] >='2005-03') & (df['Date'] <= '2005-06') & (df['NO2(GT)'] > 100)]
df = df['2005-03':'2005-06']
df = df[(df['NO2(GT)'] > 100)]
print(df)
