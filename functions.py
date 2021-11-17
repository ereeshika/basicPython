# Python function is defined using def keyword.
def my_function():
    print("Hello from a function")


# Calling a function.
my_function()

year = int(input("Enter a year: "))


def LeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


LeapYear(year)
