import random

# Print a welcome message to the user
print("Welcome to the Password Generator")

# Ask the user for the number of letters, symbols, and numbers they want in their password
n_letters = int(input("How many letters would you like in your password?: "))
n_sym = int(input("How many symbols would you like?: "))
n_num = int(input("How many numbers would you like?: "))

# Generate a list of all lowercase letters (ASCII values 97 to 122 correspond to 'a' to 'z')
letters_l = list(map(chr, range(97, 123)))

# Create a list of uppercase letters by converting each lowercase letter to uppercase
letters_l_u = [char.upper() for char in letters_l]

# Combine the lists of lowercase and uppercase letters
letters_l.extend(letters_l_u)

# Add German umlaut characters to the list of letters
umlaute = ["ä", "Ä", "ö", "Ö", "ü", "Ü"]
letters_l.extend(umlaute)

# Define a list of symbols that can be used in the password
sym_l = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', "!", "%", "&"]

# Create a list of numbers from 0 to 9
num_l = list(map(int, range(0, 10)))

# Initialize a counter for the while loops and create empty lists for password components
x = 0
pass_letters_l = []

# While loop to add random letters to the pass_letters_l list until it reaches the desired number
while x < n_letters:
    y = random.randint(0, len(letters_l) - 1)
    pass_letters_l.append(letters_l[y])
    x = x + 1

# Reset the counter and create an empty list for numbers
x = 0
pass_num_l = []

# While loop to add random numbers to the pass_num_l list until it reaches the desired number
while x < n_num:
    y = random.randint(0, len(num_l) - 1)
    pass_num_l.append(num_l[y])
    x = x + 1

# Reset the counter and create an empty list for symbols
x = 0
pass_sym_l = []

# While loop to add random symbols to the pass_sym_l list until it reaches the desired number
while x < n_sym:
    y = random.randint(0, len(sym_l) - 1)
    pass_sym_l.append(sym_l[y])
    x = x + 1

# Convert all numbers in pass_num_l to strings to be able to join them later
pass_num_l = [str(element) for element in pass_num_l]

# Create a final list for the password content and add all the components to it
pw_content_l = []
pw_content_l.extend(pass_letters_l)
pw_content_l.extend(pass_num_l)
pw_content_l.extend(pass_sym_l)

# Use random.sample to draw a sample of elements from pw_content_l equal to its length and join them into a string
password = random.sample(pw_content_l, k=len(pw_content_l))
password = ''.join(password)

# Print the final password for the user
print(f"Your password is: {password}")
