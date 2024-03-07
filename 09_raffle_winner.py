import pandas
import random

# list to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

mini_movie_frame['profit'] = mini_movie_frame['Ticket Price'] - 5

winner_name = random.choice(all_names)

win_index = all_names.index(winner_name)

total_won = mini_movie_frame.at[win_index, 'Total']

mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print()
print('---- Raffle Winner ----')
print(f"Congratulations {winner_name}. You have won ${total_won} ie: your ticket is free!")
