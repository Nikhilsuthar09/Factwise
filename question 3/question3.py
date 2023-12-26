def maxProfit(prices):
  if not prices or len(prices)<2:
    return 0
  minPrice = prices[0]
  maxProfit = 0
  for price in prices[1:]:
    if price < minPrice:
      minPrice = price
    else:
      maxProfit = max(maxProfit, price - minPrice)
  return maxProfit

prices = [7,6,4,3,1]
result = maxProfit(prices)
print(result)
