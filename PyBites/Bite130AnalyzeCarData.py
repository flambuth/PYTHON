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
# This list comprehension will make a repeating list of automakers that have have they year key be the one 
# given by the function paratmer.
    x = [i['automaker'] for i in data if i['year']==year]
    x_count = Counter(x)
    return x_count.most_common()[0][0]

def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    pass


x = [i['automaker'] for i in data if i['year']==2006] 
#Will have to use a counter and pick the top result.

x_count = Counter(temp_list) 
print(x_count)              

#This method returns a list of tuples. First 0 is the top tuple's first position, which is the automaker
#with the highest
x_count.most_common()[0][0]                                            
