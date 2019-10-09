from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    pass


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    pass


for i in data: 
    ...:     automakers.append(i['automaker']) 
    ...:     years.append(i['year']) 
    ...:                      

#Maybe zip them together
years
automakers
x = list(zip(years,automakers))

years = list(set(years))
automakers = list(set(automakers))

temp_list = []
given_year = 2013
#orders them by year
for i in years: 
    for j in x: 
        if i == j[0]: 
            print(i,j[1])
            if j[0] == given_year
                temp_list.append(j[1]) 
#That list holds all the automanufacturers that had a new car in the given year
#Will have to use a counter and pick the top result.

col_count = Counter(temp_list) 
print(col_count)              