password = input("Enter your password: ")
length_ok = len(password) >= 8
#has_number = False
#has_upper = False

for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True

if length_ok and has_number and has_upper:
    print("Strong password ✔️")
elif length_ok and (has_number or has_upper):
    print("Medium strength password ✔️")
else:
    print("Weak password ❌")
