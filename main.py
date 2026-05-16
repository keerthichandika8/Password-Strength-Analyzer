import re

password = input("Enter your password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 2
else:
    print("❌ Password should contain at least 8 characters")

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1
else:
    print("❌ Add uppercase letters")

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1
else:
    print("❌ Add lowercase letters")

# Number Check
if re.search(r"[0-9]", password):
    score += 1
else:
    print("❌ Add numbers")

# Special Character Check
if re.search(r"[@#$%^&*!]", password):
    score += 2
else:
    print("❌ Add special characters")

# Final Result
print("\nPassword Score:", score)

if score <= 3:
    print("🔴 Weak Password")
elif score <= 6:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")