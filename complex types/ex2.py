x = {'city':'Москва', 'temperature':20, 'wind':'восточный'}
print(x, x['city'])
x['temperature']=25
print(x['temperature'])
len = len(x)
print(len)
print(x.get('country', False))
x['date']='27.05.2017'
weather=[]
weather.append(x)
weather.append(x)
weather.append(x)
print(weather)
