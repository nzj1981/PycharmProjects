import pprint

# message
message = '''
Books and doors are the same thing.
You open them, and you go through into another world.
'''

# split message to words into a list

words = message.split()

# define dictionary counter

count = {}

# traverse every word and accumulate

for word in words:
    word = word.lower()
    if word[-1].isalpha():
        count.setdefault(word, 0)
        count[word] += 1
    else:
        word = word[:-1]
        count.setdefault(word, 0)
        count[word] += 1
pprint.pprint(count)

