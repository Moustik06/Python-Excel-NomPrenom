import xlrd
doc = xlrd.open_workbook_xls(r'PATH')
sh = doc.sheet_by_index(0)

def prenomNom():
    N = []
    P = []
    for i in range(1,sh.nrows):
            prenom = sh.cell(i,2)
            nom = sh.cell(i,1)
            P.append(str(prenom)[6:-1])
            N.append(str(nom)[6:-1])
            print(P[i-1],N[i-1],sep=".",end="@xxxxxxx.xx")
prenomNom() 

