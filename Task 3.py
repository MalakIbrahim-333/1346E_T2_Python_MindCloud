import random
import string

def generate_password(length):
    # characters to choose from
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    all_chars = upper + lower + digits + special

    # make sure at least one of each type is in the password
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # fill the rest with random picks
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # shuffle so the first four are not in a fixed order
    random.shuffle(password)

    return "".join(password)

# ask the user for password length
n = int(input("Enter password length: "))
if n < 4:
    print("Length should be at least 4 to include all character types.")
else:
    print("Generated password:", generate_password(n))
