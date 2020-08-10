
#this assumes 2 claw 6 scythe (not yet lol)
import random
import math
import numbers
#take spec max hits directly from the dps calculator
claw_max_fg = 48
claw_max_serp = 47
scymax=54
scythe_roll1, scythe_roll2, scythe_roll3 = 0, 0, 0
claws_done_fg = 0
claws_done_serp = 0
scythes_done = 0
damage_done = 0
claw_hit = 0
missed_counter = 0
bloat_defence = 100 #modify dependant on bgs damage
scy_att_bonus = 132 #max gear scy
claw_att_bonus = 79 #max gear claws
damagelist=[]
repetitions=1000

# = E * (B +64), B = equipment bonus, E = effective level
# effective level = ATT/DEF LVL(include pots) * PRAYER BOOST, THEN ROUNDED down, +8, ROUND DOWN


bloat_defence_roll=(bloat_defence+9)*(20+64) #calculates bloat defence roll
bloat_attack_roll_scy=(((((math.floor(118*1.2))+8)*(1.2))))*(scy_att_bonus + 64) #calculates player attack 
bloat_attack_roll_claw=(((((math.floor(118*1.2))+8)*(1.2))))*(claw_att_bonus + 64) #calculates player attack 

#print(bloat_attack_roll_claw)
#print(bloat_attack_roll_scy)
scythe_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll_claw+1)) #calculates claw accuracy
claw_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll_scy+1)) #calculates claw accuracy
print(claw_accuracy)


clawlist=[]



for i in range(1, repetitions):
    claws_done_fg=0
    damage_done=0
    while claws_done_fg < 1:
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
        clawlist.append(claw_hit)
        damage_done += claw_hit
        claws_done_fg += 1


sorted(clawlist)
print(clawlist)
