#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.

largest = None
smallest = None
while True:
    num = input("Enter an integer. Enter \"done\" when finished.")
    if num == "done":
        break
    try:
        num = int(num)
        if largest is None and smallest is None:
            largest = num
            smallest = num
        elif num > largest:
            largest = num
        elif num < smallest:
            smallest = num
        else:
            True
    except:
        print("Invalid input")
        True

print("Maximum is", largest)
print("Minimum is", smallest)