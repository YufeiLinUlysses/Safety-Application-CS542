import pandas
import numpy

result = pandas.DataFrame()
crime = pandas.read_csv('crime.csv', encoding='gbk')
crime["OCCURRED_ON_DATE"] = pandas.to_datetime(
        crime["OCCURRED_ON_DATE"], format='%Y-%m-%d %H:%M:%S')
result["CRIME_TIME"] = pandas.to_datetime(crime["OCCURRED_ON_DATE"].dt.date).values.astype(numpy.int64) // 10 ** 9

result["CRIME_TYPE"] = crime["OFFENSE_CODE"]

result["CRIME_NUMBER"] = numpy.arange(1, len(result)+1)


result.to_csv('finalcrime.csv', index=False)
