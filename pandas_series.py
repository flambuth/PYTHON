#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Use pandas to create a Series from the following data:
import pandas as pd


# In[3]:


# Name the variable that holds the series fruits.

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
)


# In[5]:


# Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()


# In[6]:


# Run the code necessary to produce only the unique fruit names.

fruits.unique()


# In[7]:


# Determine how many times each value occurs in the series.
fruits.value_counts()


# In[9]:


# Determine the most frequently occurring fruit name from the series.
fruits.value_counts().head(1)


# In[10]:


# Determine the least frequently occurring fruit name from the series.
fruits.value_counts().tail(1)


# In[52]:


# Write the code to get the longest string from the fruits series.
fruits.apply(len).sort_values().tail(1)
#which is the last on the series. has the index of 5
fruits[5]


# In[137]:


spot = fruits.apply(len).idxmax()
fruits[spot]


# In[41]:


# Capitalize all the fruit strings in the series.
fruits.str.capitalize()


# In[53]:


# Count the letter "a" in all the fruits (use string vectorization)
fruits.str.count('a')


# In[54]:


# Output the number of vowels in each and every fruit.
def count_vowels(word): 
    x = len([i for i in word if i in 'aeiou']) 
    return x
fruits.apply(count_vowels)


# In[55]:


# Output the number of vowels in each and every fruit.
#Gonna try a lambda
fruits.apply(lambda x: len([i for i in x if i in 'aeiou']))
#it worked!


# In[4]:


# Use the .apply method and a lambda function to find the fruit(s) containing two 
# or more "o" letters in the name.
#this applies the function. Lambda function is a list comprehension of 'o's in a series element
#if they're >1, then it'll return true


# the lambda makes a list comp that loops through each letter in X. X should be a string
# len of the list comp is greater than 1 will be True
fruits.apply(lambda x: len([i for i in x if i=='o'] ) >1)

#applied the boolean mask made by the 
fruits[fruits.apply(lambda x: len([i for i in x if i=='o'] ) >1)]


# In[59]:


# Write the code to get only the fruits containing "berry" in the name
fruits[fruits.str.contains('berry')]


# In[60]:


# Write the code to get only the fruits containing "apple" in the name
fruits[fruits.str.contains('apple')]


# In[5]:


# Which fruit has the highest amount of vowels?
fruits.apply(lambda x: len([i for i in x if i in 'aeiou'])).sort_values().tail(1)
# This return the index 5, so you can pass that to fruits[5]


# In[65]:


# 2
# Use pandas to create a Series from the following data:
blob = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# In[66]:


# What is the data type of the series?
blob.dtype
#outputs a 'O', which i guess means 'object', the match for string types.


# In[113]:


# Use series operations to convert the series to a numeric data type.
def remove_commas_and_dollarsign(string_num): 
    """
    Cleans off a starting $ and commas where-ever they are. Takes a string, returns a string
    """
    
    x = string_num.replace(',','') 
    x = x.strip("$") 
    return x 


# In[116]:


spam = blob.apply(remove_commas_and_dollarsign).astype('float')
print(spam)


# In[118]:


# What is the maximum value? The minimum?
spam.max()


# In[119]:


#The minimum?
spam.min()


# In[129]:


# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
temp = pd.cut(spam, 4, labels=["bad", "medium", "good", 'excellent'])


# In[130]:


temp.value_counts()


# In[179]:


# Plot a histogram of the data. Be sure to include a title and axis labels.
spam.plot(kind='hist', title='Dollar Amounts', )


# In[7]:


# 3
# Use pandas to create a Series from the following exam scores:
c = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])


# In[141]:


# What is the minimum exam score? The max, mean, median?
#Describe method ought to provide all those answers. Except median.
#Wait, the 50% marker is the median
c.describe()


# In[142]:


c.median()


# In[164]:


# Plot a histogram of the scores.
c.plot(kind = 'hist')


# In[9]:


# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' 
# and 95 should be an 'A'.
bins = [0, 60, 70, 80, 90, 100]
pd.cut(c,bins,labels=["F", "D", "C", "B", "A"])


# In[12]:


# Joins together the number grade from the series and the letter grade made from the pandas
# cut, along the bins set by the bin variable
letter_grades = pd.cut(c,bins,labels=["F", "D", "C", "B", "A"])
list(zip(c,letter_grades))


# In[176]:


# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be 
# converted to a 100, and that many points should be given to every other score as well.
curve = 100 - c[c.idxmax()]
c + curve


# In[ ]:


# 4
# Use pandas to create a Series from the following string:


# In[14]:


d = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))


# In[17]:


#putting this to double check my method of finding min and max frequency of letters
d.value_counts()


# In[15]:


# What is the most frequently occuring letter? 
d.value_counts().idxmax()
#Least frequently occuring?
# d.value_counts().idxmin()


# In[16]:


#Least frequently occuring?
d.value_counts().idxmin()


# In[158]:


# How many vowels are in the list?
vowels = list('aeiou')
len(d[d.isin(vowels)])


# In[161]:


# How many consonants are in the list?
len(d)-len(d[d.isin(vowels)])


# In[162]:


# Create a series that has all of the same letters, but uppercased
d.str.upper()


# In[21]:


# Create a bar plot of the frequencies of the 6 most frequently occuring letters.
d.value_counts().head(6).plot(kind='bar')


# In[19]:


# Create a bar plot of the frequencies of the 6 most frequently occuring letters.
d.value_counts().plot(kind='bar')


# In[ ]:




