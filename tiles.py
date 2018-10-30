import items, enemies
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def introText(self):
        raise NotImplementedError()
    def modifyPlayer(self, player):
        raise NotImplementedError()
class StartRoom(MapTile):
    def introText(self):
        return '''
        You find yourself in some sort of test start room for some reason.
        There seems to be some paths leading out of here.
        '''
    def modifyPlayer(self, player):
        # No room action #
        pass
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
    def addLoot(self, player):
        player.inventory.append(self.item)
    def introText(self):
        return '''
        Oooooooooo loot for days!
        '''
    def modifyPlayer(self):
        self.addLoot(player)
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
    def introText(self):
        return '''
        Oh shit some enemies!
        '''
    def modifyPlayer(self, player):
        if self.enemy.isAlive():
            player.hp -= self.enemy.damage
            print('The {} does {} damage. You have {} HP remaining.'.format(self.enemy, self.enemy.damage, player.hp))

class DarkPath(MapTile):
    def introText(self):
        return '''
        You look forward but you cannot seem to see into the void. You must forge onwards.
        '''
    def modifyPlayer(self, player):
        # Room has no action on player #
        pass
class EmptyPath(MapTile):
    def introText(self):
        return '''
        Nothing but jungle for as far as the eye can see. You must forge onwards
        '''
    def modifyPlayer(self, player):
        # Room has no action on player #
        pass
class BanditAmbush(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.PotatoBandit())
    def introText(self):
        if self.enemy.isAlive():
            return '''
            A Potato Bandit jumps out of the bushes in front of you, drawing his weapon!
            '''
        else:
            return '''
            The corpse of the Potato Bandit rots beneath your feet.
            '''
class BunnyPath(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SavageBunny())
    def introText(self):
        if self.enemy.isAlive():
            return '''
            A small, sweet bunny is nimbling on a carrot just ahead of you.
            As you approach it, it turns on you with a frothing mouth and red eyes.
            It charges at you!
            '''
        else:
            return '''
            The remains of the savage bunny are splatted all over the place.
            '''
class GooderPath(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Gooder())
    def introText(self):
        if self.enemy.isAlive():
            return '''
            You spot a malformed humanoid charging at you from out of nowhere!
            '''
        else:
            return '''
            The pile of mush that was once the malformed humanoid is bubbling and churning.
            '''
class NathanimalPath(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Nathanimal())
    def introText(self):
        if self.enemy.isAlive():
            return '''
            After several minutes of chasing down the small child, you find him standing in a clearing facing you with two very shiny daggers in his hand.
            He starts doing his knife tricks again, but this time its more threatening and directed at you!
            You draw your weapon and charge him.
            '''
        else:
            return '''
            The poor child lays dead; glazed over eyes staring up into the infinite blue expanse.
            '''
class VaydaPath(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Vayda())
    def introText(self):
        if self.enemy.isAlive():
            return '''
            A small but menacing shadow stares at you from the darkness.
            A feeling of pure terror rises in your gut as you realize that this is how the Demon Queen Vayda is described.
            The shadow vanishes...\n
            Next thing you know, there's a hole in your chest...\n
            Everything fades to black.
            '''
        else:
            return '''
            HACKS!
            '''
class StickPath(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Stick())
    def introText(self):
        return '''
        Oh boy! There is a mighty looking stick laying right on your path!
        '''
class RockPath(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Rock())
    def introText(self):
        return '''
        As you stumble through the jungle, you trip on a rock.
        It hurt enough to make you consider using it against your enemies.
        '''
    def modifyPlayer(self):
        self.addLoot(player)
        player.hp -= 5
class CorpsePath(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.MoneeUnit(50))
    def introText(self):
        return '''
        You come across a horrifically mangled corpse, with strangely enough, potatoes surrounding it.
        Something shiny catches your eye though, a monee unit!
        '''
class DaggerPath(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
    def introText(self):
        return '''
        As you continue wondering through the jungle, you see a small child in a clearing.
        He seems to be wearing nothing but a speedo of sorts and a bear cloak.
        The boy seems to be playing with a knife or dagger, swinging it around wildly with swift and elegant movements.
        You step forward quietly as to not desrupt the child, however you step on a branch with a loud *thwack*.
        He jumps in surprise, dropping the dagger. He looks up at you with pure shame, and runs away.
        It looks like you just got yourself a brand new rusted dagger!
        '''

