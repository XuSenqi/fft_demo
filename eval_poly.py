def eval_poly_at(poly, x, modulus):
    y = 0
    power_of_x = 1
    for coefficient in poly:
        y += power_of_x * coefficient
        power_of_x *= x
    return y % modulus

# poly = [1, 2, 3] # 3*x^2 + 2*x + 1
# x = 2
# modulus = 5

#result = eval_poly_at([1,2,3], 2, 5)  # poly 3*x^2 + 2*x + 1, x, modulus
#print(result)

xs = [1, 85, 148, 111, 336, 252, 189, 226]
o = [0 for i in xs]
for i, x in enumerate(xs):
    result = eval_poly_at([3,1,4,1,5,9,2,6], x, 337)
    o[i]=result
print(o)

xs = [1, 148, 336, 189]
o = [0 for i in xs]
for i, x in enumerate(xs):
    result = eval_poly_at([3,4,5,2], x, 337)
    o[i]=result
print(o)