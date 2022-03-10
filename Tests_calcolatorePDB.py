Cm = 12.0107
Nm = 14.0067
Om = 15.999
Hm = 1.00784
Sm = 32.065

ToT_atomi = 0
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


filename = input()


#creare dataset     

with open(filename,"r") as files:  
    for riga in files:
        lista = riga.split()
        if riga.count("ATOM"):
            ATOM = lista[0]
            chain = lista[4]
            #ATOM == "ATOM" 
            if chain == "A":                           
                #chain = lista[4]
                Numero = lista[1]            
                CA = lista[2]
                residue = lista[3] 
                atomi = lista[-1]                         
                x = lista[6]
                y = lista[7]
                z = lista[8]
                virtual_tab = ATOM +' '+residue + ' ' + atomi + ' ' + chain + ' ' + x + ' ' + y + ' ' + z +' '+ CA + ' ' + Numero
                riga_virtual_tab = str(virtual_tab)
                riga_virtual_tab += nuova_linea
                tabella.write(riga_virtual_tab)
    tabella.close()


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


# print(f"il numero dei carboni sono {C}")
# print(f"il numero degli azoto sono {N}")
# print(f"il numero degli ossigeni sono {O}")
# print(f"il numero degli idrogeni sono {H}")
# print(f"il numero degli zolfi sono {S}\n")

# print(f"la massa totale de carbonio {Cm_tot}")
# print(f"la massa totale dello zolfo {Nm_tot}")
# print(f"la massa totale dell'ossigeno {Om_tot}")
# print(f"la massa totale dello zolfo {Sm_tot}")

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


print(tabella)#FONDAMENTALE PER CAPIRE  


#calcolo centro geometrico (Centroide)

for riga3 in open('dataset'):
    lista = riga3.split()
    print(lista)
    if riga3.count('CA'):
        print("il mio x è ",lista[4])
        geom_x +=float(lista[4])
        print(geom_x)
        # print(geom_x,"coordinata x")
        geom_y += float(lista[5])
        geom_z += float(lista[6])


print(riga3, "questa è la riga 2 ")
# print(geom_x, "è il valore della sommatoria di x")
# print(geom_y, "è il valore della sommatoria di y")
# print(geom_z, "è il valore della sommatoria di z")

valore_Centroide_X = geom_x // ToT_atomi
valore_Centroide_Y = geom_y // ToT_atomi
valore_Centroide_Z = geom_z // ToT_atomi

print(valore_Centroide_X)
print(valore_Centroide_Y)
print(valore_Centroide_Z)


