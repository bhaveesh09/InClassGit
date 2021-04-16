import random 
import string

password_length = int(input("Enter length of password: "))

valid = string.ascii_letters + string.digits
password = []

for i in range (password_length):
    password.append(random.choice(valid))
print(''.join(password))