import random
import string

def generate_strong_password(length=12):
    allowed_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(allowed_characters) for _ in range(length))
    return password

password = generate_strong_password(16)
print(f" High security password: {password}")
