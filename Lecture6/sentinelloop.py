"""
File: sentinelloop.py
------------------
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

def main():
    total = 0
    num = int(input("Enter a number: "))
    while num != -1:
        total += num
        num = int(input("Enter a number: "))


    print(total)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()


"""
One other way to approach the above problem is to adopt a special word "break" 
as follows;
"""

"""
def main():
    total = 0
    while True:
        num = int(input("Enter a number: "))
        if num == -1:
            break  # Immediately exits the loop
        total += num
        #num = int(input("Enter a number: "))

    print(total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
"""
