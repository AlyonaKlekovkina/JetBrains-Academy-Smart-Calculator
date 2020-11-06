# write your code here


def determine_sign(array):
    signs = []
    for i in range(1, len(array), 2):
        if array[i].startswith('-'):
            result = len(array[i])
            if result % 2 != 0:
                signs.append('-')
            else:
                signs.append('+')
        elif array[i].startswith('+'):
            signs.append('+')
    return signs


def determine_ints(array):
    try:
        integers = []
        for j in range(0, len(array), 2):
            if array[j].startswith("+"):
                s = array[j].split('+')
                integers.append(s[1])
            elif array[j].endswith("+"):
                return "Invalid expression"
            else:
                integers.append(int(array[j]))
        return integers
    except ValueError:
        return "Invalid expression"


def calculate_expression(signs, integers):
    try:
        result_of_calculation = integers[0]
        for i in range(len(integers) - 1):
            if signs[i] == '+':
                result_of_calculation += integers[i+1]
            elif signs[i] == '-':
                result_of_calculation -= integers[i+1]
        return result_of_calculation
    except IndexError:
        return "Invalid expression"


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
    else:
        x = list(map(str, inp.split()))
        if len(x) == 0:
            continue
        elif (len(determine_sign(x)) == 0) and (len(x) == 2):
            print("Invalid expression")
        else:
            print(calculate_expression(determine_sign(x), determine_ints(x)))
