import pandas as pd 


final = pd.DataFrame()

file = pd.read_csv('raw.csv', encoding = 'utf8')
file['LOCATIONID'].astype('int')
#print(file['LOCATIONID']) 
file['LAT'].astype('float')
file['LON'].astype('float') 
file['POLICE_DISTRICT'].astype('string')
file['DISTRICT'].astype('string')

final['LOCATIONID'] = file['LOCATIONID']
#print(final['LOCATIONID'])
final['LAT'] = file['LAT']
final['LON'] = file['LON']
final['POLICE_DISTRICT'] = file['POLICE_DISTRICT']
final['DISTRICT'] = file['DISTRICT']

final.to_csv('loc.csv', index = False)

