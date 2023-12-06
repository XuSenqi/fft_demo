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
        #y_times_root = y*domain[i]
        o[i] = (x+domain[i]*y) % modulus
        o[i+n//2] = (x+domain[i+n//2]*y) % modulus
        print("o: ", o)
    return o

coefs=[3,1,4,1,5,9,2,6]
modulus=337
domain=[1, 85, 148, 111, 336, 252, 189, 226]

result = fft(coefs, modulus, domain)
print(result)