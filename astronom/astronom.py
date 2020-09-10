states = [int(s) for s in input().split(' ')] 

if len(states) == 1:
    if states[0] == 0:
        print('UP')
    else:
        print("UNKNOWN")
else:
    if states[-1] == 0:
        print('UP')
    elif states[-1] > states[-2]:
        if states[-1] != 15:
            print('UP')
        else:
            print('DOWN')
    else:
        print('DOWN') 
