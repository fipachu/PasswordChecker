def valid_length(s, min_length) -> bool:
    return len(s) >= min_length


while True:
    password = input("Enter your password: ")
    if valid_length(password, 8):
        print(f"You entered: {password}")
        break
    else:
        print('Your password is too short. Please enter a password of '
              'at least 8 characters.')
