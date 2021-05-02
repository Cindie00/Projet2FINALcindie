import sqlite3
conn = sqlite3.connect('Base2.db')
cursor = conn.cursor()

def Pourcentages():

    
    def makeDates(Jfrom, Mfrom, Yfrom, Jto, Mto, Yto):
        jours = Jfrom
        mois = Mfrom
        annee = Yfrom

        dates = {}
        
        dates[f"{jours:02}/{mois:02}/{annee}"] = 0
        while not (jours == Jto and mois == Mto and annee == Yto):
            jours += 1
            if mois == 2:
                if annee%4 != 0 and jours == 29:
                    jours = 1
                    mois += 1
                elif annee%4 == 0 and jours == 30:
                    jours = 1
                    mois += 1
            elif mois%2 == 1:
                if mois <= 7 and jours == 32:
                    jours = 1
                    mois += 1
                if mois > 7 and jours == 31:
                    jours = 1
                    mois += 1
            elif mois%2 == 0:
                if mois <= 7 and jours == 31:
                    jours = 1
                    mois += 1
                if mois > 7 and jours == 32:
                    jours = 1
                    mois += 1
            
            if mois == 13:
                mois = 1
                annee += 1
            
            dates[f"{jours:02}/{mois:02}/{annee}"] = 0
        return dates

    Dates = makeDates(int(tuple(cursor.execute("select date from velages"))[0][0][0:2]), int(tuple(cursor.execute("select date from velages"))[0][0][3:5]), int(tuple(cursor.execute("select date from velages"))[0][0][6:]), int(tuple(cursor.execute("select date from velages"))[-1][0][0:2]), int(tuple(cursor.execute("select date from velages"))[-1][0][3:5]), int(tuple(cursor.execute("select date from velages"))[-1][0][6:]))

    for born in cursor.execute("select date from velages"):
        Dates[born[0]] += 1

    cycle = []
    for a in range(28):
        cycle.append(0)

    n = 0
    for c in range(0, len(Dates)-28, 29):
        tnc = 0
        for t in range(28):
            tnc += list(Dates.items())[c+t][1] #tnc: Total de naissance du cycle
        if tnc != 0:
            for i in range(28):
                cycle[i] += list(Dates.items())[c+i][1]*(100/tnc)
        n += 1

    for m in range(len(cycle)):
        cycle[m] = round(cycle[m]/n, 2)
    print(cycle)

    Somme = 0
    for i in cycle:
        Somme += i
    print(Somme)
    
    return cycle

if __name__ == '__main__':
        conn.close()

Pourcentages()
