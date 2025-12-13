# Each value represents the stock price on a specific day.
# Days move forward from left to right, and once a day passes,
# we cannot go back in time.
# The stock must be bought first and sold on the same or a later day.
# This logic buys at the lowest price and sells at the highest price
# that occurs after the buying day.

weeks = [9, 3, 4, 5, 6, 8, 7]

mini = min(weeks)
index_mini = weeks.index(mini)
mini_start_end = weeks[index_mini:]
max_startFrommini = max(mini_start_end)
buyer = max_startFrommini - mini

print(f"The best profit is {buyer}.")
