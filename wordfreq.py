# wordfreq.py
#
# Based on John Zelle's example from PPICS 2nd ed. Page 375.
#
# Slightly modified by J. Weible

from collections import defaultdict

def byFreq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    fname = input("File to analyze: ")
    text = open(fname,'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, ' ')
    words = text.split()

    # construct a dictionary of word counts
    counts = defaultdict(int)  # dict where non-existent keys get automatically assigned an integer 0
    for w in words:
        counts[w] += 1

    # output analysis of n most frequent words.
    n = eval(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))

# This "magic" line below will allow this file to be imported by another script
# without automatically executing the functions contained in it:
if __name__ == '__main__':  main()
