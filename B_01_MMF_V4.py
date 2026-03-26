import pandas
import random

#functions go here

def make_statement(statement, decoration):
    """add decoration at the start and end of text"""
    return f"{decoration * 3} {statement} {decoration * 3}"


def string_check(question, valid_answers =('yes', 'no'),
                 num_letters=1):
    """checks that the user enters the full word
    or 'n' letter/s of a word fom a list of responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:
            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")


def instructions():
    print(make_statement("instructions", "ℹ️"))

    print('''
for each ticket holder enter...
-their name
-their age
-their payment method (cash/credit)
this program will record the ticket sale and 
calculate the ticket cost (and the profit)
    
    
once you have either sold all of the tickets or entered the exit code ('xxx'),
the program will display the ticket sales information and write the data to 
a text file.

it will also choose one lucky ticket holder who wins the 
draw (their ticket is free)
    
    ''')


def not_blank(question):
    """checks that user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

        print("sorry this cant be blank. please try again. \n")


def int_checker(question):
    """checks that the users enter an integer"""

    error = "Oops - please enter an integer"




    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)

def currency(x):
    """formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)

# main routine bellow

# initialize ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise Variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

#credit card surcharge 5%
CREDIT_SURCHARGE = 0.05

#lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price':all_ticket_costs,
    'Surcharge': all_surcharges
}
#program main heading
print(make_statement("mini-movie fundraiser program", "="))

print()
want_instructions = string_check("do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

#loop to get name, age and payment details
while tickets_sold < MAX_TICKETS:
    #ask user for their name (and check it's not blank)
    print()
    name = not_blank("name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

        # ask user for their age and check it's between 12 and 120
    age = int_checker("age: ")

    #output error message /success message
    if age <12:
        print(f"{name} is too young")
        continue

    #child ticket price is $7.50
    elif age < 16:
        ticket_price = CHILD_PRICE

    #adult ticket ($10.50)
    elif age < 65:
        ticket_price = ADULT_PRICE

    # senior citizen ticket ($6.50)
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit/ ca/ cr)
    pay_method = string_check("payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})")

    if pay_method == "cash":
        surcharge = 0

    #if paying by credit calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    #add name, ticket cost and surcharge
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1
#end of ticket loop

#create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

#Calculate the total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

#work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

#choose a random winner
winner = random.choice(all_names)

#find the index of the winner (position in list)
winner_index = all_names.index(winner)


#retrive winner ticket price and profit (so we can
# adjust profit numbers)
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']


#Currency formating (use currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)


# output movie frame without index
# print(mini_movie_frame)
mini_movie_string = mini_movie_frame.to_string(index=False)

total_paid_string = f"total_paid: ${total_paid:.2f}"
total_profit_string = f"total_profit: ${total_profit:.2f}"


#winner announcement
lucky_winner_string = f"the lucky winner is {winner}. their ticket worth ${ticket_won:.2f} is free!"
final_total_paid_string = f"total paid is now ${total_paid - ticket_won:.2f}"
final_profit_string = f"total profit is now ${total_profit - profit_won:.2f}"


if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement(f"you have sold all the tickets "
                                     f"(ie: {MAX_TICKETS} tickets)", "-")
else:
    num_sold_string = make_statement(f"you havel sold {tickets_sold} / "
                                     f"{MAX_TICKETS} tickets.", "-")




#additional string/headings
heading_string = make_statement("Mini Movie Fundraiser", "=")
ticket_details_heading = make_statement("ticket details:", "-")
raffle_heading = make_statement("--- Raffle Winner ---", "-")
adjusted_sales_heading = make_statement("adjusted sales & profit", "-")

adjusted_explanation = (f"we have given away a ticket worth ${ticket_won:.2f} which means \nour"
                        f"sales have decreased by ${ticket_won:.2f} and our profit \n"
                        f"decreased by ${profit_won:.2f}.")
# list of strings to be outputted / written to file
to_write = [heading_string, "\n",
            ticket_details_heading,
            mini_movie_string, "\n",
            total_paid_string,
            total_profit_string, "\n",
            raffle_heading,
            lucky_winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explanation, "\n",
            final_total_paid_string,
            final_profit_string, "\n",
            num_sold_string,]
#print area
print()
for item in to_write:
    print(item)

#create file to hold data (add .txt extension)
file_name = "MMF_ticket_details"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

#write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
























