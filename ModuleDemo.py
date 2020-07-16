# This code is altered from the demo given in the instruction to avoid an INFINITE LOOP! (No thanks, teach)

st = input('Type something (\'stop\') to quit: ')

while True:
    if st == 'stop':
        break
    else:
        print(f'You typed: "{st}".')
        st = input('Type something (\'stop\') to quit: ')