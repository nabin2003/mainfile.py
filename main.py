import addition
import subtraction
import multiplication
import division

print("Calculator Application")

x = addition.add_two_numbers(5, 3)
y = subtraction.subtract_two_numbers(10, 4)
z = multiplication.multiply_two_numbers(2, 3)
w = division.divide_two_numbers(8, 2)
v = division.divide_two_numbers(5, 0)  

print(f"5 + 3 = {x}")
print(f"10 - 4 = {y}")
print(f"2 * 3 = {z}")
print(f"8 / 2 = {w}")
print(f"5 / 0 = {v}")
