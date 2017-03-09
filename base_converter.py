# base_converter.py
# A program for converting integer numbers to and from different bases
# J. Weible  LIS452 example

# Requires use of int() function with base parameter.
# Requires use of string.format() method and format specifications. Chapter 5 in PPICS is related

while True:
    print('\nYour options: Quit, Binary, Decimal, Hexadecimal')
    command = input('Type the first letter of your choice and press Enter.')
    command = command[0]
    
    if command in ['q','Q','']:
        break  # exit the loop, which will quit the program

    if command in ['b','B']:
        mode = 'binary'
        base = 2
    elif command in ['d','D']:
        mode = 'decimal'
        base = 10
    elif command in ['h','H']:
        mode = 'hexadecimal'
        base = 16
    else:
        print('unrecognized option!')
        continue  # continue restarts at the top of the loop.
    
    number_text = input('Type the ' + mode + ' integer number to convert:')

    n = int(number_text, base)  # convert text into an integer, with a specific base (base defaults to decimal)

    print('in binary      {0:b}'.format(n))   # uses string format() function to display n as binary
    print('in decimal     {0:d}'.format(n))   # uses string format() function to display n as decimal (which isn't necessary)
    print('in hexadecimal {0:x}'.format(n))   # uses string format() function to display n as hexadecimal

print('all done now, bye!')
