#Name: Kendyl Evatt
#Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price of an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############## Define global variables  ##############
# Meal prices, tax rate, and service fee
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SALES_TAX_RATE = 0.062
SERVICE_FEE = 0.10

############## Define Global Variables ##############
num_adult_meals = 0
num_child_meals = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0

############## Define program Functions ##############
def main():
    more_orders = True

    while more_orders:
        get_user_data()
        perform_calculations()
        display_results()

        # Ask if user wants to place another order
        yesno = input("Would you like to order again (Y or N)? ").strip().lower()
        if yesno == "n":
            more_orders = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meals, num_child_meals

    # Get number of adult meals
    while True:
        try:
            num_adult_meals = int(input("Enter the number of adult meals: "))
            if num_adult_meals < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative integer for adult meals.")

    # Get number of child meals
    while True:
        try:
            num_child_meals = int(input("Enter the number of child meals: "))
            if num_child_meals < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative integer for child meals.")

def perform_calculations():
    global subtotal, sales_tax, service_fee, total

    # Calculate subtotal, tax, service fee, and total
    subtotal = (num_adult_meals * ADULT_MEAL) + (num_child_meals * CHILD_MEAL)
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE
    total = subtotal + sales_tax + service_fee

def display_results():
    print('-------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('-------------------------------')
    print(f'Adult Meals   $ {num_adult_meals * ADULT_MEAL:8,.2f}')
    print(f'Child Meals   $ {num_child_meals * CHILD_MEAL:8,.2f}')
    print(f'Subtotal      $ {subtotal:8,.2f}')
    print(f'Sales Tax     $ {sales_tax:8,.2f}')
    print(f'Service Fee   $ {service_fee:8,.2f}')
    print(f'Total         $ {total:8,.2f}')
    print('-------------------------------')
    print('Date: ' + str(datetime.datetime.now()))
    print('-------------------------------')

############## Run the Program ##############
main()
