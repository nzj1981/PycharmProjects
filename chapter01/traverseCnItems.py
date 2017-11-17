# Guest & items
'''
pretzels : 椒盐脆饼
'''
allGuests = {'Alice': {'apples': 3, 'pretzels': 4}, 'Bob': {'ham snadwiches': 3, 'apples': 2}, \
             'carol': {'cups': 3, 'apple pies': 1}}


# print(allGuests)

# function: get amount of a item(allGuests, item)
def totalBrought(guests, item):
    # initiate a counter
    numBrought = 0
    # traverse vlaues of all guests
    for v in guests.values():
        # accumulate the item
        numBrought += v.get(item, 0)
    return numBrought


# Initialize the collection
fruits = set()
# Get a collection of fruits
for v in allGuests.values():
    fruits |= set(v)
# print(fruits)
# print number of items (call function)
print("Number of things being brouht: \n")
for i in fruits:
    print("---{:<20}{:<4}".format(i, totalBrought(allGuests, i)))
