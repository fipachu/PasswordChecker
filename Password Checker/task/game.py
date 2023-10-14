from hashlib import sha1

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
    while True:
        # Try to get password, if user inputs exit, return from main
        if (password := get_password()) is None:
            return
        # hashlib.sha1.hexdigest() returns lowercase hex number
        hashed = sha1(password.encode('utf-8')).hexdigest()
        print(f'Your hashed password is: {hashed}')

        prefix = hashed[:5]
        suffix = hashed[5:]
        url = f'https://api.pwnedpasswords.com/range/{prefix}'
        headers = {'Add-Padding': 'true'}

        print('Checking...')
        # TODO: check whether this line is accepted by unit test
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

        # # Alternatively, and, I think, less readably:
        # try:
        #     n = suffixes[suffix]
        # except KeyError:
        #     print("Good news! Your password hasn't been pwned.")
        # else:
        #     print(f'Your password has been pwned! The password "{password}"'
        #           f' appears {n} times in data breaches.')


if __name__ == "__main__":
    main()
