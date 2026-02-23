#functions go here

def make_statement(statement, decoration):
    """add decoration at the start and end of text"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


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
    make_statement("instructions", "ℹ️")

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

# main routine bellow

# initialize ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise Variables / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement("mini-movie fundraiser program", "🍿")

print()
want_instructions = string_check("do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    #ask user for their name (and check it's not blank)
    print()
    name = not_blank("name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

        # ask user for their age and check it's between 12 and 120
    age = int_checker("age: ")

    # output error message /success message
    if age < 12:
        print(f"sorry {name},you are too young for this movie.")
        continue
    elif age > 120:
        print(f"are you sure {name}? that looks like a typo")
        continue
    else:
        pass

    # ask user for payment method (cash / credit/ ca/ cr)
    pay_method = string_check("payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    input(f"you have sold all the tickets (ie: {MAX_TICKETS} tickets)")
else:
    print(f"you havel sold {tickets_sold} / {MAX_TICKETS} tickets. ")