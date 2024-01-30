factors = []
divisor = 2
num = int(input())
while divisor <= num:
    if num % divisor == 0:
        factors.append(divisor)
        num = num / divisor
    else:
        divisor += 1

exponents = {}
for factor in factors:
    exponents[factor] = exponents.get(factor, 0) + 1

output = ""
for factor, exponent in exponents.items():
    if exponent > 1:
        output += str(factor) + "^" + str(exponent) + "*"
    else:
        output += str(factor) + "*"
print(output.rstrip("*"))