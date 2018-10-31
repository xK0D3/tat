class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return '{}\n=====\n{}\nValue: {}\n'.format(self.name, self.description, self.value)
        
class MoneeUnit(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name = 'Monee Unit',
                         description = 'An imaginary coin with a {} stamped on the front.'.format(str(self.amount)),
                         value = self.amount)
                         
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    def __str__(self):
        return '{}\n=====\n{}\nValue: {}\nDamage: {}'.format(self.name, self. description, self.value, self.damage)
class Stick(Weapon):
    def __init__(self):
        super().__init__(name = 'Stick',
                         description = 'A somewhat pointy stick, possibly useful for bashing a skull in.',
                         value = 2,
                         damage = 3)
class Rock(Weapon):
    def __init__(self):
        super().__init__(name = 'Rock',
                         description = 'A fist-sized rock, suitable for bludgeoning.',
                         value = 3,
                         damage = 5)
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name = 'Dagger',
                         description = 'A rusted dagger that might still be a viable stabbing machine.',
                         value = 10,
                         damage = 8)
       
#School Test
        
