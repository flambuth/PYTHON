#ptting some shit down

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.datacamp.com/community/tutorials'
response = urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
pages = [i.text for i in soup.find_all('a') if 'community/tutorials?page=' in str(i)]

description=[]
upvote=[]
author=[]
publishdate=[]
title=[]