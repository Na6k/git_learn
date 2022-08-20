'''
this function from class Character branch 
'''
class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.first_name + ' ' + self.last_name
        self.inicial = self.first_name[:1] + '.' + self.last_name[:1] + '.'
              
class Charecter:

    def __init__(self, rase, damage = 5):
        self.rase = rase
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0
