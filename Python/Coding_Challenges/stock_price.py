# Imagine you have a list of integers representing stock prices on different days. 
# Write a function that takes this list as input and returns the maximum profit 
# that can be made by buying and selling the stock once. If no profit can be made, return 0. 
# Please consider efficiency and edge cases in your solution.
# Here's an example to consider:
# Given the list [7, 2, 5, 3, 6, 4, 1], what would be the maximum profit that can be made? 
# Explain your approach and provide the code implementation without using any inbuilt methods.


list1 = [7, 2, 5, 3, 6, 4, 1]

init = list1[0]
rs = 0
profit = 0

for i in range(1, len(list1)):
    if list1[i] - init > rs:
        rs = list1[i] - init
        init = list1[i]



print(rs)    

def max_profit_1(prices):
    if len(prices) < 2:
        return 0  # Cannot make a profit with fewer than 2 prices

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # Update max_profit if selling at the current price yields a higher profit
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

        # Update min_price if the current price is lower
        if price < min_price:
            min_price = price

    return max_profit


print(max_profit_1(list1))


def max_profit_2(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit




print(max_profit_2(list1))
















  
  
  
  
  
  
  
    




