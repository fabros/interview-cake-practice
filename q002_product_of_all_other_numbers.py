def product_of_all_other_numbers(numbers):
	# optimized version (underlying idea remains the same:
	# compute left partial, compute right partial, multiply partials)
	assert len(numbers) > 1
	product_of_all_numbers_except_at_index = [1] * len(numbers)
	running_left_product = running_right_product = 1

	for i in range(len(numbers)):
		product_of_all_numbers_except_at_index[i] *= running_left_product
		product_of_all_numbers_except_at_index[len(numbers) - i - 1] *= running_right_product

		running_left_product *= numbers[i]
		running_right_product *= numbers[len(numbers) - i - 1]

	return product_of_all_numbers_except_at_index

if __name__ == "__main__":
	numbers = list(map(int, input().split(' ')))
	print(' '.join(map(str, product_of_all_other_numbers(numbers))))