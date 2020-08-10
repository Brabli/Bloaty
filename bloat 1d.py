#TO DO: put in defence rolls to suport dynamic defence (bgs)
#       put in serp claw specs
#       test other predown damage in game
# fix claws if else statements
#this assumes 2 claw 5 scythe (not yet lol)
import random
import math
claw_max_fg = 48
claw_max_serp = 47
bgs_max_fg= 84
scymax=54
scythe_roll1, scythe_roll2, scythe_roll3 = 0, 0, 0
claws_done_fg = 0
claws_done_serp = 0
scythes_done = 0
damage_done = 0
claw_hit = 0
scy_att_bonus = 132 #max gear scy
claw_att_bonus = 79 #max gear claws
bgs_att_bonus=154 # max gear bgs
damagelist=[]
repetitions=5

# = E * (B +64), B = equipment bonus, E = effective level
# effective level = ATT/DEF LVL(include pots) * PRAYER BOOST, THEN ROUNDED down, +8, ROUND DOWN
for i in range(1,repetitions):
    ##before spec reduction bloat defence roll 9156
    bloat_defence = 100  #modifies itself assuming 2xbgs
    bloat_attack_roll_bgsspec=2*(((((math.floor(118*1.2))+8)*(1.2))))*(bgs_att_bonus + 64) #calculates player attack
    bgs_spec_accuracy = 1 - (9156+2) / (2*(bloat_attack_roll_bgsspec+1)) #calculates bgs accuracy
    defense_reduced=0

   
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
    
    bloat_attack_roll_scy=(((((math.floor(118*1.2))+8)*(1.2))))*(scy_att_bonus + 64) #calculates player attack 
    bloat_attack_roll_claw=(((((math.floor(118*1.2))+8)*(1.2))))*(claw_att_bonus + 64) #calculates player attack 


    scythe_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll_scy+1)) #calculates claw accuracy
    claw_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll_claw+1)) #calculates scythe accuracy

    while scythes_done< random.randint(12,17): 
            if random.random() < scythe_accuracy:
              scythe_roll1 = random.randint(0,math.floor(.5*scymax))
            if random.random() < scythe_accuracy:
              scythe_roll2 = random.randint(0,math.floor(.25*scymax))
            if random.random() < scythe_accuracy:
              scythe_roll3 = random.randint(0,math.floor(.125*scymax))
            damage_done += scythe_roll1 + scythe_roll2 + scythe_roll3
            scythes_done += 1
            damagelist.append(damage_done)
    print(damage_done)



    damage_done=0
      #claw spec sim in max strength with nezzy faceguard
      #8 specs cause this currently assumes 0 bgs
    while claws_done_fg < 10:
        if random.random() < claw_accuracy:
          claw_hit = random.randint(claw_max_fg, 2 * claw_max_fg + 1)
        else:
          if random.random() < claw_accuracy:
            claw_hit = random.randint(0.75 * claw_max_fg, 1.75 * claw_max_fg + 1)
          else: 
            if random.random() < claw_accuracy:
              claw_hit = random.randint(0.50 * claw_max_fg,1.50 * claw_max_fg + 1)
            else:
              if random.random() < claw_accuracy:
                claw_hit = random.randint(0.25 * claw_max_fg,1.25*claw_max_fg + 1)
              else:
                claw_hit = 2
        damage_done += claw_hit
        claws_done_fg += 1

    print(damage_done)

      #Total scythe damage whilst bloat is down(5 scythe hits each)
    while scythes_done< 25:
        if random.random() < scythe_accuracy:
          scythe_roll1 = random.randint(0,math.floor(scymax))
        if random.random() < scythe_accuracy:
          scythe_roll2 = random.randint(0,math.floor(.5*scymax))
        if random.random() < scythe_accuracy:
          scythe_roll3 = random.randint(0,math.floor(.25*scymax))
        damage_done += scythe_roll1 + scythe_roll2 + scythe_roll3
        scythes_done += 1

    print(damage_done)
      
    damagelist.append(damage_done)

      
      #print(str(damage_done) + " total damage from claws + scy")
    claws_done_fg=0
    scythes_done=0
    damage_done=0
      
    count= 0

    #5 man bloat 2000hp
    for i in damagelist: 
        if i > .9*2000 : 
            count = count + 1
    print("If 90% pre down, " + str((count/repetitions)*100) + "% chance of 1d")

    count= 0

    for i in damagelist: 
        if i > .85*2000 : 
            count = count + 1
    print("If 85% pre down, " + str((count/repetitions)*100) + "% chance of 1d")

    count= 0

    for i in damagelist: 
        if i > .8*2000 : 
            count = count + 1
    print("If 80% pre down, " + str((count/repetitions)*100) + "% chance of 1d")







