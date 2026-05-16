import re
import random
import string
import hashlib

common_passwords = ["123456", "password", "admin", "qwerty"]


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_old_password(hashed_password):
    try:
        with open("old_passwords.txt", "r") as file:
            old_passwords = file.read().splitlines()

        return hashed_password in old_passwords

    except FileNotFoundError:
        return False


def save_password(hashed_password):
    with open("old_passwords.txt", "a") as file:
        file.write(hashed_password + "\n")


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if password.lower() in common_passwords:
        feedback.append("This password is too common")
        score = 1

    return score, feedback


def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(12))


password = input("Enter your password: ")

hashed_password = hash_password(password)


if check_old_password(hashed_password):
    print("\nWarning: This password was already used before!")

else:
    save_password(hashed_password)

score, feedback = check_password_strength(password)

print("\nPassword Analysis Result")

if score <= 2:
    print("Weak Password")

elif score == 3 or score == 4:
    print("Medium Password")

else:
    print("Strong Password")

print("\nSuggestions:")

for item in feedback:
    print("-", item)

if score < 5:
    print("\nSuggested Strong Password:")
    print(generate_strong_password())

else:
    print("\nYour password is already strong. No suggestions needed.")