message = input("Enter the message: ")
shift = int(input("Enter the shift key (1 to 26): "))
operation = input("Do you want to encrypt or decrypt? ").strip().lower()

def caesar_cipher(message, shift, operation):
    result = ""
    
    if operation == "decrypt":
        shift = -shift
    
    for char in message:
        if char.isalpha():
            original_ascii = ord(char)
            if char.islower():
                shifted_ascii = (original_ascii - ord('a') + shift) % 26 + ord('a')
            elif char.isupper():
                shifted_ascii = (original_ascii - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted_ascii)
        else:
            result += char
    
    return result

result = caesar_cipher(message, shift, operation)
print(f"Processed message is: {result}")

