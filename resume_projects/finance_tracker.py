print("Welcome to the Personal Finance Tracker program")
print("\nThis program will help you budget on a monthly basis according to income and transactions that you provide.")
print("Categories consist of groceries, transportation, housing, pets, insurance, etc.")
mainrunning = True
subrunning = True
while True:
        try:
            annual_income = int(input("\nPlease enter your annual income: "))
            break  # Exit the income input loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

transactions = []
# function to store transcation factors
def add_transaction(category, amount, description):
    # adding data to hashmap
    transaction = {
        "category": category,
        "amount": amount,
        "description": description,
    }
    transactions.append(transaction)

def data_collection():
    #collecting data
        cat = input("\nPlease enter the category of transaction: ").title()
        try:
            amount = float(input("Please enter the amount for the transaction: "))
        except ValueError:
            print("Please try again and enter a number")
            return

        desc = input("Please enter a brief description: ").title()
        print("Adding...")

        # adding data to array
        add_transaction(cat, amount, desc)
        print("\nTransaction added")

        for i in transactions:
            print("\nCategory:", i['category'], "\nAmount: $" + str(i['amount']), "\nDescription:", i['description'])
        return choice()

# def sort_category():


def choice():
    global subrunning
    user_choice = input("\nDo you want to add another transaction (yes/no)? ").lower()
    while True:    
        if user_choice == "yes":
            return data_collection()
        elif user_choice == "no":
            print("\nOkay, no more")
            choice2 = input("Would you like to sort the list by category or by amount (cat/num)?: ")
            print("\nAll transactions")
            print("Category:\t\tAmount:\t\t\tDescription:")
            for i in transactions:
                    if choice2 == "cat":
                        sorted_transactions = sorted(transactions, key=lambda transaction: transaction['category'][0])
                        print(i['category'], "\t\t\t", i['amount'], "\t\t", i['description'])
                    elif choice2 == "num":
                        sorted_transactions = sorted(transactions, key=lambda transaction: transaction['amount'])
                        print(i['category'], "\t\t\t", i['amount'], "\t\t", i['description'])
            subrunning = False
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")
            return choice()

# function to calculate the monthly expenses
def total_expenses():
    total_amount = 0
    for transacion in transactions:
        total_amount += transacion['amount']
    print("\nTotal monthly expenses: $" + str(total_amount))
    return total_amount
# Calculate total expenses and store the result

# initialized list and func for tracking saving goals    
goals_list = []
def goals(bills, spending, saving):
    goal_hash = {
        "bills": bills,
        "spending": spending,
        "saving": saving,
    }
    goals_list.append(goal_hash)

# inputs for percentage of income to save, spend, and use for bills 
def goal_input():
    print("\nThe standard rule is 50% for bills, 30% for spending, and 20% to save.")
    bills_input = int(input("Enter what percentage a month you would like to allocate towards bills (e.g., 50 for 50%): ")) / 100
    spending_input = int(input("Enter what percentage a month you would like to spend (e.g., 30 for 30%): ")) / 100
    saving_input = int(input("Enter what percentage a month you would like to save (e.g., 20 for 20%): ")) / 100
    print("\nCalculating...")
    
    #adds to array
    goals(bills_input, spending_input, saving_input)


def debt(debt_amount, category, amount):
    try:
        debt_amount = float(input("\nPlease enter the dollar amount of the debt"))
    except ValueError:
       print("Please try again and enter a number")
        
#Loop for program
while mainrunning == True:
    # user input their expenses
    while subrunning == True:
        data_collection()
    
    total_expenses_value = total_expenses()
    # inputs for percentage of income to save, spend, and use for bills
    goal_input()
    monthly_income = annual_income/12
    for i in goals_list:
        bills_percent = i['bills'] * monthly_income
        spending_percent = i['spending'] * monthly_income
        saving_precent = i['saving'] * monthly_income
    print("You should allocate $" + str(bills_percent) + " to bills, $" + str(spending_percent) + " for spending, and $" + str(saving_precent) + " for saving every month")

    
    break