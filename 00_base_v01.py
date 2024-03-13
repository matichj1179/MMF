import pandas
import random
from datetime import date

# functions go here


# shows instructions
def show_instructions():
    print('''
ℹ️ℹ️ℹ️ Instructions go here ℹ️ℹ️ℹ️

here they are
- thing one
- thing two
- thing three
        
        ''')


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

        for var_item in valid_response:
            if response == var_item[:short_version] or response == var_item:
                return var_item

        print(error)


def currency(x):
    return f"${x:.2f}"


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

if want_instructions == "yes":
    show_instructions()

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' quit) ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

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

# choose winner and look up total
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# 💰💰💰 Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

winner_name = random.choice(all_names)

print("---- Ticket Data ----")
print()

# output table with ticket data
mini_movie_frame = mini_movie_frame.set_index('Name')

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = f"-----The current date is {day}/{month}/{year}-----"
filename = f"MMF_{year}_{month}_{day}"

mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = f"Total Ticket Sales: ${total}"
total_profit = f"Total Profit: ${profit}"

sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The winner of the raffle is {winner_name} " \
              f"They have won ${total_won}. ie: their ticker is" \
              "free!"

# list holding content to print
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
