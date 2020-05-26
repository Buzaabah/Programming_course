"""
File: average2numbers.py
------------------------
This program asks the user for two numbers
and prints their average.
"""
"""
Arithmetic operations:
----------------------
+ Addition: integer addition returns integer otherwise float
- subtraction: Integer subtraction returns integer otherwise float
* Multiplication: integer multiplication returns integer otherwise float
/ Division: Division always returns float
// division: Division that returns integer
% reminder operator: Only returns a reminder value when dividing 
** raised to: returns x raised to some value y
- negation: returns the negative of a given value x.


Note: float values are not always exact, ie;
ie: 1.9 - 1 == 0.8999999999 and not 0.9
BODMAS
"""
def main():
    print("This program averages two numbers.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = (num1 + num2) / 2
    print("The average is " + str(total) + ".")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
