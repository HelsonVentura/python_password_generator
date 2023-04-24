import random
import os

print("==============================")
print("Wellcome to password generator")
print("==============================")

chars = "abcdefghijklmnopqrstuvwxyzEiABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&0123456789"

print("Amount of password")
number = int(input())

print("Input your password length: ")
length = int(input())
os.system("cls")


print("\nhere are your passwords: ")
print("==============================")
for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
print("==============================")
