import math
import re

priority = {'(': 0, '^': 3, '/': 2, '*': 2, '+': 1, '-': 1}


def from_infix_to_postfix(x):
    output = []
    stack = []
    for i in x:
        if i.isdigit():
            output.append(i)
        elif i in variables:
            value = variables.get(i)
            output.append(value)
        elif len(stack) == 0 or i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif priority.get(i) > priority.get(stack[-1]):
            stack.append(i)
        else:
            while len(stack) > 0 and priority.get(i) <= priority.get(stack[-1]):
                output.append(stack.pop())
            stack.append(i)
    while len(stack) != 0:
        output.append(stack.pop())
    return output


def get_operands(stack):
    right_operand = int(stack.pop())
    left_operand = int(stack.pop())
    return right_operand, left_operand


def calculate_postfix(postfix):
    stack = []
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        elif i == '*' or i == '+' or i == '-' or i == '/' or i == '^':
            r_op, l_op = get_operands(stack)
            if i == '^':
                result = math.pow(l_op, r_op)
            elif i == '/':
                result = l_op / r_op
            elif i == '*':
                result = l_op * r_op
            elif i == '+':
                result = l_op + r_op
            elif i == '-':
                result = l_op - r_op
            stack.append(result)
    return stack


def check_brackets_balance(expression):
    stack = []
    for i in expression:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) >= 1:
            stack.pop()
        elif i == ')' and len(stack) == 0:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


def signs_evaluation(expression):
    stack = []
    for i in expression:
        if i == '*' and stack[-1] == '*':
            return False
        elif i == '/' and stack[-1] == '/':
            return False
        elif i.startswith('-') and len(i.replace('-', '')) == 0:
            if len(i) % 2 != 0:
                stack.append('-')
            else:
                stack.append('+')
        else:
            stack.append(i)
    return stack


def declare_variable(input):
    var = input.split('=', 1)
    identifier = var[0].strip()
    value = var[1].strip()
    if not identifier.isalpha():
        print('Invalid identifier')
    elif identifier.isalpha() and value.isdigit():
        variables.update({identifier: value})
    elif identifier.isalpha() and value.isalpha() and (value not in variables):
        print('Unknown variable')
    elif identifier.isalpha() and value.isalpha() and (value in variables):
        v = variables.get(value)
        variables.update({identifier: v})
    elif not value.isdigit():
        print('Invalid assignment')


def single_identifier(var):
    if var[0].startswith('-') or var[0].isnumeric():
        print(var[0])
    elif not var[0].isalpha():
        print("Invalid identifier")
    elif var[0].isalpha() and var[0] not in variables:
        print("Unknown variable")
    elif var[0] in variables:
        print(variables.get(var[0]))


def delete_spaces(expression):
    s = []
    for i in expression:
        if i != '' and i != ' ':
            s.append(i)
    return s


variables = {}
commands = ['/exit', '/help']
while True:
    inp = input()
    if inp.startswith("/") and inp not in commands:
        print("Unknown command")
    elif inp == '/exit':
        print("Bye!")
        break
    elif inp == '/help':
        print('The program excepts the expression, determines the sign in it (double minus becomes plus), and calculates the expression')
    elif '=' in inp:
        declare_variable(inp)
    else:
        x = re.sub('\++', '+', inp)
        x = re.split('([^a-zA-Z0-9-?\d])', x)
        x = delete_spaces(x)
        if len(x) == 0:
            continue
        elif len(x) == 1:
            single_identifier(x)
        elif not signs_evaluation(x):
            print("Invalid expression")
        elif not check_brackets_balance(signs_evaluation(x)):
            print("Invalid expression")
        else:
            postfix = from_infix_to_postfix(signs_evaluation(x))
            result = calculate_postfix(postfix)
            print(result[0])
