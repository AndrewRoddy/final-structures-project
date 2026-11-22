from evaluator import evaluate
import parser
from tokenizer import tokenize


def test_evaluate_numbers():
    print("test evaluate numbers")
    vars = {}
    ast = parser.parse(tokenize("x=1; x += 2"))
    evaluate(ast, vars)
    x = vars["x"]
    print(f"x == {x}")
    assert vars["x"] == 3
