import sqlite3
baseDeDonnees = sqlite3.connect('Base2.db')
cursor= baseDeDonnees.cursor()

##4.2.##

# Total de vaches dans la famille

def TotalDeVachesDansFamille():
  familles={}
  for id_famille in cursor.execute("SELECT id FROM famille"):
    count=0
    for vache,famille in cursor.execute("SELECT id,famille_id FROM animaux "):
      if famille == id_famille:
        count += 1
        familles[famille]=count
  return familles

# Les vaches mortes de la famille

def TotalDeVachesMortesParFamille():
  familles = {}
  for id_famille in cursor.execute("SELECT id FROM famille"):
    count = 0
    for vache,famille in cursor.execute("SELECT id, famille_id FROM animaux WHERE decede= 1 "):
      if famille == id_famille:
        count += 1
        familles[famille] = count
  return familles

# les vaches vivantes dans la famille

def TotalDeVachesVivantesParFamille():
  VachesVivantes={}
  for famille in TotalDeVachesDansFamille().keys():
    VachesVivantes[famille]= int(TotalDeVachesDansFamille().values()) - int(TotalDeVachesMortesParFamille().values())
  return VachesVivantes



