def encryption(text,shift):
    encrypted=""
    shift_value = shift % 26
    for char in text:
        if char.isalpha():
            if char.islower():
                new_char=chr(((ord(char) - ord('a')+ shift_value) % 26) + ord('a'))
                encrypted += new_char
            else:
                new_char=chr(((ord(char) - ord('A')+ shift_value) % 26) + ord('A'))
                encrypted += new_char
        else:
            encrypted += char
    return encrypted
def decryption(text,shift):
    return encryption(text, -shift)
text = input("Enter plain text: ")
shift = int(input("Enter shift amount:")) 
enc=encryption(text,shift)
print("Encrypted text is: " +encryption(text,shift))
option = int(input("if you want to Decrypt it enter 1 else put any thing:"))
if option == 1:
    print("Decrypted text is: " +decryption(enc,shift))
    print("Thankyou✌")
else:
    print("Thankyou✌")