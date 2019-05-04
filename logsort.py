"""
This utility allows you to create a new .txt file from a log file containing
ONLY the lines which contain the key phrase defined by the user.
Each line from the log file is read, split, and stored in a list,
passed to a linear search function which searches for the key phrase in the 
list and if the condition is met, the line is written back to the log file 
in the initial format which is was read as.

NOTES:
- Files created and read from same directory as logsort.py
- Word split is the character in your log which separates each word. For
  example if my line is "Hello World" a space (" ") would be my word split.
  
Author: Joshua Reisbord
Date: Feb 2, 2019.
"""
import sys
import time

def file_to_list(file, split, phrase):
    """
    :param file:  File which will be turned into a list of lists
    :param split: What defines a new block of data in each line
    :param phrase: Phrase to look for in each line.
    :return: New log file.
    """
    count = 0
    outfile = open('sorted_log.txt', 'w+')  # Creates a new file
    time_start = time.time()

    with open(file) as data:
        for line in data:  # For each line in 'file'
            data_list = [str(do.strip()) for do in line.split(split)]
            # Split elements at ',' and strip trailing new line
            if phrase in data_list:  # Checks for key phrase
                count += 1
                sys.stdout.write("\r" + "Found the phrase: '" + phrase + "' " + str(count) + " times.")
                sys.stdout.flush()
                outfile.write(" ".join(data_list) + '\n')  # Writes to file.

    print("\nTook ", round(time.time() - time_start, 2), "to complete.")


def main():

    """Program execution starts here."""

    print(__doc__)

    while True:

        try:

            log = input(str('Log file: '))
            word = input(str('Search phrase: '))
            split = input(str('Word split: '))
            file_to_list(log, split, word)  # Turns log too list of lists
            print('\nAll data has been outputted to sorted_log.txt')

        except FileNotFoundError:

            print('\nERROR: Log file not found, try again!')
            pass


if __name__ == '__main__':
    main()
