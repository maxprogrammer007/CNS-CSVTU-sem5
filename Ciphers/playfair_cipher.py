def generate_key_square(key):
    """Generates the 5x5 key square for the Playfair cipher."""
    key = key.lower().replace(" ", "").replace("j", "i")
    key_square = ""
    for char in key:
        if char not in key_square:
            key_square += char
    
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in key_square:
            key_square += char
            
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_char_coords(key_square, char):
    """Finds the coordinates of a character in the key square."""
    if char == "j":
        char = "i"
    for r, row in enumerate(key_square):
        for c, cell in enumerate(row):
            if cell == char:
                return r, c
    return -1, -1 

def prepare_message(message):
    """Prepares the message for Playfair cipher encryption."""
    message = message.lower().replace(" ", "").replace("j", "i")
    prepared_message = ""
    i = 0
    while i < len(message):
        prepared_message += message[i]
        if i + 1 < len(message):
            if message[i] == message[i+1]:
                prepared_message += "x"
            else:
                prepared_message += message[i+1]
                i += 1
        else:
            prepared_message += "x"
        i += 1
    return [prepared_message[i:i+2] for i in range(0, len(prepared_message), 2)]

def playfair_cipher(key, message, mode):
    """Encrypts or decrypts a message using the Playfair cipher."""
    key_square = generate_key_square(key)
    message_pairs = prepare_message(message)
    result = ""

    for pair in message_pairs:
        r1, c1 = find_char_coords(key_square, pair[0])
        r2, c2 = find_char_coords(key_square, pair[1])

        if r1 == r2:  # Same row
            result += key_square[r1][(c1 + mode) % 5]
            result += key_square[r2][(c2 + mode) % 5]
        elif c1 == c2:  # Same column
            result += key_square[(r1 + mode) % 5][c1]
            result += key_square[(r2 + mode) % 5][c2]
        else:  # Rectangle
            result += key_square[r1][c2]
            result += key_square[r2][c1]
            
    return result

if __name__ == "__main__":
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if choice in ['e', 'd']:
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

    key = input("Enter the keyword: ")
    message = input("Enter the message: ")

    if choice == 'e':
        encrypted_message = playfair_cipher(key, message, 1)
        print("\nEncrypted message:", encrypted_message)
    else:
        decrypted_message = playfair_cipher(key, message, -1)
        print("\nDecrypted message:", decrypted_message)
