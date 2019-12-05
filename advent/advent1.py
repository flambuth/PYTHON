#Parties like they were then. We need more parties in teh USA.

import pandas as pd
import numpy as np

blob = open("day1data").readlines()

clean_list = [] 
for i in blob:
    clean_list.append(i.rstrip("\n"))

blob2 = pd.Series(clean_list, dtype='int')

blob3 = blob2 / 4

answer = blob3.apply(np.floor) - 2
