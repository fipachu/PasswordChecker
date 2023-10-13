import requests
from hashlib import sha1



def get_password(min_length=8) -> str:
    while len(password := input('Enter your password: ')) < min_length:
        print('Your password is too short. Please enter a password of'
              f' at least {min_length} characters.')
    return password


def main():
    password = get_password()
    hashed = sha1(password.encode('utf-8')).hexdigest()
    print(f'Your hashed password is: {hashed}')

    # flush to make sure it prints before requests.get does its job
    print('Checking...', flush=True)
    r = requests.get(f'https://api.pwnedpasswords.com/range/{hashed[:5]}')
    print(f'A request was sent to "{r.url}" endpoint, awaiting response...')
    # print(r.text)  # Not yet, not in this stage


# Necessary to let the unit test know to use game.py as entry point
if __name__ == "__main__":
    main()
