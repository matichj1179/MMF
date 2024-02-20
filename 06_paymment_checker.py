# functions go here

# Checks user answer yes / no to a question
def cash_credit(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("please choose a valid payment method")


# main routine goes here
while True:
    payment_method = cash_credit("Choose a payment method (cash or credit): ")

    print(payment_method)