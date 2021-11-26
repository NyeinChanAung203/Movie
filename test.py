import random

items = ['a','b','c','d','e','f','g','h','i','j','k']
newList = []
for i in range(1,6):
    item = random.choice(items)
    if item in newList:
        print('this item is here',item)
        newList.append(random.choice(items))
        continue
    newList.append(item)
    print(i,item,'done')

print(newList)