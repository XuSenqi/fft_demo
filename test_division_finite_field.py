def div(f, modulus):
    arr = list(range(1, 337))
    for ele in arr:
        if ele*f%modulus == 1:
            print("1/", f, "%", modulus, "=", ele)
            break

domain=[1, 85, 148, 111, 336, 252, 189, 226]
for d in domain:
    div(d, 337)