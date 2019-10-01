import pandas as pd

#make the alpha_d
letters = list('abcdefghijklmnopqrstuvwxyz')
scores = list(range(1,27))
alpha_df = pd.DataFrame({"letter":letters,"score":scores})

def find_NPR_scores(word): 
first, second, third, fourth, fifth = word[0], word[1], word[2], word[3], 
word[4] 
return first 

def find_NPR_scores(word): 
    first, second, third, fourth, fifth = word[0], word[1], word[2], word[3], word[4]  
    sum_of_rest = alpha_df.loc[second] + alpha_df.loc[third] + alpha_df.loc[fourth] + alpha_df.loc[fifth] 
        
    return alpha_df.loc[first] == sum_of_rest