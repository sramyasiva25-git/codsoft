import random
import string

def calculator():
    print("        PASSWORD GENERATOR          ")
    
    length = int(input("Enter the length of the password: "))

    letters = string.ascii_letters     
    digits = string.digits             
    symbols = "!@#$%^&*"                

    all_characters = letters + digits + symbols

    password = ""

    
    for i in range(length):
        password = password + random.choice(all_characters)

    print("\nPassword Generated Successfully!")
    print("Generated Password:", password)

    
    print("\nThis password contains letters, numbers, and symbols.")
    
calculator()