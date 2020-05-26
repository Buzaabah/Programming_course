"""
File: constants.py
------------------
An example program with constants.  Converts feet
to total number of inches.
The idea for constants is for programing style to avoid magic number and when it comes to change the constant in the
program, you only change once the constant.
Its always advisable to put all constants before the function.
"""

# It usually looks nice representing constants with capital snake case. for readability

# pie value
PI = 3.1415
# Number of inches in a foot
INCHES_IN_FOOT = 12

def main():
    feet = float(input("Enter number of feet: "))
    inches = feet * INCHES_IN_FOOT
    print("That is " + str(inches) + " inches!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()