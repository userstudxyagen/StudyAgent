import sympy as sp

def solve_math(expr):
    try:
        result = sp.sympify(expr)
        return str(sp.simplify(result))
    except Exception as e:
        return f"Fehler: {e}"