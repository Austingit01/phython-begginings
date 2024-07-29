import hashlib


def hash_password(password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return hash_password



password = input('Enter your password: ')
hashed_password = hash_password(password)
print(f'Hashed password: {hashed_password}')
