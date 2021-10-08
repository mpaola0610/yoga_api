import random

warmups = ['shoulder-rolls','arm-circles','neck-rolls','sun salutation','calf-raises','march in place','hip-flexor raise',
    'good-mornings','motorcycle rev','shoulder-shrugs','jefferson-curls','cat-cow','kick-stand','hip-circles']
warriors = ['warrior1','warrior2','reverse','right-angle',]
balance = ['tree', 'warrior3', 'dancer', 'toe-hold','single knee-hug','chair','single leg chair']
cooldown = ['butterfly', 'wide-leg stretch','seated forward fold','pigeon','reverse pigeon','lying-spinal twist','happy-baby',
    'childs-pose','cat-cow','thread-needle']

class displaySequence:

    def __init__ (self, custom = True):
        self.custom = custom
    
    def sequence(self):
        self.warrior= []
        self.routine=[]
        self.r_warmups=[random.choice(warmups)for i in range(4)]
        for r in self.r_warmups:
            self.routine.append(r)
            print(f'{r}\n')
        for move in warriors:
            self.warrior.append(move)
            self.routine.append(move)
            print(f'{move}\n')
        self.r_balance=random.sample(balance,2)    
        for b in self.r_balance:
            self.routine.append(b)
            print(f'{b}\n')
        self.r_cooldown= random.sample(cooldown, 4)
        for c in self.r_cooldown:
            self.routine.append(c)
            print(f'{c}\n')
        print(self.routine)
        return self.r_warmups, self.warrior, self.r_balance, self.r_cooldown, self.routine

# dylan = displaySequence()       
        
def runSequence(client):        
    client.sequence()
    


# runSequence(dylan)
        
    
    
    
    





