class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def isAlive(self):
        return self.hp > 0

class PotatoBandit(Enemy):
    def __init__(self):
        super().__init__(name = 'Potato Bandit',
                         hp = 10,
                         damage = 5)
class SavageBunny(Enemy):
    def __init__(self):
        super().__init__(name = 'Savage Bunny',
                         hp = 4,
                         damage = 2)
class Gooder(Enemy):
    def __init__(self):
        super().__init__(name = 'Gooder',
                         hp = 8,
                         damage = 6)
class Nathanimal(Enemy):
    def __init__(self):
        super().__init__(name = 'Nathanimal',
                         hp = 30,
                         damage = 10)
class Vayda(Enemy):
    def __init__(self):
        super().__init__(name = 'Vayda',
                         hp = 999,
                         damage = 999)