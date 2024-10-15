print("Welcome to the Personal Finance Tracker program")
running = True

# function to store transcation factors
def add_transaction(amount, category, description):
    # adding data to hashmap
    transaction = {
        "amount": amount,
        "category": category,
        "description": description,
    }

# function to store user inputed income
def annual_income():
    annual_income = []
    monthly_income = []

def question():
    input("\nDo you want to add another expense/transation")

# user input their income and expenses
annual_income = float(input("\nPlease enter your annual income"))
while running == True:
    print