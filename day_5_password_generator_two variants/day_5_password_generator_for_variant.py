import random

# Greet the user and explain the purpose of the script
print("Welcome to the Password Generator")

# Collect user preferences for the number of letters, symbols, and numbers in the password
n_letters = int(input("How many letters would you like in your password?: "))
n_sym = int(input("How many symbols would you like?: "))
n_num = int(input("How many numbers would you like?: "))

# Generate a list of all lowercase letters using ASCII values
letters_l = list(map(chr, range(97, 123)))

# Create a list of uppercase letters from the lowercase list
letters_l_u = [char.upper() for char in letters_l]

# Combine lists of upper and lowercase letters
letters_l.extend(letters_l_u)

# Add special German characters (Umlaute) to the letters list
umlaute = ["ä","Ä", "ö", "Ö", "ü", "Ü"]
letters_l.extend(umlaute)

# Define a list of symbols for the password
sym_l = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', "!", "%", "&"]

# Create a list of numbers 0-9
num_l = list(map(int, range(0, 10)))

# Initialize an empty list to hold the password elements
pass_l = []

# Randomly select the specified number of letters and add them to the password list
for elements in range(1, n_letters + 1):
    y = random.randint(0, len(letters_l) - 1)
    pass_l.append(letters_l[y])

# Randomly select the specified number of symbols and add them to the password list
for elements in range(1, n_sym + 1):
    y = random.randint(0, len(sym_l) - 1)
    pass_l.append(sym_l[y])

# Randomly select the specified number of numbers and add them to the password list
for elements in range(1, n_num + 1):
    y = random.randint(0, len(num_l) - 1)
    pass_l.append(num_l[y])

# Convert all integers in the password list to strings
pass_l = [str(element) for element in pass_l]

# Shuffle the password list to ensure a random order and concatenate into a final password string
password = random.sample(pass_l, k=len(pass_l))
password = ''.join(password)

# Output the final password to the user
print(f"Your password is: {password}")
