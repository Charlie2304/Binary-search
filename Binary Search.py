# [Binary Search (list already sorted)]
# [Charlie Smith]
# [05/11/2025]
# AS Computer Science

#Global Variables

sortedList = [2, 4, 5, 7, 9, 13, 17, 22, 25, 27, 28, 33]
looking_for = int(input("Type the item (integers only) that you are looking for:  "))
found = False

#Pointers

first = 0
last = len(sortedList) - 1

while found == False and last >= first:

    mid = (first+last) // 2

    if (looking_for == sortedList[mid]):
        found = True
        break

    else:

        if (looking_for > sortedList[mid]):
            first = mid + 1

        elif (looking_for < sortedList[mid]):
            last = mid - 1
            
if found == True:
    print("Item found in data")

else:
    print("Item couldn't be found")
