# Developed by S4int. Inspired by blindma1den.

# Note: Ciphertext will always be UPPERCASE and Plaintext will always be lowercase

# Define the alphabet (excluding "j")
alphabet = "abcdefghiklmnopqrstuvwxyz"

def create_keysquare(keyword):
    """
    Creates the 5x5 keysquare used for Playfair Cipher encryption/decryption.

    Args:
        keyword: The keyword to base the keysquare on.

    Returns:
        The 5x5 keysquare as a 2D list.
    """

    keysquare = []  # Initialise an empty list to hold rows

    # Add keyword letters to keysquare, removing duplicates and preserving order
    keyword = keyword.replace("j", "i")  # Handle "j"
    for letter in keyword:
        if letter not in keysquare:
            keysquare.append(letter)

    # Add remaining letters of the alphabet to keysquare
    for letter in alphabet:
        if letter not in keysquare:
            keysquare.append(letter)

    # Create the 5x5 grid directly
    keysquare = [keysquare[i:i + 5] for i in range(0, len(keysquare), 5)]

    return keysquare

def encrypt_playfair(message, keyword):
    """
    Encrypts a message using the Playfair Cipher.
    
    Args:
        message: The message to encrypt.
        keyword: The encryption keyword.
        
    Returns:
        The encrypted message.
    """
    keysquare = create_keysquare(keyword)
    encrypted_message = ""
    message = message.replace("j", "i")  # Handle "j"

    # Pad the message with an 'x' if its length is odd
    if len(message) % 2 == 1:
        message += "x"

    # Process Playfair Cipher Pairs (Digraphs)
    for i in range(0, len(message), 2):
        digraph = message[i:i + 2]

        # Find the position of each letter in the keysquare
        row1, col1 = find_indices(digraph[0], keysquare)
        row2, col2 = find_indices(digraph[1], keysquare)

        # Apply encryption rules
        if row1 == row2:
            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5
        elif col1 == col2:
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
        else:
            new_row1 = row1
            new_col1 = col2
            new_row2 = row2
            new_col2 = col1

        encrypted_digraph = keysquare[new_row1][new_col1] + keysquare[new_row2][new_col2]
        encrypted_message += encrypted_digraph

    return encrypted_message.upper()

def decrypt_playfair(message, keyword):
    """
    Decrypts a message using the Playfair Cipher.
    
    Args:
        message: The message to decrypt.
        keyword: The decryption keyword.
        
    Returns:
        The decrypted message.
    """
    keysquare = create_keysquare(keyword)
    decrypted_message = ""
    
    # Process Playfair Cipher Pairs (Digraphs)
    for i in range(0, len(message), 2):
        digraph = message[i:i + 2]
        
        # Find the position of each letter in the keysquare
        row1, col1 = find_indices(digraph[0], keysquare)
        row2, col2 = find_indices(digraph[1], keysquare)
        
        # Apply decryption rules
        if row1 == row2:
            new_col1 = (col1 - 1) % 5
            new_col2 = (col2 - 1) % 5
        elif col1 == col2:
            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5
        else:
            new_row1 = row2
            new_col1 = col1
            new_row2 = row1
            new_col2 = col2

        decrypted_digraph = keysquare[new_row1][new_col1] + keysquare[new_row2][new_col2]
        decrypted_message += decrypted_digraph

    return decrypted_message.lower()

def find_indices(letter, keysquare):
    """
    Finds the row and column of a given letter in the keysquare.

    Args:
        letter: The letter to find.
        keysquare: The keysquare to search in.

    Returns:
        The row and column of the letter in the keysquare.
    """

    for i in range(len(keysquare)):  # Iterate through each row (correct bounds for rows)
        for j in range(len(keysquare[0])):  # Iterate through each column
            if keysquare[i][j] == letter:
                return i, j
    raise ValueError(f"{letter} not found in keysquare")

def main():
    options = {
        "encrypt_playfair": encrypt_playfair,
        "decrypt_playfair": decrypt_playfair,
    }
    option = input("What do you want to do? (encrypt/decrypt): ")
    if option.isupper():
        option = option.lower()
    option += "_playfair"
    
    if option in options:
        message = input("Enter your message: ")
        keyword = input("Enter your keyword: ")
        message_result = options[option](message, keyword)
        print(f"Result: {message_result}")

if __name__ == "__main__":
    main()
