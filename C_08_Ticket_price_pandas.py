import pandas

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


def not_blank(question):
    """checks that user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

        print("sorry this cant be blank. please try again. \n")


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

#currency formating function
def currency(x):
    return "${:.2f}".format(x)
#main Routine goes here

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
    'Ticket price':all_ticket_costs,
    'Surcharge': all_surcharges
}

#get Ticket details

# #testing loop
while True:
    print()

    #ask user for their name (and check it's not blank)
    name = not_blank("name: ")
    if name == "xxx":
        break

    #ask user for their age and check it's between 12 and 120
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



    #ask user for payment method (cash / credit/ ca/ cr)
    pay_method = string_check("payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    #if paying by credit calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    #add name, ticket cost and surcharge
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

#create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

#Calculate the total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket price'] - 5

#work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

#Currency formating (use currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'total', 'profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)


# output movie frame without index
# print(mini_movie_frame)
print(mini_movie_frame.to_string(index=False))

print()
print(f"total_paid: ${total_paid:.2f}")
print(f"total_profit: ${total_profit:.2f}")