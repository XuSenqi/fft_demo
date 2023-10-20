# -*- coding: utf-8 -*-

def fft(coes, modulus, domain):
    #print("coes", coes)
    #print("domain", domain)
    if len(coes) == 1:
        return coes
    L = fft(coes[::2], modulus, domain[::2])
    R = fft(coes[1::2], modulus, domain[::2])

    k=len(domain)
    o = [0 for i in coes]
    for i, (x, y) in enumerate(zip(L, R)):
        #print(i, "(", x, y, ")", "domain[i]:", domain[i])
        y_times_root = y*domain[i]
        o[i] = (x+y_times_root) % modulus
        #o[i+k/2] = (x+domain[i+k/2]*y) % modulus
        o[i+k/2] = (x-y_times_root) % modulus # because domain[i+k/2] = -1
        #print("o: ", o)
    return o

def modular_inverse(x, n):
    return pow(x, n - 2, n)

# vitalik实现的ifft，原理不清楚
# https://vitalik.ca/general/2019/05/12/fft.html
def inverse_fft(vals, modulus, domain):
    vals = fft(vals, modulus, domain)
    return [x * modular_inverse(len(vals), modulus) % modulus for x in [vals[0]] + vals[1:][::-1]]

# coes=[3,5]
# domain=[1, 336]
# modulus=337
# vals=[8,335]

#coes=[3,4,5,2]
#modulus=337
#domain=[1, 148, 336, 189]
#inv_domain=[1, 189, 336, 148]
#vals=[14, 294, 2, 39]

coes=[3,1,4,1,5,9,2,6]
modulus=337
domain=[1, 85, 148, 111, 336, 252, 189, 226]
inv_domain=[1, 226, 189, 252, 336, 111, 148, 85]
vals=[31, 70, 109, 74, 334, 181, 232, 4]

result = fft(coes, modulus, domain)
print(result)

result = inverse_fft(vals, modulus, domain)
print(result)