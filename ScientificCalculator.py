import math

class ScientificCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    def power(self, x, y):
        return math.pow(x, y)

    def square_root(self, x):
        if x < 0:
            return "Cannot calculate square root of a negative number"
        return math.sqrt(x)

    def logarithm(self, x):
        if x <= 0:
            return "Cannot calculate logarithm of a non-positive number"
        return math.log(x)

    def sine(self, x):
        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        return math.tan(x)
    
    def factorial(self, n):
        if n == 0:
            return 1
        elif n < 0:
            return "Cannot calculate factorial of a negative number"
        else:
            return math.factorial(n)

# Example usage:
calculator = ScientificCalculator()

print("Addition: ", calculator.add(5, 3))
print("Subtraction: ", calculator.subtract(5, 3))
print("Multiplication: ", calculator.multiply(5, 3))
print("Division: ", calculator.divide(5, 3))
print("Power: ", calculator.power(5, 3))
print("Square Root: ", calculator.square_root(25))
print("Logarithm: ", calculator.logarithm(10))
print("Sine: ", calculator.sine(0))
print("Cosine: ", calculator.cosine(0))
print("Tangent: ", calculator.tangent(0))
print("Factorial: ", calculator.factorial(5))
