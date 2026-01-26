# You’ve just received a bonus and decided to spend it all on chocolate bars. 
# Each bar costs a certain price, and for every m wrappers you collect,
# the shop gives you 1 free chocolate bar.

def choco_feast(money, price, wrapper_rate):
    if money < price:
        return 0
    chocolates = money // price
    wrappers = chocolates
    while wrappers >= wrapper_rate:
        new_chocolates = wrappers // wrapper_rate
        chocolates += new_chocolates
        wrappers = wrappers % wrapper_rate + new_chocolates
    return chocolates

#You’re working at a small cinema 🎬. Every ticket costs price. On movie night, you want to know
# how many people can watch a movie if you only have a certain budget.
# But here’s the twist:

# Every third person gets a free ticket (loyalty reward).

# You still need to seat them in order (you can’t just pick and choose who’s free).

# Write a function cinema_night(budget, price) that returns the maximum number of people who can watch the movie. 
def cinema_night(budget, price):
    if budget < price:
        return 0
    tickets = 0
    while budget >= price:
        tickets += 1
        budget -= price
        if tickets % 3 == 0:
            budget += price  # Every third ticket is free
    return tickets

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, there is no common prefix
        if not strs:
            return ""

        # Start by assuming the first string is the common prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for word in strs[1:]:
            # Reduce prefix until it matches the start of the word
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                if prefix == "":
                    return ""

        return prefix
