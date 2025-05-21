
def calculator():
    try:
        expr = input("Enter an expression (e.g., 2 + 2): ")
        a_str, op, b_str = expr.split()
        a = int(a_str)
        b = int(b_str)
        if op == '+':
            print(f"{a} + {b} = {a + b}")
        elif op == '-':
            print(f"{a} - {b} = {a - b}")
        elif op == '*':
            print(f"{a} * {b} = {a * b}")
        elif op == '/':
            if b != 0:
                print(f"{a} / {b} = {a // b}")
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operator")
    except Exception as e:
        print("Invalid input:", e)

calculator()


## ahora podes hacer cambios y  comitearlos 


