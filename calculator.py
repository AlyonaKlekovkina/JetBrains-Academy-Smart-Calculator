# write your code here
def addition(array):
    the_sum = 0
    for i in array:
        the_sum += i
    return the_sum


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
    integers = []
    for j in range(0, len(array), 2):
        integers.append(int(array[j]))
    return integers


def calculate_expression(signs, integers):
    result_of_calculation = integers[0]
    for i in range(len(integers) - 1):
        if signs[i] == '+':
            result_of_calculation += integers[i+1]
        elif signs[i] == '-':
            result_of_calculation -= integers[i+1]
    return result_of_calculation


while True:
    inp = input()
    if inp == '/exit':
        print("Bye!")
        break
    elif inp == '/help':
        print('The program excepts the expression, determines the sign in in (double minus turns to plus), and calculates the expression')
    else:
        x = list(map(str, inp.split()))
        if len(x) == 0:
            continue
        else:
            array_of_signs = determine_sign(x)
            array_of_integers = determine_ints(x)
            final_result = calculate_expression(array_of_signs, array_of_integers)
            print(final_result)
