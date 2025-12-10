print("This is duplicate checker that means it checks if numbers repeated more than once.")

num1 = [7, 8, 3]
num2 = [2, 3, 4]

duplicates = set(num1) & set(num2)

if duplicates:
    print("Duplicated:", duplicates)
else:
    print("No duplicates found.")
