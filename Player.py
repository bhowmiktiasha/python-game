from Charater import Character
from Enemy import Enenmy
from random import randint


class Player(Character):

    
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max =10
  def quit(self):
    print "%s can't find the way back home, and dies of starvation.\nR.I.P." % self.name
    self.health = 0
  def help(self):
Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  }
  print Commands.keys()
  def status(self): print "%s's health: %d/%d" % (self.name, self.health, self.health_max)
  def tired(self):
    print "%s feels tired." % self.name
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print "%s can't rest now!" % self.name; self.enemy_attacks()
    else:
      print "%s rests." % self.name
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s is rudely awakened by %s!" % (self.name, self.enemy.name)
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print "%s slept too much." % self.name; self.health = self.health - 1
  def explore(self):
    if self.state != 'normal':
      print "%s is too busy right now!" % self.name
      self.enemy_attacks()
    else:
      print "%s explores a twisty passage." % self.name
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s encounters %s!" % (self.name, self.enemy.name)
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def flee(self):
    if self.state != 'fight': print "%s runs in circles for a while." % self.name; self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print "%s flees from %s." % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
      else: print "%s couldn't escape from %s!" % (self.name, self.enemy.name); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print "%s swats the air, without notable results." % self.name; self.tired()
    else:
      if self.do_damage(self.enemy):
        print "%s executes %s!" % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print "%s feels stronger!" % self.name
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print "%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name)
 
