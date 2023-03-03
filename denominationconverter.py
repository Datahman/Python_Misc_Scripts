""" 
Given an input- some integer value get back result in currency denomination  
e.g. Denominations 1p, 2p, 5p, 10p, 20p, 50p, £1, £2
|253  | 1 £2, 1 50p, 1 2p, 1 1p|

"""



def output(inputValue):
    global result 
    result=''
    if inputValue <=0:
        return result
    else:
            denomination=findLeastDistanceDenomination(inputValue)

            remainderValue=inputValue%denomination
            multiple = inputValue / denomination
            result+= f"count:{math.floor(multiple)} of {denomination}"
            print(result)
            output(remainderValue)
    return result

def findLeastDistanceDenomination(inputValue):
    denominations = [200,100,50,20,10,5,2,1]
    differences = list(map(lambda x: abs(inputValue-x), denominations))
    
    leastDifferenceIndex= min(range(len(differences)), key=differences.__getitem__)
    return denominations[leastDifferenceIndex]
    
print(output(253))

