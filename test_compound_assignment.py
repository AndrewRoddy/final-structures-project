from evaluator import evaluate
import parser
from tokenizer import tokenize


def test_compound_assignment_addition():
    print("test evaluate numbers")
    code = """
        a = 1;
        a += 2;
    """
    vars = {}
    ast = parser.parse(tokenize(code))
    evaluate(ast, vars)
    a = vars["a"]
    print(f"a == {a}")
    assert vars["a"] == 3

def test_compound_assignment_subtraction():
    print("test evaluate numbers")
    code = """
        a = 9;
        a -= 2;
    """
    vars = {}
    ast = parser.parse(tokenize(code))
    evaluate(ast, vars)
    a = vars["a"]
    print(f"a == {a}")
    assert vars["a"] == 7


def test_compound_assignment_division():
    print("test evaluate numbers")
    code = """
        a = 2;
        a /= 2;
    """
    vars = {}
    ast = parser.parse(tokenize(code))
    evaluate(ast, vars)
    a = vars["a"]
    print(f"a == {a}")
    assert vars["a"] == 1


def test_compound_assignment_multiplication():
    print("test evaluate numbers")
    code = """
        a = 3;
        a *= 3;
    """
    vars = {}
    ast = parser.parse(tokenize(code))
    evaluate(ast, vars)
    a = vars["a"]
    print(f"a == {a}")
    assert vars["a"] == 9


def test_complex_compound_assignment():
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

