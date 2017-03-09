# convert.py
#   A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():

    times_to_loop = int(input("How many temperatures do you want to convert?"))
    for i in range(times_to_loop):
        celsius = int(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()

