import pandas
import random

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

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_response:
            if response == item[:short_version] or response == item:
                return item

        print(error)


def currency(x):
    return f"{x:.2f}"


# main routine goes here

# set max amount of tickets here
MAX_TICKETS = 5
tickets_sold = 0
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

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

    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = tick_cost * 0.05

    tickets_sold += 1

    all_names.append(name)
    all_ticket_costs.append(tick_cost)
    all_surcharge.append(surcharge)


#  ***  Once tickets have been sold, create panda ***
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

winner_name = random.choice(all_names)



print("---- Ticket Data ----")
print()

# output table with ticket data
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit -----")

# output total ticker sales and profit
print(f"Total ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")
