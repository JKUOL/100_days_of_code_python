import os

# ASCII Art for the Caesar Cipher logo
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
# Function to clear the console screen based on the operating system
def clear():
    # Clear command for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Clear command for macOS and Linux
    else:
        _ = os.system('clear')

# Function to perform the Caesar Cipher encryption/decryption
def ceasar(plain_message, shift_amount, cipher_direction):
    cipher_text = ""
    # Reverse the shift if decoding
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in plain_message:
        # Encrypt/decrypt only the alphabetic characters
        if char in letters_l:
            position = letters_l.index(char)
            new_position = position + shift_amount
            # Wrap around if the shift goes beyond the list
            if new_position >= len(letters_l):
                new_position -= len(letters_l)
            new_letter = letters_l[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    print(f"The {cipher_direction}d text is: {cipher_text}")

# Clear the screen and display the logo
clear()
print(logo)

# Main program loop
run = "y"
while run == "y" or run == "yes":
    cipher = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Validate the operation type
    while cipher not in ["encode", "decode"]:
        cipher = input("Wrong input, please choose 'encode' or 'decode':\n")

    message = input("Type your message:\n").lower()
    letters_l = list(map(chr, range(97, 123)))  # List of lowercase alphabet
    shift = int(input("Type the shift number:\n")) % len(letters_l)

    # Call the encryption/decryption function
    ceasar(message, shift, cipher)
    
    # Prompt to run the program again
    run = input("Do you want to run again? Type 'y' for Yes, or any other key to exit: ").lower()

print("Goodbye!")