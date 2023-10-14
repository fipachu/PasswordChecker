from hashlib import sha1
import argparse

import requests


def get_password(min_length=8) -> str | None:
    while True:
        password = input("Enter your password (or 'exit' to quit): ")
        if password == 'exit':
            return None
        elif len(password) < min_length:
            print('Your password is too short. Please enter a password of'
                  f' at least {min_length} characters.')
        else:
            return password


def main():
    descr = ('Interactive program to check password safety against'
             ' haveibeenpwnd.com API')
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('-s', '--show-hash',
                        help='show the full hashed password in the output',
                        action='store_true')
    args = parser.parse_args()

    # Interactive CLI loop
    while True:
        # Try to get password, if user inputs exit, return from main
        if (password := get_password()) is None:
            return
        # hashlib.sha1.hexdigest() returns lowercase hex number
        hashed = sha1(password.encode('utf-8')).hexdigest()
        if args.show_hash:
            print(f'Your hashed password is: {hashed}')

        prefix = hashed[:5]
        suffix = hashed[5:]
        url = f'https://api.pwnedpasswords.com/range/{prefix}'
        headers = {'Add-Padding': 'true'}

        print('Checking...')
        # # This line is accepted by the test, but not necessary
        # print(f'A request was sent to "{url}" endpoint, awaiting response...')
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # Raise exception if GET failed

        # Make response text lowercase for compatibility with hexdigest.
        # ...yes it was a sneaky bug at one point...
        # It could be the other way around, but I like the look of lowercase.
        suffixes: str = r.text.lower()
        suffixes: dict[str, str] = dict(line.split(':')
                                        for line in suffixes.split('\r\n'))

        if suffix in suffixes and (n := suffixes[suffix]) != 0:
            print(f'Your password has been pwned! The password "{password}"'
                  f' appears {n} times in data breaches.')
        else:
            print("Good news! Your password hasn't been pwned.")


if __name__ == "__main__":
    main()
