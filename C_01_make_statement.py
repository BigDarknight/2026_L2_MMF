# functions go here
def make_statement(statement, decoration):
    """add decoration at the start and end of text"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


# Main routine goes here
make_statement("instructions", decoration= "ℹ️")
