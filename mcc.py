'''
This script will identify the most common character in a string
'''

my_paragraph = "This eBook is for the use of anyone anywhere in the United States and most other parts of the world at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org.  If you are not located in the United States, you'll have to check the laws of the country where you are located before using this ebook."

# create a variable to the most common character
most_common = None

# variable contain how often that character occurs
most_common_freq = 0

for char in my_paragraph:
    if char != " ":
        freq = my_paragraph.count(char)

        if freq > most_common_freq:
            most_common = char
            most_common_freq = freq

print(f"The most common character is {most_common}, which occurs {most_common_freq} times.")









