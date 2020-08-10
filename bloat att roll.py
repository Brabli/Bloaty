#TO DO: put in defence rolls to suport dynamic defence (bgs)
#       put in serp claw specs
#       test bgs and other predown damage in game
# fix claws if else statements
#this assumes 2 claw 6 scythe (not yet lol)
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#take spec max hits directly from the dps calculator
claw_max_fg = 48
claw_max_serp = 47
scymax=48
scythe_roll1, scythe_roll2, scythe_roll3 = 0, 0, 0
claws_done_fg = 0
claws_done_serp = 0
scythes_done = 0
damage_done = 0
claw_hit = 0
missed_counter = 0
bloat_defence = 100 #modify dependant on bgs damage
scy_att_bonus = 147 #max gear scy
claw_att_bonus = 94 #max gear claws

# = E * (B +64), B = equipment bonus, E = effective level
# effective level = ATT/DEF LVL(include pots) * PRAYER BOOST, THEN ROUNDED down, +8, ROUND DOWN


bloat_defence_roll=(bloat_defence+9)*(20+64) #calculates bloat defence roll
bloat_attack_roll=((math.floor(118*1.2))+8)*(scy_att_bonus + 64) #calculates player attack 
scythe_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll+1)) #calculates claw accuracy

bloat_defence_roll=(bloat_defence+9)*(20+64) #calculates bloat defence roll
bloat_attack_roll=((math.floor(118*1.2))+8)*(claw_att_bonus + 64) #calculates player attack 
claw_accuracy = 1 - (bloat_defence_roll+2) / (2*(bloat_attack_roll+1)) #calculates claw accuracy

for i in range(1,10):
  #claw spec sim in max strength with nezzy faceguard
  #8 specs cause this currently assumes 0 bgs
  while claws_done_fg < 8:
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
  print(str(damage_done) + "claw damage")

  #Total scythe damage whilst bloat is down(6 scythe hits each)
  while scythes_done< 30:
    if random.random() < scythe_accuracy:
      scythe_roll1 = random.randint(0,scymax)
    if random.random() < scythe_accuracy:
      scythe_roll2 = random.randint(0,.5*scymax)
    if random.random() < scythe_accuracy:
      scythe_roll3 = random.randint(0,.25*scymax)
    damage_done += scythe_roll1 + scythe_roll2 + scythe_roll3
    scythes_done += 1
  print(str(damage_done) + "total")
  damage_done=0
  claws_done_fg=0
  scythes_done=0
  
def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

fig1 = plt.figure()

data = np.random.rand(2, 25)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
                                   interval=50, blit=True)

  
