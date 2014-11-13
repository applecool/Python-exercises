import random

output = dict() #creates an empty dictionary

words = open('words.txt') 

line = words.readline() 

def key_value():
	for line in words:
		word = line.strip() 
		output[word] = random.random() #assigning each word value to a random number key

	return output

print key_value()

