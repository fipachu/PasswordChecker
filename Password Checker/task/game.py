from hashlib import sha1


def is_valid(s, min_length) -> bool:
    return len(s) >= min_length


while True:
    password = bytes(input("Enter your password: "), 'utf-8')
    if is_valid(password, 8):
        hashed_password = sha1(password).hexdigest()
        print(f'Your hashed password is: {hashed_password}')
        break
    else:
        print('Your password is too short. Please enter a password of '
              'at least 8 characters.')
