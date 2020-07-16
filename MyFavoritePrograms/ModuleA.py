# This code is altered from the demo given in the instruction to avoid an INFINITE LOOP! (No thanks, teach)

def type_something():
    st = input('Type something (\'stop\') to quit: ')

    while True:
        if st == 'stop':
            break
        else:
            print(f'You typed: "{st}".')
            st = input('Type something (\'stop\') to quit: ')

def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum

def sum_of_cubes(n):
    sum = 0
    for i in range(1, n + 1):
        sum = i * i * i
    return sum