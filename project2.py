# Exp Tracker Project

ExpensesList = [] #list of all exp of dicstinary
print("welcome to Exp Tracker: spend less money on unnessary stuff")

while True:
    print("=====Menu=====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses ")
    print("4. Exit")

    Choice =  int(input("Please Enter Your Choice : "))

# Add expense.
    if(Choice ==1):
        date = input("In which date you have spend money ?: ")
        category = input("which kind of category?  (Food, Travel, Books, Make-up, etc): ")
        Description = input("Give more detail about category:" )
        Amount = float(input("Enter the amount : "))

        Expenses = {
                    "date": date,
                    "category": category,
                    "despription": Description,
                    "Amount": Amount
                    }
                
        ExpensesList.append(ExpensesList)
        print(" \n Done bro. Expenses is added successfully.")

# 2. View All Expense
    elif (Choice==2):   
        if ( len(ExpensesList)==0 ):
                            
         print("No Expenses Add. first go and spend money.")
        else:
            print("========This is all your expense======")
            count = 1
            for eachitem in ExpensesList:
             print(f"expense number {count} -> {eachitem["date"]},{eachitem["category"]}, {eachitem["description"]}, {Amount["amount"]}")


# 3.View Total Spending
    elif(Choice == 3):
        total = 0
        for eachitem in ExpensesList:
             total = total + eachitem["amount"]
        print(" \n Total expenses = ",total) 


# 4.Exit
    elif(Choice==4):
       print("Thankyou for using our system .")
       break

    else:
       print("INVALID CHOICE , TRY AGAIN")

