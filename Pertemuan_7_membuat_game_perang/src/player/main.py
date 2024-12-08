
class Player():
    def __init__(self,nama , darah , attack_power):
        self.name = nama
        self.health = darah
        self.min_attack = attack_power

    def attack(self):
        return self.min_attack

    def take_demage(self, demage):
        self.health -= demage
        if self.health < 0 :
            self.health = 0

    def defense(self,incoming_demage):
        reduced_demage = max(0 , incoming_demage)
        self.take_demage(reduced_demage)
        
    def is_alive(self):
        return self.health > 0
