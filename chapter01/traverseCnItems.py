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
    # tranverse vlaues of all guests
    for v in guests.values():
        # accumulate the item
        numBrought += v.get(item, 0)
    return numBrought

# print number of items (call function)
print("Number of things being brouht: \n")
print("-Apple            {:>4}".format(totalBrought(allGuests, 'apples')))
print("-pretzels         {:>4}".format(totalBrought(allGuests, 'pretzels')))
print("-ham snadwiches   {:>4}".format(totalBrought(allGuests, 'ham snadwiches')))
print("-cups             {:>4}".format(totalBrought(allGuests, 'cups')))
print("-apple pies       {:>4}".format(totalBrought(allGuests, 'apple pies')))