def alberti_cipher_disk(message, shift):
    """
    This function implements the Alberti Cipher Disk.
    """
    outer_disk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inner_disk = "DEFGHIJKLMNOPQRSTUVWXYZABC"  # Shifted 3 places to the left

    cipher_text = ""

    for letter in message:
        if letter.upper() in outer_disk:
            is_upper_case = letter.isupper()
            letter = letter.upper()

            # Find the position of the letter in the outer disk
            pos = outer_disk.index(letter)

            # Apply the shift to find the corresponding letter in the inner disk
            shifted_pos = (pos + shift) % 26
            shifted_letter = inner_disk[shifted_pos]

            # If the original letter was lowercase, make the shifted letter lowercase too
            if not is_upper_case:
                shifted_letter = shifted_letter.lower()

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
    cipher_text = alberti_cipher_disk(message, shift)

    # Display the encoded message
    print(f"\nThe encoded message is: {cipher_text}")


if __name__ == "__main__":
    main()
