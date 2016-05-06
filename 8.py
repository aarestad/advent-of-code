#!/usr/bin/env python

def encoded_length(s):
	total_length = 2 # we get "" for free

	for c in s:
		if c == "\\" or c == '"':
			total_length += 2
		else:
			total_length += 1

	return total_length

total_diff = 0

with open('input_8.txt') as strings:
	for s in strings:
		s = s.strip()
		total_diff += (encoded_length(s) - len(s))

print total_diff
