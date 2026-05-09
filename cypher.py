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
        # Case 1: lowercase letter
        if ch.islower():
            new_code = ord(ch) + shift

            # Wrap around if we go past 'z'
            if new_code > ord('z'):
                new_code -= 26

            encoded += chr(new_code)

        # Case 2: uppercase letter
        elif ch.isupper():
            new_code = ord(ch) + shift

            # Wrap around if we go past 'Z'
            if new_code > ord('Z'):
                new_code -= 26

            encoded += chr(new_code)

        # Case 3: not a letter (space, punctuation, numbers, etc.)
        else:
            encoded += ch

    return encoded


# -------------------- Main program --------------------
# Get input from the user
user_message = input("Enter a message to encode: ")

# Encode the message
result = encode_message(user_message)

# Display the result clearly
print("\nEncoded message:")
print(result)
