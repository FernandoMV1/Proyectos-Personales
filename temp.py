from random import* 
import matplotlib.pyplot as plt
import time


def triInsertion(Liste):
    for i in range(1,len(Liste)):
        carte=Liste[i]
        j=i-1
        while j>=0 and Liste[j]>carte:
            Liste[j+1]=Liste[j]
            j=j-1
        Liste[j+1]=carte
    return Liste 


def triSelection(Liste):
    for i in range(0,len(Liste)-1):
        minimum=Liste[i]
        rangmin=i
        for j in range(i+1,len(Liste)):
            if Liste[j]<minimum:
                minimum=Liste[j]
                rangmin=j
        Liste[i],Liste[rangmin]=Liste[rangmin],Liste[i]
    return Liste 

def fusion(gauche,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):        
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat
 
def tri_fusion(m):
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))

def genereListe(longueur,valeurmax):
    Liste=[]
    for i in range(longueur):
       Liste.append(randint(0,valeurmax))
    return Liste

        

def representationTemps():
    X=[]
    Y=[]
    Z=[]    
    P=[]
    T=[]
    for i in range(500,5000,500):
        X.append(i)
        L=genereListe(i,8000)
        L1=L
        L2=L 
        L3=L
        startTime = time.time()
        triInsertion(L1)
        endTime = time.time()
        Y.append(endTime-startTime)
        startTime = time.time()
        triSelection(L2)
        endTime = time.time() 
        Z.append(endTime-startTime)
        P.append((i**2)*(2*10**-8))
        startTime = time.time()
        tri_fusion(L3)
        endTime = time.time()
        T.append(endTime-startTime)
    plt.plot(X,Y)
    plt.plot(X,Z)
    plt.plot(X,P)
    plt.plot(X,T)
    plt.legend(["insertion","selection","parabole","fusion"])
    plt.ylabel("temps en secondes")
    plt.xlabel("taille des listes")
    plt.savefig("Courbes.png")
    plt.clf()

representationTemps()