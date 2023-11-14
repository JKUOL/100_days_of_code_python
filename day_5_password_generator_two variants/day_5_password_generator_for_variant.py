import random

print("Welcome to the Password Generator")

n_letters = int(input("How many letters would you like in your password?: "))
n_sym = int(input("How many symbols would you like?: "))
n_num = int(input("How many numbers would you like?: "))

# creates list out of all lower case letters
letters_l = list(map(chr, range(97, 123)))

#creates list of upper case letters out of letters_l
letters_l_u = [char.upper() for char in letters_l]

# creates list of upper and lower case letters
letters_l.extend(letters_l_u)

# adds "umlaute" to letters
umlaute = ["ä","Ä", "ö", "Ö", "ü", "Ü"]
letters_l.extend(umlaute)

# list of symbols
sym_l = ['\\', '/' ,':' ,'*', '?', '"', '<', '>', '|',"!","%","&"]

# list of numbers 0-9
num_l = list(map(int,range(0,10)))

# creates empty list
pass_l = []

# for every element in the range of 1 and the number of elements for the list choosen one random element of the 
# the letters list gets drawn and put into a list
for elements in range (1, n_letters+1):
    y = random.randint(0, len(letters_l) - 1)
    pass_l.append(letters_l[y])

for elements in range (1, n_sym+1):
    y = random.randint(0, len(sym_l) - 1)
    pass_l.append(sym_l[y])

for elements in range (1, n_letters+1):
    y = random.randint(0, len(num_l) - 1)
    pass_l.append(num_l[y])

# integers of the list get turned into strings
pass_l = [str(element) for element in pass_l ]

# random strings gets drawn of the list (no duplicates with .sample) and joined to one string
password = random.sample(pass_l, k = len(pass_l))
password = ''.join(password)

print(f"Your password is: {password}")