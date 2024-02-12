# functions go here

# Checks user answer yes / no to a question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "show instructions"

        elif response == "no" or response == "n":
            return "code continues"

        else:
            print("please answer yes / no")


# main routine goes here
show_instructions = yes_no("Do you want to see the instructions? ")

print(show_instructions)