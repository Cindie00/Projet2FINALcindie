
################################################
## Fichier main.py du Projet 2 du Groupe 1A_5 ##
################################################

# Les imports
from extractorkyllian import *
from extractormax import *
from extractorcindie import *
from extractorchong import *
from flask import Flask, render_template, request

#Lancement de Flask
app = Flask(__name__, template_folder='templates')
app.debug = True

#Route vers la page principale du site
@app.route("/LaFermeDes3Chenes")
def principal():
    #MAX
    PourcentageParCycle= [40, 50, 10, 47, 80, 2, 49, 56, 57, 13, 50, 56, 67, 15, 67, 22, 44, 66, 88, 56, 8, 4, 10, 50, 60, 5, 6, 8] #Pourcentages() #

    #CINDIE
    mortes = [10,5,20,40] #list(TotalDeVachesMortesParFamille().values()) #
    vivantes= [75,80,100,120] #list(TotalDeVachesVivantesParFamille().values()) #
    familles= ['famille1','famille2','famille3','famille4'] #list(TotalDeVachesVivantesParFamille().keys()) #

    #KYLLIAN
    deces= list(totalveauxmortnes().values())  #[40,50,10,47,30,2,49,56,57,13,50,10]

    #CHONG
    VelageX =['Velage1','Velage2','Velage3','Velage4','Velage5']
    VelageS = [4,8,2,4,7]
    #velage = Velage()
    #Annee = list(velage.keys())
    #VelageX = []
    #for a in Annee:
        #for i in range(1, 8):
            #if i == 1:
                #VelageX.append("{}: {}er velage(s)".format(a, i))
            #else:
                #VelageX.append("{}: {}eme velage(s)".format(a, i))
    #VelageS = []
    #for a in Annee:
        #for i in range(1, 8):
            #VelageS.append(velage[a][i])

    return render_template('interfacefinale2.html', PourcentageVelagePleineLune=PourcentageParCycle, m=mortes, v=vivantes,f=familles, n=deces, VelageX=VelageX, VelageS=VelageS)



if __name__ == '__main__':
    app.run()
