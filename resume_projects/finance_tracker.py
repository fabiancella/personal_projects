print("Welcome to the Personal Finance Tracker program")
print("\nThis program will help you budget on a monthly basis according to income and transactions that you provide.")
print("Categories consist of grocries, transportation")
running = True

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

        # adding to array
        add_transaction(cat, amount, desc)
        print("\nTransaction added")
        for i in transactions:
            print("Category:", i['category'], "\nAmount: $", i['amount'], "\nDescription:", i['description'])

def choice():
    global running
    user_choice = input("\nDo you want to add another transaction (yes/no)? ").lower()
    if user_choice == "yes":
        return data_collection
    elif user_choice == "no":
        print("\nOkay, no more")
        running = False
    else:
        print("Invalid input, please type 'yes' or 'no'.")
        return choice


def debt(debt_amount, category, amount):
    try:
        debt_amount = float(input("\nPlease enter the dollar amount of the debt"))
    except ValueError:
       print("Please try again and enter a number")
        
# user input their income and expenses
annual_income = int(input("\nPlease enter your annual income: "))

#Loop for program
while running == True:    
    #calling data collection function
    data_collection()
    choice()
    
    # if choice() == "no":
    #     print("Calculating monthly budget according to your annual income and monthly expenses")
    #     annual_income /= 12
    #     print("\nTotal monthly income\n")
    #     for i in ['amount']:
    #         print(i)
            