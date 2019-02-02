"""
This utility allows you to create a new .txt file from a log file containing
ONLY the lines which contain the key phrase defined by the user.

NOTES:
- Files created and read from same directory as logsort.py

- Word Split is the character in your log which separates each word. For
  example if my line is "Hello World" a space would be my word split.

Author: J. Reisbord
Date: Feb 2, 2019.
"""


def file_to_list(file, split):

    converted_data = []

    with open(file) as data:

        for line in data:  # For each line in 'file'
            data_list = [str(do.strip()) for do in line.split(split)]
            # Split elements at ',' and strip trailing new line
            converted_data.append(data_list)  # Appended data to converted_data

        return converted_data  # Returns converted data.


def write_by_phrase(converted_log, phrase):

    outfile = open('sorted_log.txt', 'w+')  # Creates a new file

    for element in converted_log:  # Loops for all lines in converted_log
        if phrase in element:  # Checks for key phrase
            outfile.write(" ".join(element) + '\n')  # Writes too file.


def main():

    """Program execution starts here."""


print(__doc__)
log = input(str('Log file: '))
word = input(str('Word: '))
split = input(str('Word Split: '))
con_log = (file_to_list(log, split))
write_by_phrase(con_log, word)
print('All data has been outputted to sorted_log.txt')

main()
