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


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)
    print("You chose", want_instructions)

for case in range(0, 5):
    pay_method = string_checker("...", 2, payment_list)
    print("you chose", pay_method)
