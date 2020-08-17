class Fighter:
  def __init__(self,name):
    self.name = name
    self.health = 100 #predefined parameters
    self.damage = 10  #predefined parameters

  def attack(self, other_guy):
    other_guy.health = other_guy.health - self.damage

sak = Fighter("Sarthak")
pak= Fighter("Prabhu")
jak = Fighter("Jax")

pak.attack(sak)

print(sak.health)
