import random
import math
bgs_max_fg= 84#actual max is 42 due to 50% reduction, this is accounted for in the damage_done
scymax=45/2
scythe_roll1, scythe_roll2, scythe_roll3 = 0, 0, 0
scythes_done = 0
damage_done = 0
scy_att_bonus = 132 #max gear scy
bgs_att_bonus=154 # max gear bgs
damagelist=[]
repetitions=1000

# = E * (B +64), B = equipment bonus, E = effective level
# effective level = ATT/DEF LVL(include pots) * PRAYER BOOST, THEN ROUNDED down, +8, ROUND DOWN
for i in range(1,repetitions):
  
        ##before spec reduction bloat defence roll 9156
        bloat_defence = 100  #modifies itself assuming 2xbgs
        bloat_attack_roll_bgsspec=2*(((((math.floor(118*1.2))+8)*(1.2))))*(bgs_att_bonus + 64) #calculates player attack
        bgs_spec_accuracy = 1 - (9156+2) / (2*(bloat_attack_roll_bgsspec+1)) #calculates bgs accuracy
        defense_reduced=0
        damage_done=0
        scythes_done=0
       
        if random.random() <bgs_spec_accuracy:
          bgs_spec= random.randint(0, bgs_max_fg)
          bloat_defence = 100 - bgs_spec
          damage_done=bgs_spec/2

        bloat_defence_roll=(bloat_defence+9)*(20+64) #calculates bloat defence roll
        bgs_spec_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll_bgsspec+1)) #calculates bgs accuracy 
        if random.random() <bgs_spec_accuracy:
          bgs_spec= random.randint(0, bgs_max_fg)
          damage_done+=(bgs_spec/2) 

        bloat_defence=bloat_defence- bgs_spec
        if bloat_defence<0:
          bloat_defence=0
        #print("bloat defence is " + str(bloat_defence))
        #print("damage done by bgs is " + str(damage_done))
        bloat_defence_roll=(bloat_defence+9)*(20+64) #calculates bloat defence roll
        
        bloat_attack_roll_scy=(((((math.floor(118*1.2))+8))))*(scy_att_bonus + 64) #calculates player attack 

        scythe_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll_scy+1)) #calculates claw accuracy


        while scythes_done< random.randint(12,17): 
            if random.random() < scythe_accuracy:
              scythe_roll1 = random.randint(0,math.floor(scymax))
            if random.random() < scythe_accuracy:
              scythe_roll2 = random.randint(0,math.floor(.5*scymax))
            if random.random() < scythe_accuracy:
              scythe_roll3 = random.randint(0,math.floor(.25*scymax))
            damage_done += scythe_roll1 + scythe_roll2 + scythe_roll3
            scythes_done += 1
        #print("Total damage done is: " + str(damage_done))
        damagelist.append(damage_done)

count= 0

    #5 man bloat 2000hp
for i in damagelist: 
        if i > .5*2000 : 
            count = count + 1
print("Chances of getting 5% damage whilst Necking are: " + str((count/repetitions)*100) + "%")

count= 0

for i in damagelist: 
        if i > .10*2000 : 
            count = count + 1
print("Chances of getting 10% damage whilst Necking are: " + str((count/repetitions)*100) + "%")

count= 0

for i in damagelist: 
        if i > .11*2000 : 
            count = count + 1
print("Chances of getting 11% damage whilst Necking are: " + str((count/repetitions)*100) + "%")

count= 0

for i in damagelist: 
        if i > .12*2000 : 
            count = count + 1
print("Chances of getting 12% damage whilst Necking are: " + str((count/repetitions)*100) + "%")

count= 0

for i in damagelist: 
        if i > .13*2000 : 
            count = count + 1
print("Chances of getting 13% damage whilst Necking are: " + str((count/repetitions)*100) + "%")

count= 0

for i in damagelist: 
        if i > .14*2000 : 
            count = count + 1
print("Chances of getting 14% damage whilst Necking are: " + str((count/repetitions)*100) + "%")

count= 0

for i in damagelist: 
        if i > .15*2000 : 
            count = count + 1
print("Chances of getting 15% damage whilst Necking are: " + str((count/repetitions)*100) + "%")


