def eval_poly_at(poly, x, modulus):
    y = 0
    power_of_x = 1
    for coefficient in poly:
        y += power_of_x * coefficient
        power_of_x *= x
    return y % modulus

poly = [1, 2, 3] # 3*x^2 + 2*x + 1
x = 2
modulus = 5

result = eval_poly_at(poly, x, modulus)
print(result)