# convert.py
#   A program to convert Celsius temps to Fahrenheit
#
# J. Weible, based on example from John Zelle's 2nd edition Python textbook.

def main():
    """Interactive converter of temperatures."""
    times_to_loop = False
    while times_to_loop == False:
        try:
            times_to_loop = int(input("How many temperatures do you want to convert?"))
        except ValueError:
            print("Retry, by entering an integer number.")
            times_to_loop = False

    for i in range(times_to_loop):
        celsius = int(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

