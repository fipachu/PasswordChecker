import requests
from hashlib import sha1


def is_valid(s, min_length) -> bool:
    return len(s) >= min_length


def main():
    while True:
        password = bytes(input("Enter your password: "), 'utf-8')
        if is_valid(password, 8):
            hashed_password = sha1(password).hexdigest()
            print(f'Your hashed password is: {hashed_password}')

            # flush to make sure it prints before requests.get does its job
            print('Checking...', flush=True)
            r = requests.get(f'https://api.pwnedpasswords.com/range/{hashed_password[:5]}')
            print(f'A request was sent to "{r.url}" endpoint, awaiting response...')
            # print(r.text)  # Not yet, not in this stage
            break
        else:
            print('Your password is too short. Please enter a password of '
                  'at least 8 characters.')


# Necessary to let the unit test know to use game.py as entry point
if __name__ == "__main__":
    main()
