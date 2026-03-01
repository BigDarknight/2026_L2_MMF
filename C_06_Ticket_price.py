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


#main Routine goes here

# initialise Variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

#credit card surcharge 5%
CREDIT_SURCHARGE = 0.05







# #testing loop
while True:
    print()

    #ask user for their name (and check it's not blank)
    name = not_blank("name: ")

    #ask user for their age and check it's between 12 and 120
    age = int_checker("age: ")

    #output error message /success message
    if age <12:
        print(f"{name} is too young")
        continue

    #child ticket price is $7.50
    elif 12 <= age < 16:
        ticket_price = ADULT_PRICE

    #adult ticket ($10.50)
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # senior citizen ticket ($6.50)
    elif 65 <= age < 121:
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

    #calculate total payable...
    total_to_pay = ticket_price + surcharge

    print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"so the total payable is ${total_to_pay:.2f}\n")