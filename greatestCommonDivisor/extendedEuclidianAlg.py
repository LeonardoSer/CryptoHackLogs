#!/usr/bin/env python

def gcd_e(a, b):

	if(a < b):
		t = a
		a = b
		b = t
	s = []
	t = []

	s.append(1)
        s.append(0)
       	t.append(0)
        t.append(1)

	while(b != 0):

		q = a/b
		r = a%b
		print("a: " + str(a) + " b:" + str(b) + " q: " + str(q) + " r: "+ str(r))
		tmp_s = s[1]
		tmp_t = t[1]

		s[1] = s[0]-q*s[1]
		t[1] = t[0]-q*t[1]
		print("s: " + str(s[1]) + " t: " + str(t[1]))

		s[0] = tmp_s
		t[0] = tmp_t

		a = b;
		b = r;
	return a

x, y = [int(x) for x in raw_input("Enter two value: ").split(" ")] 
print(gcd_e(x, y))
