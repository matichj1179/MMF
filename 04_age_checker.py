# functions go here

# checks users enter and integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an integer")


# Main routine goes here
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
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

    tickets_sold += 1

print(f"You have sold {tickets_sold} ticket/s.")
