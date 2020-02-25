'''
This script will break apart the 四庫全書總目提要 into a structured dataset
'''

import re

# We will start by designing our regular expressions and then run through the
# logic of the program

'''
This text was originally divided into pages on zh.wikisource.org.
An average page starts with something like this, which contains information on 
the Siku categorization and the sub-class:
卷二 經部二
---------------

==易類二==

We want to extract "經" and "易"
'''
# this regex matches that pattern
sikuregex = re.compile(r"""
    卷     # match 'scroll' (juan)
    [一二三四五六七八九十百零]+     # match numbers
    \s?    # optionally match whitespace
    ([經史子集]) # Match Siku Categories (and capture value)
    部     # Match 'category' (bu)
    [一二三四五六七八九十百零]+     # match numbers
    """, 
    # run this with the Verbose flag to allow multi-line regex
    re.X)

'''
Information on the sub-category follows these patterns:
==春秋類二==
or
○孝經類 (sometimes followed by extra things, but we can ignore those)
'''
subcat_regex = re.compile(r'''
    ^ # beginning of the line
    (?:
    ==
    (.+)
    類
    [一二三四五六七八九十百零]+
    ==
    )
    |
    (?:
    ○
    (.+)
    類
    )
    ''', re.X|re.M)

'''
Bibliographic information tends to look like this (but there are multiple 
variations that we should account for):

==《[[東坡易傳]]》•九卷{{*|副都御史黃登賢家藏本}}==

宋蘇軾撰。是書一名《毗陵易傳》。陸遊《老學庵筆記》謂其書初遭元祐黨禁，不敢顯題軾名...

The format is like this:
==《[[Title]]》•Length卷{{*|Edition}}==

Book Information
'''
# This regex retrieves this bibliographic information
book_regex = re.compile(r"""
    ^  # All book titles match at the start of line

    # Titles start with == or △
    # parentheses allow me to control phrases within regex
    (?: # start group, '?:' means don't capture as we don't need to return this
    ==  # match ==
    |   # or
    △   # △
    )   # close group
    

    《  # open title quote
    (.+?)   # match all values, this will be the title (and capture it)
    》  # close title quote

    # The title is usually ofset from the length by a space or a circle
    [\s•]?  #optionally match a space or a circle

    # Most works mention how many scrolls they contain, but not all do
    (?:     # open a non-capture group
    ([一二三四五六七八九十百零]+) # match numbers (and capture them)
    卷      # match scroll (or juan)
    )?      # close the group, make it optional

    # Sometimes further information is in curly brackets here
    (?:     # open a non-capture group
    \{\{    # match {{
    \*      # match *
    \|      # match |
    (.+?)   # match the contents in the brackets (and capture)
    \}\}    # match }}
    )?      # close the group, make it optional

    # Title level information closes with == in most cases
    ={2}?  # close title level information

    # In some cases, more information is provided on the next line
    (?:     # open a non-capture group
    \n      # match the new line 
    (.+)    # followed by some data (and capture it)
    )?      # close the group, make it optional

    # The book descriptions appear after two new line characters
    \n{2}   # match \n twice
    (.+)    # get book description (and capture it). will need more processing
    """, 
    # re.X flag for verbose, re.M for multiline (enabling ^ for start of line)
    re.X|re.M) 

'''
The bibliographic information for each title also contains information on the 
people associated with the text (author most commonly) and when they were alive

These are in the format
[Dynasty][Person][Relationship to Text]
and records usually open with them
'''
role_regex = re.compile(r'''
    ^ # beginning of the line
    (.+?) # information on the person
    ([撰編纂選輯注述])  # by (zhuan)/ edited (bian)/ compiled (zuan) / selected (xuan) / edited (ji) / annotated (zhu) / narrated by (shu)
    ''', re.X|re.M)

# Let's set up some containers for the data we are working with
data = []

# now that we have our regular expressions, we can extract the data
# load the text
with open("四庫全書總目提要.txt", 'r', encoding='utf8') as rf:
    text = rf.read()

# divide the text. The first page doesn't have any book info on it, nor do the
# the last five pages, so we can discard those
pages = text.split("~~~NEXT~~~")[1:-5]

# The first page does not contain easy to parse meta information, so we can 
# initialize it by hand
current_siku = "經"
current_subcat = "易"

# Iterate through all pages and extract the information
for page in pages:
    
    # use the siku regular expression to get siku information
    siku_info = sikuregex.search(page)
    
    # if there are any results, update the current meta information
    if siku_info:
        # the first capture group is the siku classification
        current_siku = siku_info.group(1)
    
    # use the subcat regex to get the subcat information
    subcat_info = subcat_regex.search(page)
    if subcat_info:
        if subcat_info.group(1):
            current_subcat = subcat_info.group(1)
        else:
            current_subcat = subcat_info.group(2)

    # use the book regular expression to find all of the book entries
    info_on_books = book_regex.finditer(page)
    
    # iterate through all of the results
    for book_info in info_on_books:
        # if there is a result, extract the relevant information
        if book_info:

            # the first group holds the title
            title = book_info.group(1)

            # let's replace the [[]] in all the titles
            title = title.replace("[", "").replace("]", "")

            # the second group has the length
            length = book_info.group(2)
            # if no length was found, provide an empty string
            if not length:
                length = ""

            # any information in the {{}} is the third group and supplemental
            # info is in the fourth group. Let's check if they exist and 
            # combine them (str uses to convert None to string, which is then)
            # replaced
            supplemental_info = str(book_info.group(3)) + str(book_info.group(4))
            supplemental_info = supplemental_info.replace("None", '')

            # the bulk of the book information is in group 5
            book_description = book_info.group(5)

            # Once we have the book description, we can get info on people
            person_info = role_regex.search(book_description)
            
            # save the person information if found
            if person_info:
                # the person is in group 1
                person = person_info.group(1)
                # their role is in group 2
                role = person_info.group(2)
            # we also need to save variables if no info is found
            else:
                person = ""
                role = ""
            
            # Put the data into a list
            temp_info = [title, current_siku, current_subcat, length, person, role, supplemental_info, book_description]
            # Turn the data into a comma seperated value string
            temp_string = ",".join(temp_info)
            # add the string to the data list
            data.append(temp_string)

# Join the data into a string that we can write to file
data_string = "\n".join(data)

# write the results to file:
with open("catalog.csv", 'w', encoding='utf8') as wf:
    # Write a header:
    wf.write("Title,Siku,SubCat,Length,Person,Role,Supp,BookInfo\n")
    # write the data
    wf.write(data_string)