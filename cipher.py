def encode_message(message):
    """
    Encode a message using a Caesar-style cipher with a fixed shift of 15.

    Rules:
    - Lowercase letters stay lowercase (a-z)
    - Uppercase letters stay uppercase (A-Z)
    - Spaces and punctuation are unchanged
    """
    shift = 15
    encoded = ""

    for ch in message:
        # Lowercase letters
        if ch.islower():
            new_code = ord(ch) + shift

            if new_code > ord("z"):
                new_code -= 26

            encoded += chr(new_code)

        # Uppercase letters
        elif ch.isupper():
            new_code = ord(ch) + shift

            if new_code > ord("Z"):
                new_code -= 26

            encoded += chr(new_code)

        # Spaces, punctuation, numbers
        else:
            encoded += ch

    return encoded


# Main program
user_message = input("Enter a message to encode: ")

result = encode_message(user_message)

print("\nEncoded message:")
print(result)
