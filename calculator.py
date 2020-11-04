# write your code here
def addition(a, b):
    return int(a) + int(b)


while True:
    inp = input()
    if inp == '/exit':
        print("Bye!")
        break
    elif inp != inp.strip():
        continue
    else:
        x = list(map(int, inp.split()))
        if len(x) == 1:
            print(x[0])
        if len(x) == 2:
            print(addition(x[0], x[1]))
