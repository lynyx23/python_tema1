import random

difficulty=int(input("Selectati dificultatea: "))
health=300/difficulty
regen=90/difficulty

if difficulty==3:
    damage=random.randint(65,80)

elif difficulty==2:
    damage=random.randint(35,50)

elif difficulty==1:
    damage=random.randint(15,30)

print("Caracterul are {} viata pe dificultatea {} si a luat {} damage".format(int(health),difficulty,damage))
print("A ramas cu {} viata, apoi si-a regenerat {} viata".format(int(health-damage),int(regen)))
