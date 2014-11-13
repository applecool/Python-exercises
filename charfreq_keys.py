def frequency(string):
	d = dict()
	for char in string:
		d[char] = 1 + d.get(char,0)

	return d 

def print_freq(f):
	result_keys = f.keys()
	result_keys.sort()
	for char in result_keys:
		print char, f[char]

input = raw_input('Enter a string to find the frequency of each character:\n')

x = frequency(input) 

print_freq(x)
