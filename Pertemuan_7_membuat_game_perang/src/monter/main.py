import random

class Monster:
    def __init__(self,nama, darah, attack_power):
        self.name = nama
        self.health = darah
        self.min_attack = attack_power

    def attack(self):
        return random.randint(1,self.min_attack)
    
    def take_demage(self,damage):
        self.health -= damage
        if self.health < 0 :
            self.health = 0
    def is_alive(self):
        return self.health > 0