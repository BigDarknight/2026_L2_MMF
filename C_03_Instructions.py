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
# main routine bellow

make_statement("mini-movie fundraiser program", "🍿")

print()
want_instructions = string_check("do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("program continues...")