import csv
import regex as re
from functools import lru_cache

# initialize variables
listA = list()
listB = list()
finalSum = 0 # answer for partA
similarityScore = 0 # answer for partB

@lru_cache(maxsize=256)
def read_data(file):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            data = line[0]
            numbers = re.findall("\d+", data)
            listA.append(int(numbers[0]))
            listB.append(int(numbers[1]))
    return listA,listB

listA,listB = read_data("data.csv")

### Part A


listA.sort()
listB.sort()

for i in range(len(listA)):
    finalSum += abs(listA[i]-listB[i])
    
print(finalSum)

### Part B

def filter_ab(a,b):
    temp_list = [n for n in b if a==n]
    return len(temp_list)

for n in listA:
    similarityScore += n * filter_ab(n,listB)
    
print(similarityScore)
    
