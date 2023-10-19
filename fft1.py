def fft(vals, modulus, domain):
    #print("vals", vals)
    #print("domain", domain)
    if len(vals) == 1:
        return vals
    B=vals[::2]  #even
    C=vals[1::2] #odd
    L = fft(B, modulus, domain[::2])
    R = fft(C, modulus, domain[::2])

    k=len(domain)
    o = [0 for i in vals]
    for i, (x, y) in enumerate(zip(L, R)):
        #print(i, "(", x, y, ")", "domain[i]:", domain[i])
        y_times_root = y*domain[i]
        o[i] = (x+domain[i]*y) % modulus
        o[i+k/2] = (x+domain[i+k/2]*y) % modulus
        #print("o: ", o)
    return o

vals=[3,1,4,1,5,9,2,6]
modulus=337
domain=[1, 85, 148, 111, 336, 252, 189, 226]

result = fft(vals, modulus, domain)
print(result)