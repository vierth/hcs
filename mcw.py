'''
This script will identify the most common character in a string
'''

my_paragraph = "This eBook is fiiiiiiiiiiiiiiiiiiiiiiiiiiior the use of anyone anywhere in the United States and most other parts of the world at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org.  If you are not located in the United States, you'll have to check the laws of the country where you are located before using this ebook."

my_word_list = my_paragraph.split(" ")

unique_chars = set(my_word_list)

# create a variable to the most common character
most_common = []

# variable contain how often that character occurs
most_common_freq = 0

frequencies = {}

for char in unique_chars:
    if char.isalnum():
        freq = my_paragraph.count(char)

        if freq > most_common_freq:
            most_common = [char]
            most_common_freq = freq
        elif freq == most_common_freq:
            most_common.append(char)

print(f"The most common character is {most_common}, which occurs {most_common_freq} times.")









