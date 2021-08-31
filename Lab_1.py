# skriv lab 1 nedanför

class Pokemon():

  def __init__(self,row):
    divided_row = row.split(",")
    self.number = divided_row[0]
    self.name = divided_row[1]
    self.type1 = divided_row[2]
    self.type2 = divided_row[3]
    self.total = divided_row[4]
    self.hp = divided_row[5]
    self.attack = divided_row[6]
    self.defense = divided_row[7]
    self.sp_atk = divided_row[8]
    self.sp_def = divided_row[9]
    self.speed = divided_row[10]
    self.generation = divided_row[11]
    self.legendary = divided_row[12]
  

  def __str__(self):
    return self.name + " " + self.type1



pokedex = Pokemon("1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False")
print(pokedex)
