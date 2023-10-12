# author: https://hyperskill.org/profile/1254124
# source: https://hyperskill.org/projects/381/stages/2271/implement#solutions-2532994
import hashlib

while len(password := input('Enter your password: ')) < 8:
    print('Your password is too short. Please enter a password of at least 8 characters.')
print('Your hashed password is:', hashlib.sha1(password.encode()).hexdigest())
