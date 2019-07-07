class Unit:
    def __init__ (self, name, cost, population, life):
        self.name = name
        self.cost = cost
        self.population = population
        self.life = life

    def sayMyCost (self):
        print("I cost {} minerals and {} vespine gas".format(self.cost["minerals"], self.cost["gas"]))



class Type(Unit):
    def __init__ (self, name, cost, population, life, race, isBionic, type):
        Unit.__init__ (self, name, cost, population, life)
        self.race = race
        self.isBionic = isBionic
        self.type = type



class Entity(Type):
    def __init__ (self, name, cost, population, life, race, isBionic, type, code, genTime, status, attack):
        Type.__init__ (self, name, cost, population, life, race, isBionic, type)
        self.code = code
        self.genTime = genTime
        self.status = status
        self.attack = attack

    def attackEnemy (self, enemy):
        enemy.life["HP"] -= self.attack
        print("{} attacked {}!!!".format(self.code, enemy.code))
        print("{}'s life became {}...".format(enemy.code, enemy.life["HP"]))
