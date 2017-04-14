# Used to read and process a data file for an assignment on binary file processing
#
# J. Weible

# The input data file is structured as binary data with variable-length records, as:

# The file (and every subsequent record) begins with:
#  a 2-byte integer (little-endian) indicating the number of data values (not bytes)
#                        in the record.
#  a 1-byte code indicating the record type and sensor unit number.
#     rec.type is the Most-significant bit: [0 = test data, 1 = production run data]
#     The remainder is the sensor unit number.
#  1 byte, currently unused. (Keeps the byte offsets aligned evenly.)
#  the raw data, stored as 2-byte words (little-endian)

from struct import unpack
import io

filename = input('Enter the input data filename: ')
bytes_per_value = 2

f = open(filename, 'rb')

record_count = 0

f.seek(0, io.SEEK_END)  # Jump to the end of the file
end_of_file_position = f.tell()  # Get file pointer position
print('File size is', end_of_file_position, 'bytes.')
f.seek(0, io.SEEK_SET)  # Return pointer to the beginning of the file

while f.tell() < end_of_file_position:
    record_count += 1

    # Unpacking binary data can be tricky...
    # Read 2 bytes from the file
    # "Unpack" the bytes as little-endian 2-byte integer(s) [sic].
    # Get the first result from tuple (there should be only one value in this case)
    record_length = unpack('<H', f.read(2))[0]

    print('record', record_count, 'has', record_length, 'values, or', record_length * bytes_per_value, 'bytes.')
    f.seek(2 + record_length * bytes_per_value, io.SEEK_CUR)  # Scan forward to start of next record

f.close()
print('Done processing.')
