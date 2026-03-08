import pandas

#lists to hold ticket details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket price':all_ticket_costs,
    'Surcharge': all_surcharges
}


#create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

#Calculate the total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket price'] - 5

#work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

print(mini_movie_frame)
print()
print(f"total_paid: ${total_paid:.2f}")
print(f"total_profit: ${total_profit:.2f}")