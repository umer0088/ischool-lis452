# convert.py
#   A program to convert Celsius temps to Fahrenheit
#
# J. Weible, based on example from John Zelle's 2nd edition Python textbook.

def main():
    """Interactive converter of temperatures."""
    while how_many_temps == False:
        try:
            how_many_temps = int(input("How many temperatures do you want to convert?"))
        except ValueError:
            how_many_temps = False

    for i in range(how_many_temps):
        celsius = int(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # This is just an extra comment I've added

main()

