numberItems = int(input("Number of items: "))
itemList = dict()

for n in range(numberItems):
    readInput = input("Input item and price: ")
    holder = readInput.split(' ')
    itemList[holder[0]] = int(holder[1])
    sortedList = sorted(itemList.items(), key = lambda x:x[1], reverse = False)

for n in sortedList:
    print(n[0], n[1])