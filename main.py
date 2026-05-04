# Expense Tracker Project 

expenses = [] # list of expneses in form of dictionary
print(" Welcome to Expense Tracker  : Kharcha kam kiya kro ")

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4.Exit")

    choice = int(input("Please Enter your choice  :  "))
    
    if(choice ==1):
        date= input("Date of Expenditure")
        category= input("What Category ? (Food, Travel, Makeup, Books)")
        description= input("Any other details")
        amount= float(input("Enter the amount:   "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n Expenses are added successfully")

#2View all expenses
    elif(choice ==2):
            if( len(expenses)== 0):
                print("NO Expenses Added.")
            else:
                print("===== Expenses - Summary ======")
                count= 1
                for eachkharcha in expenses:
                    print(f"Kharcha Number {count} -> {eachkharcha["date"]}, {eachkharcha["description"], {eachkharcha["amount"]}}")
                    count = count+1


# 3 View Total Spending 
    elif(choice ==3):
         total= 0
         for eachkharcha in expensesList:
              total = total + eachkharcha["amount"]

        print("\n TOTAL Kharcha = ", total)
              
    
    
    
#4Exit
    elif(choice ==4):
        print("Thank you for using the expense tracker system")
        break

    else:
        print("Invalid Choice. Try again")
         
         

