import random

warmups = ['shoulder-rolls','arm-circles','neck-rolls','sun salutation','calf-raises','march in place','hip-flexor raise',
    'good-mornings','motorcycle rev','shoulder-shrugs','jefferson-curls','cat-cow','kick-stand','hip-circles']
warriors = ['warrior1','warrior2','reverse','right-angle',]
balance = ['tree', 'warrior3', 'dancer', 'toe-hold','single knee-hug','chair','single leg chair']
cooldown = ['butterfly', 'wide-leg stretch','seated forward fold','pigeon','reverse pigeon','lying-spinal twist','happy-baby',
    'childs-pose','cat-cow','thread-needle']

def sequence():
    routine=[]
    r_warmups=[random.choice(warmups)for i in range(4)]
    for r in r_warmups:
        routine.append(r)
        print(f'{r}\n')
    for move in warriors:
        routine.append(move)
        print(f'{move}\n')
    r_balance=random.sample(balance,2)    
    for b in r_balance:
        routine.append(b)
        print(f'{b}\n')
    r_cooldown= random.sample(cooldown, 4)
    for c in r_cooldown:
        routine.append(c)
        print(f'{c}\n')
    print(routine)
       
        
sequence()        
        
    
    
    
    





