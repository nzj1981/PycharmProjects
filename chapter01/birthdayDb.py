# Complete birthday database

# current database
birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Tom':'Jun 3'}
print(birthdays)

# loop to perfect birthday database

while True:
    # input name which decides next step
    name = input("Enter a name(blank to quit):")

    # exit, exist already, no record
    if (name == '') or (name == 'quit'):
        break
    elif name in birthdays:
        print('{} is the birthday of {}'.format(name, birthdays[name]))
    else:
        print('I do not have birthday information:',name)
        bday = input('What is the birthday?')
        birthdays[name] = bday
        print('Birthday database update!')
print(birthdays)

