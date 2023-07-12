"""
. Creating a simple password generator;
"""
from random import choice
import string

password = ""
passwd_lenght = int(input("Input the password's lenght: "))
characters = string.ascii_letters + string.digits + string.punctuation

for element in range(passwd_lenght):
    password += choice(characters)

print(f"New password here: {password}")
