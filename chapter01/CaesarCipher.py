# =========== PROBLEM:CAESAR`S CIPHER =======
# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again

def encr_orig(*args):
    # Prepare your secret message

    secret_message = ''

    # get message value
    message = args[0]

    # get key value
    key = int(args[1])

    # get original message
    if len(args) == 3:
        if args[2] == 1:

            key = -key


    # Cycle through each character in the message
    for char in message:

        # if it is a letter

        if char.isalpha():

            # Get unicode and add the shift amount

            char_code = ord(char) + key

            # if uppercase

            if char.isupper():

                # if greater than 'Z'

                if char_code > ord('Z'):
                    char_code -= 26

                # if less than 'A'

                if char_code < ord('A'):
                    char_code += 26

            # if lowercase

            if char.islower():

                # if greater than 'z'

                if char_code > ord('z'):
                    char_code -= 26

                # if less than 'a'

                if char_code < ord('a'):
                    char_code += 26

            # Convert from code to letter and add to message

            secret_message += chr(char_code)

        # if not a letter leave the character as is

        else:
            secret_message += char

    # print the encrypted message

    return secret_message

    # print("Encrypted message: ", secret_message)

if __name__ == '__main__':
    # Receive the message to encrypt and the number of characters to shift
    message = input("Enter your message:")
    key = input("How many characters should we shift(-26~26):")
    encr_mess = encr_orig(message,key)
    print("Encrypted message:", encr_mess)
    print("original message:", encr_orig(encr_mess, key, 1))
