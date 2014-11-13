known = {0:0,1:1}

def fibonacci(n):
	if n in known:
		return known[n]

	result = fibonacci(n-1) + fibonacci(n-2)
	known[n] = result
	return result

input = raw_input('Enter a number:')
print fibonacci(int(input))