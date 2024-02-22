# functions go here


# checks user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# checks users age is correct
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an integer")


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # tickets price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a lst of options
def string_checker(question, num_letters, valid_response):
    error = f"please choose {valid_response[0]} or {valid_response[1]}"



    while True:

        response = input(question).lower()

        for item in valid_response:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine goes here

# set max amount of tickets here
MAX_TICKETS = 3
tickets_sold = 0
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# ask user if they want to see the instructions

want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)
print("You chose", want_instructions)

if want_instructions == "yes":
    print("instructions go here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' quit) ")

    if name == 'xxx':
        break
    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again")
        continue

    # calculate ticket price
    tick_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("Choose a payment method (cash / credit)", 2, payment_list)
    print(f"you chose {pay_method}")

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s remaining")
