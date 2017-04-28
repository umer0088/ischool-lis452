# regex_line_separator.py
# J. Weible

# playing with STDIO behaviors

import sys
import argparse
import re

"""This program reads text coming from STDIN, and based on
the regex specified on the command line, it will split that
incoming text two ways.

Lines that match the regex will get sent to STDOUT, and
the lines that don't match will be sent to STDERR
with the assumption they are "erroneous".

When the program is invoked, STDOUT and/or STDERR may be
redirected to capture or discard each as desired.
"""

parser = argparse.ArgumentParser(description='separates stdin lines into stdout & stderr.')
parser.add_argument('regex', type=str,
                   help='a regex, used to match lines for separation')

args = vars(parser.parse_args())

try:
    # Read a line at a time from stdin, and keep going until there is no more
    for line in sys.stdin:

        # if the line matches the regex pattern, then it gets sent to stdout
        if re.search(args['regex'], line):
            sys.stdout.write(line)
        else:
            # No match, so send to stderr
            sys.stderr.write(line)

except KeyboardInterrupt:
    # Catches when we hit Control-C to stop the program when interactive
    exit()
