import sqlite3
with sqlite3.connect("Base2.db") as conn:
    cursor=conn.cursor()
    data=list(cursor.execute("SELECT mere_id, date FROM velages"))
    
def Velage():
    dico={}
    annee={}
    for x in data:
        if dico.get(x[0],None) == None:
            dico[x[0]]=1
        else:
            dico[x[0]]+=1
        if annee.get(x[1][-4:],None) == None:
            annee[x[1][-4:]]={dico[x[0]]:1}
        
        else:
            if annee[x[1][-4:]].get(dico[x[0]],None) == None:
                annee[x[1][-4:]][dico[x[0]]]=1
            else:
                annee[x[1][-4:]][dico[x[0]]]+=1

    for a in annee:
        for i in range(1,8):
            if annee[a].get(i,None) == None:
                annee[a][i]=0
        
    
    return annee
