from string import digits, ascii_letters, punctuation
from random import choice


def generate():

    Password_len = int(input("Enter passwords length: "))
    Symbol = input("Do you need special characters? (y/n): ")

    if Symbol == "y":
        dictionary = ascii_letters + digits + punctuation
        Password = "".join(choice(dictionary) for i in range(Password_len))
    else:
        dictionary = ascii_letters + digits
        Password = "".join(choice(dictionary) for i in range(Password_len))

    return Password
