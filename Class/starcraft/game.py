import character as HERO

Jim = HERO.Jim
Zeratul = HERO.Zeratul


Jim.sayMyCost()
Zeratul.sayMyCost()
while (Zeratul.life["HP"] >  0) :
        shoot = int(input())
        if shoot == 1 :
            Jim.attackEnemy(Zeratul)
        else : print('Missed Suckers!')

Zeratul.life["HP"] = 0
Zeratul.status = "dead"
print("Zeratul died with {}HP and {}Shield".format(Zeratul.life["HP"], Zeratul.life["Shield"]))
