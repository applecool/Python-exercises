#Implementation of fibonacci using memos

known = {0:0,1:1} #dictionary that keeps track of fibonacci numbers we already know

def fibonacci(n):
	if n in known:
		return known[n] #if the result is already there, it returns immediately

	result = fibonacci(n-1) + fibonacci(n-2) #computes the new value
	known[n] = result #adds the above result to the dictionary
	return result

input = raw_input('Enter a number:') #prompts for the user input
print fibonacci(int(input))