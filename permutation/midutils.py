# coding: utf-8

MAXN = 8

def mid2str(mid):
	return ''.join(str(x) for x in mid).rstrip('0')[::-1]

def str2mid(str):
	mid = [int(x) for x in str][::-1]
	if len(mid) < MAXN:
		mid.extend([0] * (MAXN-len(mid)))
	return mid