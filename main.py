# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = input("Enter your word choice: ")
anagram = input("Enter your anagram answer: ")


def find_anagram(word, anagram):
    # [assignment] Add your code here

    # Removing of spaces
    string_1 = word.replace(" ", "").lower()
    string_2 = anagram.replace(" ", "").lower()

# **print(sorted(string_1) == sorted(string_2))** #

# Dict to store data values
    hold_words = {}

# checking if the lengths are equal after removing spaces.
    if len(string_1) == len(string_2):

        # verifying in the first word
        for check in string_1:
            if check in hold_words:
                hold_words[check] += 1
            else:
                hold_words[check] = 1

# verifying in the anagram answer
        for check in string_2:
            if check in hold_words:
                hold_words[check] -= 1
            else:
                hold_words[check] = 1

# checking if there is any word left/remaining
        for check in hold_words:
            if hold_words[check] != 0:
                return False
        return True

    else:
        # if the lengths are unequal
        return False


print(find_anagram(word, anagram))
