import sqlite3
from typing import List

conn = sqlite3.connect('Base.sqlite')
cursor = conn.cursor()

fichiers=['insert_animaux.sql','insert_animaux_types.sql','insert_animaux_velages.sql','insert_complications.sql','insert_familles.sql','insert_types.sql','insert_velages.sql','insert_velages_complications.sql']
for fichier in fichiers:
    fichier=open(fichier,"w")
    file=fichier.readlines()
    for line in file:
        line=line.strip()
        cursor.execute(line)
    truc.close()


conn.commit()
conn.close()