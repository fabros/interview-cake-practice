from itertools import islice

def update_max_3(sorted_3, new_num):
	if new_num > sorted_3[0]:
		sorted_3[0] = new_num
	for i in range(1, 3):
		if new_num > sorted_3[i]:
			sorted_3[i-1] = sorted_3[i]
			sorted_3[i] = new_num

def update_min_3(sorted_3, new_num):
	if new_num < sorted_3[-1]:
		sorted_3[-1] = new_num
	for i in range(-2, -4, -1):
		if new_num < sorted_3[i]:
			sorted_3[i+1] = sorted_3[i]
			sorted_3[i] = new_num

def find_max_and_min_3(numbers):
	running_max_3 = sorted(numbers[:3])
	running_min_3 = sorted(numbers[:3])
	for num in islice(numbers, 3, None):
		update_max_3(running_max_3, num)
		update_min_3(running_min_3, num)
	return running_max_3, running_min_3

def max_product_of_3(numbers):
	assert len(numbers) >= 3
	# Official solution is probably more generalizable, but this one I think is more straightforward.
	max_3, min_3 = find_max_and_min_3(numbers)
	max_3_numbers_product = max_3[0] * max_3[1] * max_3[2]
	possibly_negative_numbers_product = min_3[0] * min_3[1] * max_3[2]
	return max(possibly_negative_numbers_product, max_3_numbers_product)

if __name__ == "__main__":
	numbers = list(map(int, input().split(' ')))
	print(max_product_of_3(numbers))