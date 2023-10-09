from hashlib import sha1

password = bytes(input("Enter your password: "), 'utf-8')
hashed_password = sha1(password).hexdigest()
print(f'Your hashed password is: {hashed_password}')
