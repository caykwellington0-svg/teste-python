# calculadora_segura.py
import ast
import operator

# operadores permitidos mapeados para funções Python
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
}

UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def safe_eval(expr: str):
    """
    Avalia expressões aritméticas de forma segura usando AST.
    Suporta números, parênteses, + - * / ** % // e sinais unários.
    """
    node = ast.parse(expr, mode='eval').body
    return _eval_node(node)

def _eval_node(node):
    if isinstance(node, ast.Constant):  # números (Python 3.8+)
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Constantes não-numéricas não são permitidas.")
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in OPERATORS:
            return OPERATORS[op_type](left, right)
        raise ValueError(f"Operador binário não permitido: {op_type}")
    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)
        if op_type in UNARY_OPERATORS:
            return UNARY_OPERATORS[op_type](operand)
        raise ValueError(f"Operador unário não permitido: {op_type}")
    # evitar qualquer outro tipo de nó (chamadas, nomes, atribuições, etc.)
    raise ValueError(f"Expressão não permitida (nó: {type(node)})")

def repl():
    print("Calculadora segura. Digite 'sair' ou 'exit' para encerrar.")
    while True:
        try:
            expr = input(">>> ").strip()
            if expr.lower() in ("sair", "exit", "quit"):
                print("Encerrando.")
                break
            if not expr:
                continue
            resultado = safe_eval(expr)
            # mostra int sem .0 quando for inteiro
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            print(resultado)
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    repl()
    