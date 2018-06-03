#!/usr/bin/env python3

import string

plaintext = open("in/bis.txt", "rb").read()
ciphertext = open("in/bis.txt.enc", "rb").read()
xor = [x ^ y for x, y in zip(plaintext, ciphertext)]

N_B = 32
N = N_B * 8

SUB = [0, 1, 1, 0, 1, 0, 1, 0] # original register
UNSUB = ([0, 3, 5, 7], [1, 2, 4, 6]) # possibilities register

def step_forward(x): # keystream function for encryption
    x = (x & 1) << N+1 | x << 1 | x >> N-1 
    y = 0
    for i in range(N):
        y |= SUB[(x >> i) & 7] << i

    return y

def step_back_x(x): # undo x modification
    return  (x >> 1) & ((1 << N) - 1)

def step_back(y): # generate possible inputs x for output y
    prev = UNSUB[y & 1]

    for i in range(1, N):
        next = []
        bit = (y >> i) & 1
        possibilities = UNSUB[bit]

        for p in possibilities:
            for item in prev:
                if p & 3 == item >> i:
                    next.append(item | p << i)
        
        prev = next

    return [step_back_x(x) for x in next]

keystream = int.from_bytes(xor[:32], 'little')

for i in range(N//2):
    for res in step_back(keystream):
        if step_forward(res) == keystream:
            keystream = res
            break
    
res = keystream.to_bytes(N_B, 'little')
key = "".join([chr(c) for c in res if chr(c) in string.printable])
print(key)
