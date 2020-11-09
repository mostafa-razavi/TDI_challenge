import pandas
import numpy
from datetime import datetime
import warnings
from scipy import stats

def get_year(date):
    if pandas.isnull(date):
        warnings.warn("A date value is missing or invalid.")
        return
    try:
        return datetime.strptime(date, '%Y-%m-%d').year 
    except:
        return

def get_month(date):
    if pandas.isnull(date):
        warnings.warn("A date value is missing or invalid.")
        return
    try:
        return datetime.strptime(date, '%Y-%m-%d').month 
    except:
        return

def get_day(date):
    if pandas.isnull(date):
        warnings.warn("A date value is missing or invalid.")
        return
    try:
        return datetime.strptime(date, '%Y-%m-%d').day 
    except:
        return


def append_datraset():
    years_array = numpy.arange(1980, 2021, 1)
    for iyear in range(len(years_array)):
        csv_address = 'C:\myProjects\TDI\Data\CSV\\' + 'daily_42101_' + str(years_array[iyear]) + '.csv'
        

        if iyear == 0:
            all_years_df = pandas.read_csv(csv_address, sep=',')
        else:
            all_years_df = all_years_df.append(pandas.read_csv(csv_address, sep=','))

    print(all_years_df)






all_years_df = pandas.read_csv('C:\myProjects\TDI\Data\\1980-2020_air_quality.csv', sep=',')
#df_test_2019 = pandas.read_csv('C:\myProjects\TDI\Data\\test_2018_2019.csv', sep=',')
df = all_years_df





# Parse dates and add Year, Month, and Day columns
df['Year'] = df.apply(lambda x: get_year(x['Date Local']), axis=1)
df['Month'] = df.apply(lambda x: get_month(x['Date Local']), axis=1)
df['Day'] = df.apply(lambda x: get_day(x['Date Local']), axis=1)

#city = df[df['City Name'] == 'Deer Park']
#city = df[df['City Name'] == 'Salt Lake City']
#city_aqi = city[(city['Method Name'] != ' - ') & (city['Month'] == 8)]

cities_counts = df['City Name'].value_counts()
months_counts = df['Month'].value_counts()
years_counts = df['Year'].value_counts()

months_aqi = df[df['Month'] == 1] ['AQI']
#print(months_aqi)
my_cities = ['Salt Lake City', 'Denver', 'Cleveland', 'Boston', 'San Fransisco', 'Los Angeles', 'Austin', 'Seattle']

month_mean_aqi_array = []
months_array = numpy.arange(1, 13, 1)
#for city, _ in cities_counts.items():
for icity in range(len(my_cities)):
    for month, _ in months_counts.items():
        city_month_aqi = df[     (df['AQI'].notnull() == True)  &  (df['Month'] == month)  &  (df['City Name'] == my_cities[icity])       ]["AQI"].mean()
        #print(city, month)
        month_mean_aqi_array.append([my_cities[icity], month, city_month_aqi]) 
        print(city_month_aqi)

month_mean_aqi_array = numpy.asarray(month_mean_aqi_array)
month_mean_aqi_array = month_mean_aqi_array[month_mean_aqi_array[:,1].argsort()]

print(month_mean_aqi_array)
