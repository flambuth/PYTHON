

#%%
def simpleArraySum(array):
    """
    Function accepts an array of integers and returns their sum
    """
    sum = 0
    for i in array:
        sum += i
    return sum

#%%
    
def compareTriplets(a,b):
    a_score, b_score = (0,0)
    blob = list(zip(a,b))
    for i in blob:
        if i[0]>i[1]:
            a_score += 1
        elif i[0]<i[1]:
            b_score += 1
    return a_score, b_score

#%%
    
def aVeryBigSum(ar1, ar2):
    number = [1000000000] * ar
    new_list = []
    count = 1
    for i in number:
        i = i + count
        new_list.append(i)
        count += 1
    return sum(ar2)

#%%
def diagonalFirstDifference(twoDarray):
    length = len(twoDarray[0])
    for i in range(length):
        for j in range(length):
            if i == j: 
                print(twoDarray[i][j])

def diagonalOtherDifference(twoDarray):
    length = len(twoDarray[0])
    for i in range(length):
        for j in range(length):
            if (i+j) == (length-1): 
                print(twoDarray[i][j])

def diagonalDifference(arr):
    length = len(arr[0])
    diags1 = []
    diags2 = []
    
    for i in range(length):
        for j in range(length):
            if i == j: 
                diags1.append(arr[i][j])
                
    for i in range(length):
        for j in range(length):
            if (i+j) == (length-1): 
                diags2.append(arr[i][j])
    return abs(sum(diags1) - sum(diags2))