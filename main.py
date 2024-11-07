# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            if shifted_position < 0:
                cipher_text += alphabet[len(alphabet) + shifted_position]
            else:
                cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")

def caesar(original_text, shift_amount, encode_or_decode):

    encode_or_decode = encode_or_decode.lower()
    if encode_or_decode == "encode":
        encrypt(original_text, shift_amount)
    elif encode_or_decode == "decode":
        decrypt(original_text, shift_amount)
    else:
        print("Invalid input - please restart the program")


# TODO-3: Can you figure out a way to restart the cipher program?

finished = False

while not finished:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again == 'no':
        finished = True
        print ('Good bye')