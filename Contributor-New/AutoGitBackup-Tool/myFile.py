import ast
import math
import operator
import sys
from typing import Any, Dict

#!/usr/bin/env python3
"""
Safe calculator: evaluate arithmetic expressions with +, -, *, /, //, %, **, parentheses,
and selected math functions like sqrt, sin, cos, log, exp, with constants pi and e.
Usage:
   python myFile.py "2 + 3*4"
   python myFile.py              # starts interactive mode
"""


# Allowed operators
_BIN_OPS = {
      ast.Add: operator.add,
      ast.Sub: operator.sub,
      ast.Mult: operator.mul,
      ast.Div: operator.truediv,
      ast.FloorDiv: operator.floordiv,
      ast.Mod: operator.mod,
      ast.Pow: operator.pow,
}
_UNARY_OPS = {
      ast.UAdd: operator.pos,
      ast.USub: operator.neg,
}

# Allowed math functions and constants
_ALLOWED_FUNCS = {
      "sqrt": math.sqrt,
      "sin": math.sin,
      "cos": math.cos,
      "tan": math.tan,
      "asin": math.asin,
      "acos": math.acos,
      "atan": math.atan,
      "log": math.log,      # natural log; log(x, base) also allowed
      "log10": math.log10,
      "exp": math.exp,
      "fabs": math.fabs,
      "floor": math.floor,
      "ceil": math.ceil,
      "degrees": math.degrees,
      "radians": math.radians,
      "hypot": math.hypot,
      "abs": abs,
}
_ALLOWED_NAMES = {
      "pi": math.pi,
      "e": math.e,
}


class _SafeEvaluator:
      def __init__(self, extra_names: Dict[str, Any] | None = None):
            self.names: Dict[str, Any] = dict(_ALLOWED_NAMES)
            if extra_names:
                  # Only allow numeric values in extra names
                  for k, v in extra_names.items():
                        if isinstance(v, (int, float)):
                              self.names[k] = v

      def eval(self, expr: str) -> float:
            try:
                  node = ast.parse(expr, mode="eval")
            except SyntaxError as e:
                  raise ValueError(f"Syntax error: {e.msg}") from e
            value = self._eval_node(node.body)
            if not isinstance(value, (int, float)):
                  raise ValueError("Expression did not evaluate to a number")
            return float(value)

      def _eval_node(self, node: ast.AST) -> Any:
            if isinstance(node, ast.Constant):
                  if isinstance(node.value, (int, float)):
                        return node.value
                  raise ValueError(f"Unsupported constant: {node.value!r}")

            if isinstance(node, ast.Num):  # for very old Python versions
                  return node.n

            if isinstance(node, ast.BinOp):
                  op_type = type(node.op)
                  if op_type not in _BIN_OPS:
                        raise ValueError(f"Operator not allowed: {op_type.__name__}")
                  left = self._eval_node(node.left)
                  right = self._eval_node(node.right)
                  return _BIN_OPS[op_type](left, right)

            if isinstance(node, ast.UnaryOp):
                  op_type = type(node.op)
                  if op_type not in _UNARY_OPS:
                        raise ValueError(f"Unary operator not allowed: {op_type.__name__}")
                  operand = self._eval_node(node.operand)
                  return _UNARY_OPS[op_type](operand)

            if isinstance(node, ast.Name):
                  if node.id in self.names:
                        return self.names[node.id]
                  if node.id in _ALLOWED_FUNCS:
                        return _ALLOWED_FUNCS[node.id]
                  raise ValueError(f"Unknown identifier: {node.id}")

            if isinstance(node, ast.Call):
                  # Only allow simple function calls: func(arg1, arg2, ...)
                  if not isinstance(node.func, ast.Name):
                        raise ValueError("Only direct function calls are allowed")
                  func_name = node.func.id
                  if func_name not in _ALLOWED_FUNCS:
                        raise ValueError(f"Function not allowed: {func_name}")
                  func = _ALLOWED_FUNCS[func_name]
                  if node.keywords:
                        # Support log(x, base=10) style keywords safely by evaluating values
                        kwargs = {kw.arg: self._eval_node(kw.value) for kw in node.keywords if kw.arg}
                  else:
                        kwargs = {}
                  args = [self._eval_node(a) for a in node.args]
                  return func(*args, **kwargs)

            if isinstance(node, ast.Expression):
                  return self._eval_node(node.body)

            # Disallow everything else: attributes, subscripts, comprehensions, lambdas, etc.
            raise ValueError(f"Unsupported expression element: {type(node).__name__}")


def evaluate(expression: str, variables: Dict[str, float] | None = None) -> float:
      """
      Evaluate a safe arithmetic expression.
      variables can provide numeric bindings (e.g., {"x": 3}).
      """
      return _SafeEvaluator(variables).eval(expression)


def _print_result(expr: str) -> int:
      try:
            result = evaluate(expr)
            print(result)
            return 0
      except Exception as e:
            print(f"Error: {e}")
            return 1


def main(argv: list[str]) -> int:
      if argv:
            exit_code = 0
            for expr in argv:
                  exit_code |= _print_result(expr)
            return exit_code

      print("Safe Calculator (type 'quit' or Ctrl-D to exit)")
      print("Examples: 2+3*4, (1+2)**3/7, sqrt(2), sin(pi/2), log(8, 2)")
      while True:
            try:
                  expr = input("> ").strip()
            except EOFError:
                  print()
                  break
            if not expr:
                  continue
            if expr.lower() in {"q", "quit", "exit"}:
                  break
            _print_result(expr)
      return 0


if __name__ == "__main__":
      raise SystemExit(main(sys.argv[1:]))