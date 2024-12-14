class Calculator:
    def __init__(self, a, b, operation_type):
        self.a = a
        self.b = b
        self.operation_type = operation_type

    def calculate(self):
        if self.operation_type == 'addition':
            return self.a + self.b
        elif self.operation_type == 'subtraction':
            return self.a - self.b
        elif self.operation_type == 'multiplication':
            return self.a * self.b
        elif self.operation_type == 'division':
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid operation type"

a = 10.5
b = 5.2
operation = 'addition'

calc = Calculator(a, b, operation)
result = calc.calculate()
print(f"Result of {operation} between {a} and {b}: {result}")
