# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    if a != 0:
        discriminant = ((b ** 2) - 4 * a * c)
        if discriminant >= 0:
            root1 = float(round((-b+(((b**2)-4*a*c)**1/2))/(2*a)))
            root2 = float(round((-b-(((b**2)-4*a*c)**1/2))/(2*a)))
            if root1 == root2:
                return f"({root1})"
            else:
                return f"{root1, root2}"
        else:
            return "( )"
    elif a == 0:
        root1 = float(round((-c/b)))
        return (root1)
def value_y(a, b, c, x):
    valorY = (a*x)**2 + b*x + c
    return valorY
def to_string(a, b, c):
    if a == 0 and b == 0:
        textoCambiado = f"f(x) = {c}"
        return textoCambiado
    elif a == 0:
        textoCambiado = f"f(x) = {b} * X + {c}"
        return textoCambiado
    elif b == 0:
        textoCambiado = f"f(x) = {a} * X^2 + {c}"
        return textoCambiado
    else:
        textoCambiado = f"f(x) = {a} * X^2 + {b} * X + {c}"
        return textoCambiado


def derivation(a, b, c):
    if a == 0:
        derivada = f"f'(x) = {b}"
        return derivada
    elif b == 0:
        derivada = f"f'(x) = {2*a} * X"
        return derivada
    else:
        derivada = f"f'(x) = {2*a} * X + {b}"
        return derivada