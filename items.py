class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return '{}\n=====\n{}\nValue: {}\n'.format(self.name, self.description, self.value)
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    def __str__(self):
        return '{}\n=====\n{}\nValue: {}\nDamage: {}'.format(self.name, self. description, self.value, self.damage)
class GoldCoin(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name = 'Gold Coin',
                         description = 'A round coin with a {} stamped on the front.'.format(str(self.amount)),
                         value = self.amount)
