def caesar_cipher(message, shift):
    """
    This function implements the Caesar cipher.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = ""

    for letter in message:
        if letter.lower() in alphabet:
            is_upper_case = letter.isupper()
            letter = letter.lower()

            # Find the position of the letter in the alphabet and apply the shift
            shifted_pos = (alphabet.index(letter) + shift) % 26
            shifted_letter = alphabet[shifted_pos]

            # If the original letter was uppercase, make the shifted letter uppercase too
            if is_upper_case:
                shifted_letter = shifted_letter.upper()

            cipher_text += shifted_letter
            print(f"Encoding letter '{letter}' as '{shifted_letter}'")
        else:
            cipher_text += letter  # Non-alphabet characters are left as-is

    return cipher_text


def main():
    """
    This function handles user interaction for the script.
    """
    # Get the shift value
    shift = int(input("Enter the shift value (an integer): "))

    # Get the message to encode
    message = input("Enter the message to encode: ")

    print("\nStart encoding the message:\n")

    # Encode the message
    cipher_text = caesar_cipher(message, shift)

    # Display the encoded message
    print(f"\nThe encoded message is: {cipher_text}")


if __name__ == "__main__":
    main()

