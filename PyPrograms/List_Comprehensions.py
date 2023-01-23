from Clear import clear
from time import time

clear()

start = time()
result = [[x, y] for x in range(1, 3) for y in range(1,3)]  #nested list - 2D
print(result)
end = time()
print(end-start)

result = [(x, y) for x in range(1, 3) for y in range(1,3)]  #list of tuples
print(result)


matrix = [[j for j in range(1,3)] for i in range(1, 3)]
print(matrix)

matrix = [[i,j] for i,j in zip(range(1, 3), range(1,3))]
print(matrix)

dct = [{i:j} for i,j in zip(range(1, 3), range(1,3))]  #list of dict
print(dct)

dct = {i:j for i,j in zip(range(1, 3), range(1,3))}  #dict-comprehension
print(dct)


result = []
list1 = [11, 22, [33, 44, [55, 66, 77], 45, 34], 88, 75]

def listProcess(list1=None):
    for val in list1:
        if isinstance(val, list):
            listProcess(val)
        else:
            result.append(val)
    return result


listProcess(list1)
print(result)


def findRepeatedCharacters(chars=""):
    set1 = set()
    i = 0
    for ch in chars:
        if chars.count(ch) > 1:
            set1.add(ch)
            #print(f"{ch} first found at index {i}")
        i = i + 1
    return set1



print(findRepeatedCharacters("abcdaab"))
print(findRepeatedCharacters("Hello"))
print(findRepeatedCharacters("Morning"))


dict1 = {"one":10, "two": {1: 10, 2:20} }
dict2 = {}

def flattenDictionary(dict1):
    for k,v in dict1.items():
        if isinstance(v, dict):
            flattenDictionary(v)
        else:
            dict2[k] = v
    return result


flattenDictionary(dict1)
print(dict2)