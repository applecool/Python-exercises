# Write a function that reads the words in words.txt and stores
# them as keys in a dictionary. It doesn't matter what the values
# are.
# 
# I used the python's in-built function random to generate random values
# One can use uuid to generate random strings which can also be used to 
# pair the keys i.e., in this case the words in the .txt file

import random

output = dict() #creates an empty dictionary

words = open('words.txt') 

line = words.readline() 

def key_value():
	for line in words:
		word = line.strip() 
		output[word] = random.random() 

	return output

print key_value()

