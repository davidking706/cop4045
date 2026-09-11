"""David Evra - Homework 1, Problem 5: Interactive Caesar Cipher"""


def caesar_cipher(text, shift):
    """Return text with each English letter shifted by shift positions."""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""

    # A shift only needs to be between 0 and 25.
    shift = shift % 26

    for character in text:
        if character in lowercase:
            old_index = lowercase.index(character)
            new_index = (old_index + shift) % 26
            encrypted_text += lowercase[new_index]
        elif character in uppercase:
            old_index = uppercase.index(character)
            new_index = (old_index + shift) % 26
            encrypted_text += uppercase[new_index]
        else:
            # Spaces, numbers, and punctuation do not change.
            encrypted_text += character

    return encrypted_text


def caesar_decipher(cyphertext, shift):
    """Return the original text by shifting in the opposite direction."""
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    """Return case-insensitive counts for every English letter."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequencies = {}

    # Start every letter at zero so all 26 letters are in the result.
    for letter in alphabet:
        frequencies[letter] = 0

    for character in text.lower():
        if character in alphabet:
            frequencies[character] += 1

    return frequencies


def main():
    """Run the interactive Caesar cipher menu."""
    while True:
        print("\nCaesar Cipher Menu")
        print("1. Encrypt a message")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "2":
            print("Goodbye!")
            break

        if choice != "1":
            print("Please enter 1 or 2.")
            continue

        message = input("Enter a message: ")

        try:
            shift = int(input("Enter an integer shift: "))
        except ValueError:
            print("The shift must be an integer.")
            continue

        encrypted_text = caesar_cipher(message, shift)
        frequencies = letter_frequency(message)
        decrypted_text = caesar_decipher(encrypted_text, shift)

        print("Encrypted text:", encrypted_text)
        print("Letter frequencies:")
        for letter in frequencies:
            print(letter + ":", frequencies[letter])
        print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
