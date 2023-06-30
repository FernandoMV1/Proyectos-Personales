import csv
fichier=open("company.csv")

lecteur = list(csv.DictReader(fichier))
Tab=[dict(ligne) for ligne in lecteur]

for i in range(len(Tab)):
    Tab[i]["Seniority"] = int(Tab[i]["Seniority"])
    salaire = Tab[i]["Salary"].split(" ")[0]
    salaire = salaire.split (",")
    Tab[i]["Salary"] = float(salaire[0]+"."+salaire[1])
print (" 1) nombre de salaires", len(Tab))
print()

(NbrF, NbrH) = (0,0)
for i in range (len(Tab)):
    if Tab[i]["Sex"]=="F":
        NbrF = NbrF + 1
    else:
        NbrH = NbrH + 1
print(" 2) Il y a", NbrF, "femmes employées et", NbrH, "hommes employées")
print()

(NbrManager) = (0)
for i in range (len(Tab)):
    if Tab[i]["Level"]=="manager":
        NbrManager = NbrManager + 1
print(" 3) Il y a", NbrManager, "managers employées")
print()

level = ["director", "manager", "engineer", "tecchnician"]
NbrLevel = {l:0 for l in level}
for i in range (len(Tab)):
    for l in level:
        if Tab[i]["Level"] == l:
            NbrLevel[l] = NbrLevel[l] + 1
print(" 4) La repartition des employés par postes est: ")
print(NbrLevel)
print()

level = ["director", "manager", "engineer", "technician"]
Salairelevel = {l:[0,"H"] for l in level}
for i in range(len(Tab)):
    for l in level:
        if Tab[i]["Level"]==l:
            if Tab[i]["Salary"]>Salairelevel[l][0]:
                Salairelevel[l][0]=Tab[i]["Salary"]
                Salairelevel[l][1]=Tab[i]["Sex"]
print(" 5) les salaires les plus élévés et le sexe de l'employé par postes sont: ")
print(Salairelevel)
print()

(NbrF, NbrH) = (0,0)
(SalaireMoyF, SalaireMoyH) = (0,0)
for i in range (len(Tab)):
    if Tab[i]["Sex"] == "F":
        NbrF = NbrF + 1
        SalaireMoyF = SalaireMoyF + Tab[i]["Salary"]
    else:
        NbrH = NbrH + 1
        SalaireMoyH = SalaireMoyH + Tab[i]["Salary"]
(SalaireMoyF,SalaireMoyH) = (SalaireMoyF/NbrF,SalaireMoyH/NbrH)

print(" 6) le salaire moyen des femmes est: ", SalaireMoyF)
print("   le salaire moyen des hommes est: ", SalaireMoyH)
print()

level = ["director", "manager", "engineer", "technician"]
NbrLevel = {'director': 4, 'manager': 11, 'engineer': 6, 'technician': 19}
SalaireMoyLevel = {l:0 for l in level}
for i in range(len(Tab)):
    for l in level:
        if Tab[i]["Level"]==l:
            SalaireMoyLevel[l]=SalaireMoyLevel[l] + Tab[i]["Salary"]
for l in level:
    SalaireMoyLevel[l] = SalaireMoyLevel/NbrLevel
print(" 7) Les salaires moyens par postes sont: ")
print(SalaireMoyLevel)






