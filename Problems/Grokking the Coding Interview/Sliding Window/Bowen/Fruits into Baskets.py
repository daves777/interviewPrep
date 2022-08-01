# Problem:
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
# You are given two baskets. Your goal is to pick as many fruits as possible to be placed in the given baskets.
# You are given an array of characters where each character represents a fruit tree. These are the rules:

# 1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# 2. You can start with any tree, but you can’t skip a tree once you have started.
# 3. You will pick exactly one fruit from every tree until you cannot (Stop when you have to pick a third fruit type)

# Write a function to return the maximum number of fruits in both baskets.

def fruits_into_baskets(fruits):
    if(len(fruits)<=2):
        return len(fruits)
    fruit_types = set()
    prevChar = ''
    prevCharChain = 0
    currLength = 0
    maxLength = 0
    for i in range(len(fruits)):
        fruit = fruits[i]
        if(len(fruit_types)==2 and fruit not in fruit_types):
            fruit_types = set()
            fruit_types.add(prevChar)
            fruit_types.add(fruit)
            maxLength = max(maxLength,currLength)
            currLength = prevCharChain+1
        else:
            fruit_types.add(fruit)
            currLength+=1
        if prevChar == fruit:
            prevCharChain+=1
        else:
            prevChar = fruit
            prevCharChain=1
    return max(maxLength,currLength)
            
def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()