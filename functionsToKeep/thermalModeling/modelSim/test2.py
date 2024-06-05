import matplotlib.pyplot as plt
import random
josh = 5


newguess = 0
test = 0
overshoot = 0
undershoot = 0
test = 0
while josh != round(newguess):
    print(abs(josh-newguess))
    if overshoot == 0 and undershoot == 0:
        if josh > newguess:
            add = random.uniform(1,100-newguess)
            newguess += add
            if josh < newguess:
                overshoot = 1
                # oldguess = newguess
        elif josh < newguess:
            sub = random.uniform(1,newguess)
            newguess -= sub
            if josh > newguess:
                undershoot = 1
                # oldguess = newguess
        
    elif overshoot == 1 and undershoot == 0:
        sub = random.uniform(1,add-1)
        newguess -= sub
        if josh > newguess:
            overshoot = 0
            undershoot = 1
        elif josh < newguess:
            add -= sub
    elif undershoot == 1 and overshoot == 0:
        add = random.uniform(1,sub-1)
        newguess += add
        if josh < newguess:
            overshoot = 1
            undershoot = 0
        elif josh > newguess:
            sub -= add
    test += 1
print(newguess)
print('\n',test)


    




    
    
    

