def caesar_cipher():
   

    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if choice in ['e', 'd']:
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

    message = input("Enter your message: ")
    while True:
        try:
            key = int(input("Enter the key (an integer from 1 to 25): "))
            if 1 <= key <= 25:
                break
            else:
                print("Invalid key. Please enter an integer between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if choice == 'd':
        key = -key

    result = ""
    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - start + key) % 26
            result += chr(start + shifted)
        else:
            result += char

    print("\nYour processed message is:")
    print(result)

if __name__ == "__main__":
    caesar_cipher()
