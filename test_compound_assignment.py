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


def test_complex_assignment():
    print("this: ")
    code = """
        i = function() {return 0;};
        a = [1,1,2,3];
        v = 3;
        a[i()] += v;
        print(a);
    """
    vars = {}
    ast = parser.parse(tokenize(code))
    evaluate(ast, vars)
    a = vars["a"]
    print(f"a == {a}")
    assert vars["a"][0] == 4

