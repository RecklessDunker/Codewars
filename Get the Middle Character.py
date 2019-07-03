# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Wednesday, 3rd July 2019
# Version: 1.0
# --------------------------------------------------------
#
# You are going to be given a word. Your job is to return the middle character of the
# word. If the word's length is odd, return the middle character. If the word's length
# is even, return the middle 2 characters.

def get_middle(s):
    # your code here
    wordlen = len(s)
    if wordlen % 2 == 0:
        # is even, so find middle two characters
        middlechar = s[len(s) // 2 - 1] + s[len(s) // 2]

    else:
        # is odd, so find the middle letter
        middlechar = s[len(s) // 2]

    return middlechar


midchar = get_middle(input("Please type in a word: "))
print(midchar)

