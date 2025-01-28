import secrets 
import string 

def gen_password(length = 15):
    if length < 5:
        raise ValueError("Error the password should at least be five characters long")

    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    password = [
    secrets.choice(letters),
    secrets.choice(digits),
    secrets.choice(punctuation),
]

    all_characters = letters + digits + punctuation
    password.extend(secrets.choice(all_characters)for _ in range(length - 3))
    secrets.SystemRandom().shuffle(password)
    return " ".join(password)

print(gen_password(15))