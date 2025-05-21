class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()  # make operation lowercase to avoid case issues

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operation"

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

calc = Calculator(a, b, operation)
result = calc.calculate()

print("Result:", result)
