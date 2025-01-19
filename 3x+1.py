def threexplus1 (n):
	count = 1
	while n != 1:
			if n % 2 == 0:
					n = n // 2
			else:
					n = 3 * n + 1
			count += 1
	return count

def find_starting_number(limit):
	max_length = 0
	starting_number = 0

	for i in range(1, limit):
			length = threexplus1(i)
			if length > max_length:
					max_length = length
					starting_number = i

	return starting_number, max_length

# Set the limit to a reasonable range
limit = 10
starting_number, max_length = find_starting_number(limit)

print(f"The starting number with the longest sequence up to cycle 421 is {starting_number} with a sequence length of {max_length}.")
