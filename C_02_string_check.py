# Functions go here
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

# Main routine goes here

payment_ans = ('cash', 'credit')

like_coffee = string_check("do you want instructions? ")
print(f"you chose {like_coffee}")
pay_method = string_check("payment method: ", payment_ans, 2)
print(f"you chose: {pay_method}")