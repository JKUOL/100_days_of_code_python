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

# sets counter to 0 and creates empty list
x = 0
pass_letters_l = []
# while counter is smaller then the input number random elements get drawn from list and appended a list
while x < n_letters:
    y = random.randint(0, len(letters_l) - 1)
    pass_letters_l.append(letters_l[y])
    x = x + 1

x = 0
pass_num_l = []
while x < n_num:
    y = random.randint(0, len(num_l) - 1)
    pass_num_l.append(num_l[y])
    x = x + 1

x = 0
pass_sym_l = []
while x < n_sym:
    y = random.randint(0, len(sym_l) - 1)
    pass_sym_l.append(sym_l[y])
    x = x + 1

# transforms all list content to string format
pass_num_l = [str(element) for element in pass_num_l]

# creates empty list and extends it with the created random lists
pw_content_l = []
pw_content_l.extend(pass_letters_l)
pw_content_l.extend(pass_num_l)
pw_content_l.extend(pass_sym_l)

# draws random elements from the password list and joins them togethers as one string
password = random.sample(pw_content_l, k = len(pw_content_l))
password = ''.join(password)

print(f"Your password is: {password}")

