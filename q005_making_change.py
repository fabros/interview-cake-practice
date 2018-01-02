def ways_to_make_change(amount, denominations):
	# DP bottom-up solution
	ways_to_make_change_for = [0] * (amount + 1)
	ways_to_make_change_for[0] = 1  # instrumental for later increases

	for coin in denominations:
		for current_amount in range(coin, amount+1):
			ways_to_make_change_for[current_amount] += ways_to_make_change_for[current_amount - coin]
	return ways_to_make_change_for[amount]


if __name__ == "__main__":
	amount = int(input())
	denominations = list(map(int, input().split(' ')))
	print(ways_to_make_change(amount, denominations))