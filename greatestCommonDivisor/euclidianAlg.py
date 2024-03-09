#!/usr/bin/env python

def gcd(a, b):
	while b!=0:
		t=b
		b = a%b
		a = t
	return a

print(gcd(66528,52920))
