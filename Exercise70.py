message = input("Enter the message: ")
shift = int(input("Enter the shift amount: "))
encoded_message = ""
for char in message:
    if char.isalpha():
        shift_amount = shift % 26  # Ensure the shift amount is within the range of the alphabet
        if char.islower():
            encoded_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
        else:
            encoded_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        encoded_message += encoded_char
    else:
        encoded_message += char
print(f"The encoded message is: {encoded_message}")