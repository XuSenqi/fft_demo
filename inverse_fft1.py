def fft(coefs, modulus, domain):
    #print("coefs", coefs)
    #print("domain", domain)
    if len(coefs) == 1:
        return coefs
    B=coefs[::2]  #even
    C=coefs[1::2] #odd
    L = fft(B, modulus, domain[::2])
    R = fft(C, modulus, domain[::2])

    n=len(domain)
    o = [0 for i in coefs]
    for i, (x, y) in enumerate(zip(L, R)):
        print(i, "(", x, y, ")", "domain[i]:", domain[i])
        print("n:", n)
        y_times_root = y*domain[i]
        o[i] = (x+y_times_root) % modulus
        #o[i+n//2] = (x+domain[i+n//2]*y) % modulus
        o[i+n//2] = (x-y_times_root) % modulus  # because domain[i+n//2] = -domain[i]
        print("o: ", o)
    return o

def ifft(coefs, modulus, inv_domain):
    o=fft(coefs, modulus, inv_domain)
    return [x/len(coefs) for x in o]

# coes=[3,5]
# domain=[1, 336]
# modulus=337
# coefs=[8,335]

#coes=[3,4,5,2]
#modulus=337
#domain=[1, 148, 336, 189]
#inv_domain=[1, 189, 336, 148]
#coefs=[14, 294, 2, 39]

coes=[3,1,4,1,5,9,2,6]
modulus=337
domain=[1, 85, 148, 111, 336, 252, 189, 226]
inv_domain=[1, 226, 189, 252, 336, 111, 148, 85]  # domain[i] * inv_domain[i] % modulus = 1
coefs=[31, 70, 109, 74, 334, 181, 232, 4]

result = fft(coes, modulus, domain)
print(result)

result = ifft(coefs, modulus, inv_domain)
print(result)