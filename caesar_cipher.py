def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            print("Exiting program.")
            break
        elif choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, -shift)  # Decrypt by shifting in the opposite direction
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()

