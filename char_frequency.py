def frequency(string):
	d = dict()
	for char in string:
		#if char not in d: #alternative method with "if"
		#	d[char] = 1
		#else:
		#	d[char] +=1
		d[char] = 1 + d.get(char,0)

	return d 

input = raw_input('Enter a string to find the frequency of each character:\n')
print frequency(input) 