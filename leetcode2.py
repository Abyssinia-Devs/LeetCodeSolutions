password=input("Enter your password: ")
lenth_ok=len(password)>=7
for char in password:
    if  char.isdigit():
        has_number=True
    if char.isupper():
        have_upper=True
if lenth_ok and has_number and have_number:
    print("Strong password ✔️")
elif lenth_ok and (has_number or have_upper):
    print("Medium strength password ✔️")
else: print("Weak password ❌")
