# prices = [7, 1, 5, 3, 6, 4]  # expected 5
# prices = [7, 6, 4, 3, 1]  # expected 0
# prices = [1, 2]  # expected 1

prices = [2, 1, 2, 0, 1]  # expected 1
l, r, maxProfit = 0, 1, 0  #left = buy, Right = sell
while (r < len(prices)):
    if prices[r] > prices[l]:
       profit = prices[r] - prices[l]
       maxProfit = profit if profit > maxProfit else maxProfit
    else:
        l = r
    r += 1

print(maxProfit)