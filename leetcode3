expenses = []

while True:
    print("\n1. Add expense")
    print("2. View all expenses")
    print("3. View total expenses")
    print("4. View expenses by category")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append({"amount": amount, "category": category})
        print("Expense added.")
    elif choice == "2":
        for e in expenses:
            print(f"{e['category']}: ${e['amount']}")
    elif choice == "3":
        total = sum(e['amount'] for e in expenses)
        print(f"Total expenses: ${total}")
    elif choice == "4":
        cat = input("Enter category: ")
        cat_expenses = [e['amount'] for e in expenses if e['category'] == cat]
        print(f"Total for {cat}: ${sum(cat_expenses)}")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
