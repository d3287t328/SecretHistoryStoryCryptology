import random

def create_polyphonic_cipher():
    """
    This function creates a polyphonic cipher.
    """
    cipher = {
        'a': ['1', '2'],
        'b': ['3', '4'],
        'c': ['5', '6'],
        'd': ['7', '8'],
        'e': ['9', '0'],
        # Add more mappings as needed
    }

    print("The Polyphonic cipher has been created:\n")
    for letter, codes in cipher.items():
        print(f"{letter}: {codes}")

    return cipher

def polyphonic_cipher(message, cipher):
    """
    This function encodes a message using a polyphonic cipher.
    """
    message = message.lower()
    cipher_text = ""

    for letter in message:
        if letter in cipher:
            # Randomly select one of the symbols for this letter
            symbol = random.choice(cipher[letter])
            cipher_text += symbol
            print(f"Encoding letter '{letter}' as '{symbol}'")
        else:
            cipher_text += letter  # Non-alphabet characters are left as-is

    return cipher_text

def main():
    """
    This function handles user interaction for the script.
    """
    # Create the polyphonic cipher
    cipher = create_polyphonic_cipher()

    # Get the message to encode
    message = input("\nEnter the message to encode: ")

    print("\nStart encoding the message:\n")

    # Encode the message
    cipher_text = polyphonic_cipher(message, cipher)

    # Display the encoded message
    print(f"\nThe encoded message is: {cipher_text}")


if __name__ == "__main__":
    main()
