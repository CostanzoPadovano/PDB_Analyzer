import os
import api_cacolatorePDB

pollo = 0.00
pollo1 = 0.00

Cm = 12.0107
Nm = 14.0067
Om = 15.999
Hm = 1.00784
Sm = 32.065

ToT_atomi = 0
massa_TOTALE = 0

C = 0
N = 0
O = 0
H = 0
S = 0
nuova_linea = "\n"

x = 0
y = 0
z = 0

geom_x = 0
geom_y = 0
geom_z = 0
massa_x = 0
massa_y = 0
massa_z = 0


tabella = open("dataset", "w+") #dataset diverrà la finestra virtuale tipo txt
filename = input('/home/costano/Desktop/Progetto_Bioinformatica/ESAME_PYTHON/2qnd.pdb')


#creare dataset     
api_cacolatorePDB.PDBcalc(filename,tabella)
api_cacolatorePDB.PESOMOLECOLARE(filename)

#lista virtual_lab

for riga2 in open("dataset"):
    lista2 = riga2.split()
    ATOM = lista2[0]
    residuo = lista2[1]
    tipo= lista2[2]
    catena = lista2[3]
    x = lista2[4]
    y = lista2[5]
    z = lista2[6]
    CA = lista2[7]
    Numero = lista2[8]
    


    # print(riga2)
#conta totale atomi e totale massa
    if "C" == tipo:
        C += 1
        Cm_tot = C * Cm 
    elif "N" == tipo:
        N += 1    
        Nm_tot = N * Nm
    elif "O" == tipo:
        O += 1       
        Om_tot = O * Om  
    elif "H" == tipo:
        H += 1   
        Hm_tot = H * Hm                 
    elif "S" == tipo:
        S += 1  
        Sm_tot = S * Sm   
    ToT_atomi += 1
    massa_TOTALE = C * Cm + N * Nm + O * Om +  H * Hm + S * Sm 
print(massa_TOTALE,"massa totale")

if H == 0:
    print(f"la massa totale dell'idrogeno non è disponibile, in quanto essi sono assenti e bisogna aggiungerli\n")
else:
    print(f"la massa totale degli idrogeni è {Hm_tot}\n") 

#calcolo centro di massa della proteina

    
massa_tot = Cm_tot + Nm_tot + Om_tot + Sm_tot    
for riga in open('dataset'):
    lista = riga.split()
    if lista[2]=="C":
        MixRi_x = float(Cm) * float(lista[4])
        MixRi_y = float(Cm) * float(lista[5])
        MixRi_z = float(Cm) * float(lista[6])
        massa_x += MixRi_x
        massa_y += MixRi_y
        massa_z += MixRi_z
        #print(lista[4], "rigacazzooooo")

    elif lista[2] == "N":
        MixRi_x = float(Nm) * float(lista[4])
        MixRi_y = float(Nm) * float(lista[5])
        MixRi_z = float(Nm) * float(lista[6])
        massa_x += MixRi_x
        massa_y += MixRi_y
        massa_z += MixRi_z
  
    elif lista[2] == "O":
        MixRi_x = float(Om) * float(lista[4])
        MixRi_y = float(Om) * float(lista[5])
        MixRi_z = float(Om) * float(lista[6])
        massa_x += MixRi_x
        massa_y += MixRi_y
        massa_z += MixRi_z
       
    elif lista[2] == "S":
        MixRi_x = float(Sm) * float(lista[4])
        MixRi_y = float(Sm) * float(lista[5])
        MixRi_z = float(Sm) * float(lista[6])
        massa_x += MixRi_x
        massa_y += MixRi_y
        massa_z += MixRi_z
     
        
        
risultato_x = massa_x // massa_tot
risultato_y = massa_y // massa_tot
risultato_z = massa_z // massa_tot

print(risultato_x,"risultato del centro di massa della proteina di x")
print(risultato_y,"risultato del centro di massa della proteina di y")
print(risultato_z,"risultato del centro di massa della proteina di z")

#calcolo centro geometrico (Centroide)

for riga3 in open('dataset'):
    lista = riga3.split()
    if riga3.count('CA'):
        geom_x += float(lista[4])
        geom_y += float(lista[5])
        geom_z += float(lista[6])

# print(geom_x, "è il valore della sommatoria di x")
# print(geom_y, "è il valore della sommatoria di y")
# print(geom_z, "è il valore della sommatoria di z")

valore_Centroide_X = geom_x // ToT_atomi
valore_Centroide_Y = geom_y // ToT_atomi
valore_Centroide_Z = geom_z // ToT_atomi

print(valore_Centroide_X)
print(valore_Centroide_Y)
print(valore_Centroide_Z)

nuova_linea1 = '\n'


#generatore file.txt.         
indice = 0
boolIndice = False

while boolIndice == False:
    try:
        os.mknod(f"out{indice}.pdb")#mknod è per creare un file.txt mentre mkdir per creare una cartella
        boolIndice = True
    except FileExistsError:
        boolIndice = False
        indice+=1
        print("esiste già il file")

#apportare modifica al file .pdb aggiungendo i valori x y z del centro geometrico 
with open(filename) as f:
    with open(f"out{indice}.pdb", "w+") as f1:
        for line in f:
            if line.count("END"):
                f1.write(f"HETATM 9999999  Centro_Geometrico referer_chain_A  {valore_Centroide_X} {valore_Centroide_Y} {valore_Centroide_Z} {pollo} {pollo1} C_geom")
                f1.write("\n")
                f1.write(line)
            else:
                f1.write(line)
        f1.close()
        
