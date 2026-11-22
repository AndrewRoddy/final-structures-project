from evaluator import evaluate
import parser
from tokenizer import tokenize


def run_code(code):
    vars = {}
    ast = parser.parse(tokenize(code))
    evaluate(ast, vars)
    return ast, vars


def test_compound_assignment_addition():
    print("test compound assignment addition")
    code = """
        a = 1;
        a += 2;
    """
    _, vars = run_code(code)
    a = vars["a"]
    assert vars["a"] == 3


def test_compound_assignment_subtraction():
    print("test compound assignment subtraction")
    code = """
        a = 9;
        a -= 2;
    """
    _, vars = run_code(code)
    a = vars["a"]
    assert vars["a"] == 7


def test_compound_assignment_division():
    print("test compound assignment division")
    code = """
        a = 2;
        a /= 2;
    """
    _, vars = run_code(code)
    a = vars["a"]
    assert vars["a"] == 1


def test_compound_assignment_multiplication():
    print("test compound assignment multiplication")
    code = """
        a = 3;
        a *= 3;
    """
    _, vars = run_code(code)
    a = vars["a"]
    assert vars["a"] == 9


def test_complex_compound_assignment():
    print("test complex compound assignment")
    code = """
        i = function() {return 0;};
        a = [1,1,2,3];
        v = 3;
        a[i()] += v;
        print(a);
    """
    _, vars = run_code(code)
    a = vars["a"]
    assert vars["a"][0] == 4

