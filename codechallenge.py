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