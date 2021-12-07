from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            
def caesar(start_text, shift_amount, option):
    cipher_text = ''
# loop over the each character of the text
    for n in range(len(start_text)):
#if the nth character is not a letter, don't do anything and store it in the new cipher text var
        if start_text[n] not in alphabet:
            cipher_text += start_text[n]
        else:
#if user entered encoded        
            if option == 'encode':
                text_locate = alphabet.index(start_text[n]) + shift_amount
                if text_locate > 25:
                    excess_locate = text_locate % 26
                    cipher_text += alphabet[excess_locate]
                else:
                    cipher_text += alphabet[text_locate]
            elif option == 'decode':
                text_locate = alphabet.index(start_text[n]) - shift_amount
                if text_locate < -25:
                    excess_locate = text_locate % 26
                    cipher_text += alphabet[excess_locate]
                elif text_locate < 0:
                    excess_locate = text_locate + 26
                    cipher_text += alphabet[excess_locate]
                else:
                    cipher_text += alphabet[text_locate]        
    print(f"Here's the {direction}d result: {cipher_text}")
    
print(logo)

start_game = True

while start_game: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Hit any key and press enter if you want to retry. Otherwise type 'no' to exit. ").lower()
    if restart == 'no':
        break

# shift = 1222 to nullify cipher
