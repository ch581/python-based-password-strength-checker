password = input("Enter Your Password :").strip()

# Special Characters
special_characters = []

# Numbers
numeric_char = []

# Alphabets
alpha_chars = []

for char in password:
    # Special characters
    if not char.isalnum():
        special_characters.append(char)
    
    # Numbers
    elif char.isnumeric():
        numeric_char.append(char)
    
    # Alphabets
    elif char.isalpha():
        alpha_chars.append(char)

# Conditions to check strength
if len(password) < 8:
    print("Your password must have at least eight characters")
elif special_characters and numeric_char and alpha_chars:
    print("Your Password is strong")
elif not special_characters and numeric_char and alpha_chars:
    print("Good Password")
elif not special_characters and not numeric_char and alpha_chars:
    print("It is a weak Password")
else:
    print("Your password does not meet the required conditions")


