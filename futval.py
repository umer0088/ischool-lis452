# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future
#
# from Page 48-49 of PPICS 2nd edition.

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate. Enter a 3% rate as 0.03: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in 10 years is:", principal)

main()          
