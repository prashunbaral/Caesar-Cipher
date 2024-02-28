#Prashun Baral
#2408881
# Define the alphabet and its length
letters = 'abcdefghijklmnopqrstuvwxyz'  # String containing a-z
num_letters = len(letters)  # Length of letters (26)

def encrypt(plaintext, shift):
    """
    Encrypts the given plaintext using the Caesar Cipher.

    Parameters:
    - plaintext (str): The input text to be encrypted.
    - shift (int): The number of positions to shift each letter.

    Returns:
    str: The encrypted text in uppercase.
    """
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter == ' ':
            ciphertext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + shift
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext.upper()

def decrypt(ciphertext, shift):
    """
    Decrypts the given ciphertext using the Caesar Cipher.

    Parameters:
    - ciphertext (str): The input text to be decrypted.
    - shift (int): The number of positions to shift each letter.

    Returns:
    str: The decrypted text in uppercase.
    """
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter == ' ':
            plaintext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - shift
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
    return plaintext.upper()

def process_file(filename, mode, shift):
    """
    Processes a file, either encrypting or decrypting messages.

    Parameters:
    - filename (str): The name of the file to be processed.
    - mode (str): 'e' for encryption, 'd' for decryption.
    - shift (int): The number of positions to shift each letter.

    Returns:
    list: A list of encrypted or decrypted messages.
    """
    messages = []
    with open(filename, 'r') as file:
        for line in file:
            message = line.strip()

            if mode.lower() == 'e':
                encrypted_message = encrypt(message, shift)
                messages.append(encrypted_message)
            elif mode.lower() == 'd':
                decrypted_message = decrypt(message, shift)
                messages.append(decrypted_message)
            else:
                print('Invalid Mode. Please enter e or d !!!')
                return None
    return messages

def is_file(filename):
    """
    Checks if a file exists.

    Parameters:
    - filename (str): The name of the file to be checked.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    try:
        with open(filename, 'r'):
            return True
    except FileNotFoundError:
        return False

def write_messages(list_of_str):
    """
    Writes a list of strings to a file named 'results.txt'.

    Parameters:
    - list_of_str (list): A list of strings to be written to the file.
    """
    with open('results.txt', 'w') as file:
        file.write(' \n'.join(list_of_str))

def message_or_file():
    """
    Gets user input for mode, input method, filename, and shift.

    Returns:
    tuple: A tuple containing mode, file_or_console, filename, and shift.
    """
    while True:
        mode = input('Would you like to encrypt (e) or decrypt (d): ').lower()
        if mode not in ['e', 'd']:
            print('Invalid Mode')
            continue

        file_or_console = input('Would you like to read from a file (f) or the console (c)? ').lower()
        if file_or_console not in ['c', 'f']:
            print('Invalid Input. Please enter c or f')
            continue

        filename = None
        if file_or_console == 'f':
            while True:
                filename = input('Enter a filename: ')
                if is_file(filename):
                    break
                else:
                    print('Invalid Filename')

        shift = int(input('Enter shift: '))
        return mode, file_or_console, filename, shift

def welcome():
    """Displays a welcome message."""
    print('\n*** WELCOME TO THE CAESAR CYPHER ***\n')

def enter_message():
    """
    Main function to handle user interaction.
    Encrypts or decrypts messages based on user choices.
    """
    while True:
        welcome()

        mode, file_or_console, filename, shift = message_or_file()

        if file_or_console == 'c':
            text = input(f'Enter the text to {mode}: ').upper()
            if mode == 'e':
                result = encrypt(text, shift)
            else:
                result = decrypt(text, shift)
            print(f'{mode.upper()}ODED MESSAGE: {result}')
            write_messages([result])

        elif file_or_console == 'f':
            if mode == 'e':
                print(' ** ENCRYPTION MODE ACTIVATED **')
            elif mode == 'd':
                print(' ** DECRYPTION MODE ACTIVATED **')

            result = process_file(filename, mode, shift)
            if result:
                print(result)
                write_messages(result)

        continue_input = input('Would you like to encrypt or decrypt another message? (y/n): ').lower()

        if continue_input == 'n':
            print('THANK YOU !!!')
            break
        elif continue_input != 'y':
            print('Invalid Input. Please enter y/n')

# Call the main function
enter_message()
