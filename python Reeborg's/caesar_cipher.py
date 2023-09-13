import logo
print(logo.caesar_cipher)


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' a inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
    
#TODO-3: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-4: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")
#TODO-5: Cheack if the user wanted to encrypt or decrypt the message chaking the 'diraction' variable. Then call the currect function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)
    
#TODO-6: Combine the encrypt() and decrypt() functions into a single function called caesar()
def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += letter
    print(f"The {cipher_direction} text is {end_text}")
#TODO-7: Call the ceaser() function, passing over the 'text', 'shift' and 'direction' values.
should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    shift = shift % 26
    caeser(start_text = text, shift_amount = shift, cipher_direction = direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if result == 'no':
        should_continue = False
        print(logo.goodbye)
#TODO-8: What if the user enters shift that is greter than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45
#Hint: Think about how can use the modulus (%)

#TODO-9: What happens if the user enters a number/symbol/space?
#can you fix the code to keep the number/symbol/space when the text is encode/decoded? 