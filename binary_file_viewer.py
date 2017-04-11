# Simple binary file viewer
#
# for LIS452 J. Weible

# This program doesn't "understand" any type of binary format, it
# simply demonstrates opening a file in binary mode, displaying
# selected contents, and closing the file.  It will not modify the
# file.

filename = input('Enter a filename to view in binary mode:')

start_pos = int(input('Enter the byte position where you want to start (must be an integer):'))
length = int(input('Enter the number of bytes to display (must be an integer):'))

# open the file in read-only binary mode:
f = open(filename, mode='rb')

# Starting from the beginning of the file, move the file pointer
# to the desired starting position:
f.seek(start_pos)

# Read (up to) length number of bytes from the file.  If file is shorter
#  than expected, data will be smaller of course.
data = f.read(length)
f.close()  # close the file

if len(data) == 0:
    print("Notice: file is shorter than expected. No data exists after start position.")
    exit()  # quit program

if len(data) < length:
    print("Notice: file only contains", len(data), "bytes from requested start position.\n")

print("File contains:")

# Loop through the data and display the binary content by converting each byte
# into a hexadecimal number:

for i in range(len(data)):
    # start a new line every 32 bytes and show the file position:
    if (i % 32) == 0:
        print('\n{:06x}: '.format(start_pos + i), end='')

    # print one byte as a 2-digit hex number, a space, and stay on the line:
    print('{:02x} '.format(data[i]), end='')

print('\nDone.')
