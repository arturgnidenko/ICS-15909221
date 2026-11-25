import math

x = float(input("Введіть значення x: "))

if x >= 5:
    y = -9 + math.log(x) + math.sqrt(x)
elif -0.5 < x < 5:
    y = math.cos(x) + math.sin(2 * x)
else:
    y = abs(-x**2 + 2 * x**(-x))

print("f(x) =", y)
