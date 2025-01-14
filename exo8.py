class Voiture:

  def __init__(self, modele, pressionAV, pressionAR):
    self.modele = modele
    self.pressionAV = pressionAV
    self.pressionAR = pressionAR
    self.roues = [Roue(pressionAV, "AVG"), Roue(pressionAV, "AVD"), Roue(pressionAR, "ARG"), Roue(pressionAR, "ARD"), Roue(pressionAV, "RDS")]

  def presenter(self):
    print(f"Voiture {self.modele}, pressionAV: {self.pressionAV} bars, pressionAR: {self.pressionAR} bars")
    for roue in self.roues:
      roue.presenter()

class Roue:

  def __init__(self, pression, position):
    self.pression = pression
    self.position = position

  def presenter(self):
    print(f"Roue {self.position}, pression: {self.pression} bars")

v1 = Voiture("Peugeot 205", 2.0, 2.2)
v1.presenter()