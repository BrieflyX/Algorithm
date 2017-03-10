#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, division
from math import factorial
from midutils import *

def dec2mid(num, n=MAXN):
	''' convert the decimal number to decreased mid number '''
	mid = []
	for i in range(n+1, 0, -1):
		mid.append(num % i)
		num = num // i
	return mid

if __name__ == '__main__':
	print(mid2str(dec2mid(2015, 7)))
