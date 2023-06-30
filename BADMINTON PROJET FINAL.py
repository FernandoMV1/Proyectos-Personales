#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################### importation des bibliothèques ############################################### 
from tkinter import * 
from tkinter.messagebox import *
#################################################################################################################

##################################### déclaration des variables ###################################################
Score1=0
Score2= 0
Set1=0
Set2=0
#################################################################################################################
		
    
###################################### création de l'interface graphique ##########################################

fenetre = Tk()##Définition de la fenetre



zone_dessin = Canvas(fenetre, width=450, height=300) #Définit les dimensions du canvas
zone_dessin.pack()
zone_dessin.create_line(0,100,450,100)#Création lignes tableau
zone_dessin.create_line(0,200,450,200)# 
zone_dessin.create_line(150,0,150,500)#
zone_dessin.create_line(300,0,300,500)#
zone_dessin.create_line(450,0,450,500)#

zone_dessin.create_text(75,50, text='Nom', font="Arial 16 italic", fill='blue')#Nom dans les cases correspondantes
zone_dessin.create_text(225,50, text='Score', font="Arial 16 italic", fill='blue')
zone_dessin.create_text(375,50, text='Set', font="Arial 16 italic", fill='blue')
zone_dessin.create_text(75,150, text='Equipe 1', font="Arial 16 italic", fill='red')
zone_dessin.create_text(75,250, text='Equipe 2', font="Arial 16 italic", fill='red')

label_Score1=Label(fenetre, text=Score1) #Création des "labels" contenant les variables
label_Score1.place(x=225, y=140)#emplacement des labels dans le canvas
label_Score2=Label(fenetre, text=Score2)
label_Score2.place(x=225, y=240)
label_Set1=Label(fenetre, text=Set1)
label_Set1.place(x=375, y=140)
label_Set2=Label(fenetre, text=Set2)
label_Set2.place(x=375, y=240)

###################################################################################################################

########################################## définition des fonctions ###############################################

def PE1(): #définition des différentes variables en variable global
    global Score1
    global Score2
    global Set1
    Score1 += 1 
    label_Score1.config(text=Score1)
    
    if Score1 > 20 and Score2 != 21 and Score2 != 22: #Quand le joueur 1 gagne un jeu on augmente de 1 la variable "Jeu1" et on remet les scores des joueurs a 0
        label_Score1.config(text='0')
        Score1 = 0
        label_Score2.config(text='0')
        Score2 = 0
        Set1 += 1
        label_Set1.config(text=Set1)
        label_Score2.config(text='0')#on remet les scores des joueurs a 0
        Score2 = 0
    elif Score1 == 20 and Score2 == 20:#Bloc de condition dans lequel on vérifie si les scores sont égaux à 20, 
        while True:
            if abs(Score2 - Score1) >= 2: #si c'est le cas, on commence une boucle while qui se termine lorsqu'un joueur a une avance de deux points.
                label_Score1.config(text='0')
                Score1 = 0
                label_Score2.config(text='0')
                Score2 = 0
                if Score1 > Score2:
                    Set1 += 1 #On ajoute 1 si score 1 a 2 points de différence
                    label_Set1.config(text=Set1)
                else:
                    Set2 += 1
                    label_Set2.config(text=Set2)
                label_Score2.config(text='0')
                Score2 = 0
                break
    elif Set1 > 1 :
        showinfo('Bravo', 'Joueur 1 a gagné !')#On affiche un message pour annoncer que le joueur à gagner

def PE2():
    global Score1
    global Score2
    global Set2
    Score2 += 1 
    label_Score2.config(text=Score2)
    
    if Score2 > 20 and Score1 != 21 and Score1 != 22:
        label_Score2.config(text='0')
        Score2 = 0
        label_Score1.config(text='0')
        Score1 = 0
        Set2 += 1
        label_Set2.config(text=Set2)
        label_Score1.config(text='0')
        Score1 = 0
    elif Score1 == 20 and Score2 == 20:
        while True:
            if abs(Score1 - Score2) >= 2:
                label_Score1.config(text='0')
                Score2 = 0
                label_Score2.config(text='0')
                Score1 = 0
                if Score2 > Score1:
                    Set2 += 1
                    label_Set2.config(text=Set2)
                else:
                    Set1 += 1
                    label_Set1.config(text=Set1)
                label_Score1.config(text='0')
                Score1 = 0
                break
    elif Set2 > 1:
        showinfo('Bravo', 'Joueur 2 a gagné !')

			

	
#################################################################################################################	

Boutton1= Button(fenetre, text ='Point equipe 1', command=PE1).pack(side=LEFT, padx=10, pady=5)#Création bouttons, "command" sert a attribuer une fonction a un bouton
Boutton2= Button(fenetre, text ='Point equipe 2', command=PE2).pack(side=RIGHT, padx=10, pady=5)

fenetre.mainloop()#maintient la fenetre ouverte

#################################################################################################################


