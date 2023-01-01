import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == "decode":
        shift_amount *= -1
    end_text = []
    for c in start_text:
        if c in alphabet:
            letter_position = alphabet.index(c)
            end_text.append(alphabet[(letter_position+shift_amount) % len(alphabet)])
        else:
            end_text.append(c)
    return ''.join(end_text)


print(art.logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
 
    if direction == "encode" or direction == "decode":
        print(f"The {direction}d text is {caesar(start_text=text,shift_amount= shift, cipher_direction=direction)}")
    else:
        print("Unknown operation.")
 
    if input("Do you want to encode / decode again? (y/n)").lower() != 'y':
        print("Goodbye.")
        should_continue = False
