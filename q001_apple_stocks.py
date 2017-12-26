import math

def get_max_profit(stock_prices):
	assert len(stock_prices) >= 2
	running_min_price = stock_prices[0]
	running_max_profit = -math.inf

	for price in stock_prices[1:]:
		profit = price - running_min_price
		if profit > running_max_profit:
			running_max_profit = profit

		if price < running_min_price:
			running_min_price = price

	return running_max_profit


if __name__ == "__main__":
	stock_prices = list(map(int, input().split(' ')))
	print(get_max_profit(stock_prices))