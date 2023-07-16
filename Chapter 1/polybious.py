def create_polybius_square():
    """
    This function creates a Polybius square which is a 5x5 grid of the 
    alphabet, excluding 'j' which is usually combined with 'i'.
    """
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # Alphabet without 'j'
    square = {}

    # Populate the square
    for i, letter in enumerate(alphabet):
        row = i // 5 + 1
        col = i % 5 + 1
        square[letter] = str(row) + str(col)

    print("The Polybius square has been created:\n")
    for i in range(1, 6):
        for j in range(1, 6):
            for letter, code in square.items():
                if code == str(i) + str(j):
                    print(f"{letter} ({code})", end=" ")
        print("\n")
    return square


def polybius_cipher(message, square):
    """
    This function encodes a message using a Polybius square.
    """
    # Normalize the message
    message = message.lower().replace("j", "i")

    # Encode the message
    cipher_text = ""
    for letter in message:
        if letter in square:
            cipher_text += square[letter]
            print(f"Encoding letter '{letter}' as '{square[letter]}'")
        else:
            cipher_text += letter  # Non-alphabet characters are left as-is

    return cipher_text

def main():
    """
    This function handles user interaction for the script.
    """
    # Create the Polybius square
    square = create_polybius_square()

    # Get the message to encode
    message = input("\nEnter the message to encode: ")

    print("\nStart encoding the message:\n")

    # Encode the message
    cipher_text = polybius_cipher(message, square)

    # Display the encoded message
    print(f"\nThe encoded message is: {cipher_text}")


if __name__ == "__main__":
    main()
