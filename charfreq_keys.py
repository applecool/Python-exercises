#Implement the keys method of dictionaries. 
#Write a function which takes the output of the 
#frequency function and prints the keys and their 
#values in alphabetical order

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
