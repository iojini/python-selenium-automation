#Problem 1: Exclamation marks series #2: Remove all exclamation marks from the end of sentence
#Description: Remove all exclamation marks from the end of sentence.

def remove(st):
    for i in range(len(st)-1, -1, -1):
        if st[i] != "!":
            return st[0:i+1]

#Problem 2: Regex count lowercase letters
#Description: Your task is simply to count the total number of lowercase letters in a string.

def lowercase_count(strng):
    count = 0
    for char in strng:
        if char.isalpha and char.islower():
            count += 1
    return count

#Problem 3: Check same case
#Description: Write a function that will check if two given characters are the same case.
#If either of the characters is not a letter, return -1
#If both characters are the same case, return 1
#If both characters are letters, but not the same case, return 0

def same_case(a, b):
    if not a.isalpha():
        return -1
    elif not b.isalpha():
        return -1
    elif a.islower() == b.islower():
        return 1
    elif a.isupper() == b.isupper():
        return 1
    return 0