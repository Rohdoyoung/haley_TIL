import os 

T = str(int(input()))
TT = str(int(input()))
TTT = str(int(input()))


 
for tc in range(1, T+1):
    answer = ''
    if answer == '':
        answer = True
    elif answer != '':
        answer = False
    
    print('#{} {}' .format(tc, answer))