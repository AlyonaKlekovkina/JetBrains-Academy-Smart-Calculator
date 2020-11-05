# write your code here
def addition(array):
    sum = 0
    for i in array:
        sum += i
    return sum


while True:
    inp = input()
    if inp == '/exit':
        print("Bye!")
        break
    elif inp == '/help':
        print('The program calculates the sum of numbers')
    else:
        x = list(map(int, inp.split()))
        if len(x) == 0:
            continue
        else:
            print(addition(x))
