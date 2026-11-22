from evaluator import evaluate
import parser
from tokenizer import tokenize


# Helper function for running the tests
def run_code(code):
    vars = {}
    ast = parser.parse(tokenize(code))
    result = evaluate(ast, vars)
    return ast, vars, result


# Regular tests
def test_compound_assignment_addition():
    print("test compound assignment addition")
    code = """
        a = 1;
        a += 2;
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"] == 3


def test_compound_assignment_subtraction():
    print("test compound assignment subtraction")
    code = """
        a = 9;
        a -= 2;
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"] == 7


def test_compound_assignment_division():
    print("test compound assignment division")
    code = """
        a = 2;
        a /= 2;
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"] == 1


def test_compound_assignment_multiplication():
    print("test compound assignment multiplication")
    code = """
        a = 3;
        a *= 3;
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"] == 9


# Complex tests
def test_complex_compound_assignment_addition():
    print("test complex compound assignment")
    code = """
        i = function() {return 0;};
        a = [1,1,2,3];
        v = 3;
        a[i()] += v;
        print(a);
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"][0] == 4


def test_complex_compound_assignment_subtraction():
    print("test complex compound assignment")
    code = """
        i = function() {return 0;};
        a = [9,1,2,3];
        v = 3;
        a[i()] -= v;
        print(a);
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"][0] == 6


def test_complex_compound_assignment_division():
    print("test complex compound assignment")
    code = """
        i = function() {return 0;};
        a = [9,1,2,3];
        v = 3;
        a[i()] /= v;
        print(a);
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"][0] == 3


def test_complex_compound_assignment_multiplication():
    print("test complex compound assignment")
    code = """
        i = function() {return 0;};
        a = [3,1,2,3];
        v = 3;
        a[i()] *= v;
        print(a);
    """
    _, vars, _ = run_code(code)
    a = vars["a"]
    assert vars["a"][0] == 9


# Checks for side effects
def test_side_effects():
    print("test for side effects")
    code = """
       count = 0;
       function next() {
           set count = count + 1;
           return 0;
       };
       x = [1, 2];
       x[next()] += 1;
    """
    _, vars, _ = run_code(code)
    assert vars["count"] == 1
    assert vars["x"] == [2, 2]


def test_exit_before_compound_assignment():
    print("test compound assignment")
    code = """
        x = 1;
        function stop() {
            exit(3);
        };
        x += stop();
        i_should_not_exist = 1;
        
    """
    _, vars, result = run_code(code)
    assert result == (3, "exit")
    assert vars["x"] == 1
    assert "i_should_not_exist" not in vars