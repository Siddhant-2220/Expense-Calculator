# Expense Tracker Project 

expenses = []  # list of expenses in form of dictionary
print("Welcome to Expense Tracker : Kharcha kam kiya kro ")

while True:
    print("\n=== Menu ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter your choice: "))

    # 1. Add Expense
    if choice == 1:
        date = input("Date of Expenditure: ")
        category = input("Category? (Food, Travel, Makeup, Books): ")
        description = input("Any other details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\nExpense added successfully!")

    # 2. View All Expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses added.")
        else:
            print("\n===== Expenses Summary =====")
            count = 1
            for eachkharcha in expenses:
                print(f"{count}. {eachkharcha['date']} | {eachkharcha['category']} | {eachkharcha['description']} | ₹{eachkharcha['amount']}")
                count += 1

    # 3. View Total Expenses
    elif choice == 3:
        total = 0
        for eachkharcha in expenses:
            total += eachkharcha["amount"]

        print("\nTOTAL Kharcha = ₹", total)

    # 4. Exit
    elif choice == 4:
        print("Thank you for using the expense tracker system")
        break

    else:
        print("Invalid Choice. Try again")