# interpreter.py

variables = {}

def run_line(line):
    line = line.strip()

    # Handle comments or empty lines
    if not line or line.startswith("#"):
        return

    # PRINT
    if line.startswith("print "):
        expr = line[6:].strip()
        value = evaluate_expression(expr)
        print(value)
        return

    # INPUT
    if line.startswith("input "):
        prompt, varname = line.split("->")
        prompt = prompt.replace("input", "").strip().strip('"')
        varname = varname.strip()
        user_input = input(prompt + " ")
        variables[varname] = parse_value(user_input)
        return

    # LET
    if line.startswith("let "):
        _, rest = line.split("let", 1)
        varname, expr = rest.strip().split("=", 1)
        varname = varname.strip()
        value = evaluate_expression(expr.strip())
        variables[varname] = value
        return

    print("Unknown command:", line)

# def evaluate_expression(expr):
#     # Variable reference
#     if expr in variables:
#         return variables[expr]

#     # Math operations (very basic for now)
#     if "*" in expr:
#         left, right = expr.split("*")
#         return parse_value(evaluate_expression(left.strip())) * parse_value(evaluate_expression(right.strip()))
#     if "+" in expr:
#         left, right = expr.split("+")
#         return parse_value(evaluate_expression(left.strip())) + parse_value(evaluate_expression(right.strip()))

#     # String literal
#     if expr.startswith('"') and expr.endswith('"'):
#         return expr.strip('"')

#     # Try to parse number
#     return parse_value(expr)
def evaluate_expression(expr):
    expr = expr.strip()

    # Variable reference
    if expr in variables:
        return variables[expr]

    # String literal
    if expr.startswith('"') and expr.endswith('"'):
        return expr.strip('"')

    # Reverse
    if expr.startswith("reverse "):
        inner = expr[len("reverse "):].strip()
        val = evaluate_expression(inner)
        return str(val)[::-1]

    # Repeat
    if expr.startswith("repeat "):
        parts = expr[len("repeat "):].split(" ", 1)
        if len(parts) != 2:
            return "ERROR: repeat needs 2 arguments"
        char_expr, times_expr = parts
        char = str(evaluate_expression(char_expr.strip()))
        times = int(evaluate_expression(times_expr.strip()))
        return char * times

    # Math operations (basic)
    if "*" in expr:
        left, right = expr.split("*")
        return parse_value(evaluate_expression(left.strip())) * parse_value(evaluate_expression(right.strip()))
    if "+" in expr:
        left, right = expr.split("+")
        return parse_value(evaluate_expression(left.strip())) + parse_value(evaluate_expression(right.strip()))

    # Try to parse number
    return parse_value(expr)


def parse_value(value):
    try:
        return int(value)
    except:
        return value

def run_script(file_path):
    with open(file_path) as f:
        for line in f:
            run_line(line)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py your_program.txt")
    else:
        run_script(sys.argv[1])
