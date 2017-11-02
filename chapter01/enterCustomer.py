# =======Problem:create a customer list=======
#   create an array of customer dictionaries
#   Output should look like this

'''

Dear XX XXXXX
     As our distinguished custoomer,you......

Enter Customer (Yes/No) : y
Enter Customer Name: Harry Potter male
Enter Customer (Yes/No) : y
Enter Customer Name: Sherlock Holmes male
Enter Customer (Yes/No) : y
Enter Customer Name: Taylor Swift female
Enter Customer (Yes/No) : n

'''

# initiate the customer
customers = []
# loop
while True:
    # input and cut off the 1st letter to cover user`s input
    createEntry = input("Enter customer(yes/no)?")
    createEntry = createEntry[0].lower()

    # y or n
    if (createEntry == 'n') or (createEntry != 'y'):
        break
    else:
        fName, lName, gender = input("Enter custer`s name&gender: ").split()
        customers.append({'fName':fName, 'lName':lName, 'gender':gender})
    for cust in customers:
        #title
        if cust['gender'] == 'male':
            title = 'Mr ' + cust['lName']
        else:
            title = 'Ms ' + cust['lName']
        # print the maile
        print('''
        Dear {},
    As our distinguished customer,you......
        '''.format(title))