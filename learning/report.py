
operations = {
            "add": (2, lambda a, b: a + b),
            "sub": (2, lambda a, b: a - b),
            "mul": (2, lambda a, b: a * b),
            "div": (2, lambda a, b: a / b),
            "pow": (2, lambda a, b: a ** b),
            "mod": (2, lambda a, b: a - (a / b).to_integral_value(rounding=ROUND_FLOOR) * b),
            "sqrt": (1, lambda a: a.sqrt()),
            "abs": (1, lambda a: abs(a)),
        }

print(operations["add"])