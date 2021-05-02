

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting
import sqlite3
baseDeDonnees = sqlite3.connect('Base2.db')
cursor= baseDeDonnees.cursor()

def totalveauxmortnes():
    nombre_mort_nes={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,}
    for ligne in cursor.execute("SELECT animaux_id, animaux.mort_ne, velages.date from animaux INNER JOIN velages ON animaux.id = velages.id WHERE animaux.mort_ne <>'8';"):
        nombre_mort_nes[ligne[2][3:5]]+=1
    return render_templates('graphiques/kyllian.html', data=nombre_mort_nes)
