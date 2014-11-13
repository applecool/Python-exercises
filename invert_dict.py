def frequency(string):
	d = dict()
	for char in string:
		d[char] = 1 + d.get(char,0)
	return d


def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

input = raw_input('Enter a string to find the frequency of each character:\n')

h = frequency(input)

print h

inverse = invert_dict(h)

print inverse