from Character import Character
from random import randint
class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'a katappa'
    self.health = randint(1, player.health)
