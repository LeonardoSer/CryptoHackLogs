#!/usr/bin/env python
from pwn import xor

k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313".decode("hex")
k1_xor_k2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e".decode("hex")
k2_xor_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1".decode("hex")
flag_k1_k2_k3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf".decode("hex")

k2 = xor(k1, k1_xor_k2)
k3 = xor(k2, k2_xor_k3)
flag = xor(xor(xor(flag_k1_k2_k3, k1),k2),k3)

print(flag)
