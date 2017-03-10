#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, division
from math import factorial
from midutils import *

def dec2mid(num, n=MAXN):
	''' convert the decimal number to increased mid number '''
	mid = []
	for i in range(n, 0, -1):
		mid.insert(0, num // factorial(i))
		num = num % factorial(i)
	return mid

def mid_add(mid1, mid2):
	''' 递增进位制数加法 '''
	S = mid1
	c = 0
	for i in range(len(S)):
		S[i] += mid2[i] + c
		c = 0
		if S[i] >= i + 2:
			S[i] -= i + 2
			c = 1
	return S

def mid_sub(mid1, mid2):
	''' 递增进位制减法 '''
	A = mid1
	B = mid2
	for i in range(len(A)):
		if A[i] >= B[i]:
			A[i] -= B[i]
		else:
			A[i] = A[i] + i + 2 - B[i]
			for j in range(i+1, len(A)):
				if A[j] > 0:
					A[j] -= 1
					break
				else:
					A[j] = j + 1
	return A

def test():
	print(mid2str([1,2,3,2,4,6,2,7]))
	print(mid2str([0,2,0,4,0,0,0,0]))
	print(str2mid('72642321'))
	print(str2mid('4020'))
	print(mid2str(dec2mid(279905)))
	print(mid_sub([1,2,3,2,4,6,2,7], [0,2,0,4,0,0,0,0]))
	print(mid_add([1,2,3,2,4,6,2,7], [0,2,0,4,0,0,0,0]))
	print(mid2str(mid_sub(str2mid('7244221'), str2mid('243321'))))
	print(mid2str(mid_sub(str2mid('7442221'), str2mid('243321'))))

if __name__ == '__main__':
	test()