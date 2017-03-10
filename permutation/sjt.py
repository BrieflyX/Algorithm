#!/usr/bin/env python
# coding: utf-8

# data structure : [[number, direction],...]
# direction is 1 or -1

def convert(state):
	''' convert data structure to flat list of number '''
	return map(lambda x:x[0], state)

def next_permut(state):

	# find largest mobile integer m
	idx = -1
	m = False
	for i in range(len(state)):
		j = state[i][1] + i
		if j >= 0 and j < len(state) and state[i][0] > state[j][0] and state[i][0] > m:
			idx = i
			m = state[idx][0]

	if m == False:
		return False
	# swap number, change direction
	j = state[idx][1] + idx
	state[j], state[idx] = state[idx], state[j]

	for i in range(len(state)):
		if state[i][0] > m:
			state[i][1] *= -1

	return state

def test():
	init = [[x, -1] for x in range(1, 5)]

	for i in range(10):
		print(init)
		init = next_permut(init)

if __name__ == '__main__':
	test()