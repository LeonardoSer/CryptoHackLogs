#!/usr/bin/env python


from pwn import * # pip install pwntools
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
import json


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for x in range(200):
	print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaoh"+str(x))
	received = json_recv()

	if received["type"] == "base64":

		decoded = base64.b64decode(received["encoded"])

	elif received["type"] == "hex":

		decoded = received["encoded"].decode("hex")

	elif received["type"] == "rot13":

		decoded = codecs.decode(received["encoded"],'rot_13')

	elif received["type"] == "bigint":

		arrHex = []
		decoded = ""
		i = 2
		while i < (len(received["encoded"])-1):
		        arrHex.append(received["encoded"][i]+received["encoded"][i+1])
		        i += 2
		for j in arrHex:
		        decoded+=chr(int(j, 16))

	elif received["type"] == "utf-8":

		decoded = ""
		for i in received["encoded"]:
		        decoded += chr(i)

	to_send = { "decoded" : decoded }

	json_send(to_send)


