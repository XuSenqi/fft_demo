# def fft(vals, modulus, domain):
#     #print("vals", vals)
#     #print("domain", domain)
#     if len(vals) == 1:
#         return vals
#     L = fft(vals[::2], modulus, domain[::2])
#     R = fft(vals[1::2], modulus, domain[::2])

#     k=len(domain)
#     o = [0 for i in vals]
#     for i, (x, y) in enumerate(zip(L, R)):
#         #print(i, "(", x, y, ")", "domain[i]:", domain[i])
#         y_times_root = y*domain[i]
#         o[i] = (x+y_times_root) % modulus
#         #o[i+k/2] = (x+domain[i+k/2]*y) % modulus
#         o[i+k/2] = (x-y_times_root) % modulus  # because domain[i+k/2] = -1
#         #print("o: ", o)
#     return o

# vals=[3,1,4,1,5,9,2,6]
# modulus=337
# domain=[1, 85, 148, 111, 336, 252, 189, 226]

# result = fft(vals, modulus, domain)
# print(result)

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

coefs=[3,1,4,1,5,9,2,6]
modulus=337
domain=[1, 85, 148, 111, 336, 252, 189, 226]

result = fft(coefs, modulus, domain)
print(result)