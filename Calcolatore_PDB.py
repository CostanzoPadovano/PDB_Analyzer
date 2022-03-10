#! /usr/bin/python

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import Conta_atomi_LIB

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Example")
        self.master.rowconfigure(5, weight=5)
        self.master.columnconfigure(5, weight=5)
        self.grid(sticky=W+E+N+S)

        self.button = Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=1, column=0, sticky=W)

    def load_file(self):
        fname = askopenfilename(filetypes=("File PDB", "*.pdb"))

        Cm = 12.0107
        Nm = 14.0067
        Om = 15.999
        Hm = 1.00784
        Sm = 32.065

        C = 0
        N = 0
        O = 0
        H = 0
        S = 0
        nuova_linea = "\n"

        x = 0
        y = 0
        z = 0

        massa_x = 0
        massa_y = 0
        massa_z = 0

        tabella = open("dataset", "w+") #dataset diverrà la finestra virtuale tipo txt


        filename = fname
        #creare dataset     

        with open(filename,"r") as files:  
            for riga in files:
                lista = riga.split() 
                ATOM = lista[0]   
                ATOM == "ATOM"
                if riga.count("ATOM"):
                    residue = lista[3] 
                    atomi = lista[-1]
                    chain = lista[4]
                    if chain == "A":                        
                        x = lista[6]
                        y = lista[7]
                        z = lista[8]
                        virtual_tab = ATOM + ' ' + residue + ' ' + atomi + ' ' + chain + ' ' + x + ' ' + y + ' ' + z
                        riga_virtual_tab = str(virtual_tab)
                        riga_virtual_tab += nuova_linea
                        tabella.write(riga_virtual_tab)
                        print(virtual_tab)
            tabella.close()



        #lista virtual_lab

        for riga2 in open("dataset"):
            lista2 = riga2.split()
            print(lista2)
            ATOM = lista2[0]
            residuo = lista2[1]
            tipo= lista2[2]
            catena = lista2[3]
            x = lista2[4]
            y = lista2[5]
            z = lista2[6]
            
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

        print(f"il numero dei carboni sono {C}")
        print(f"il numero degli azoto sono {N}")
        print(f"il numero degli ossigeni sono {O}")
        print(f"il numero degli idrogeni sono {H}")
        print(f"il numero degli zolfi sono {S}\n")

        print(f"la massa totale de carbonio {Cm_tot}")
        print(f"la massa totale dello zolfo {Nm_tot}")
        print(f"la massa totale dell'ossigeno {Om_tot}")
        print(f"la massa totale dello zolfo {Sm_tot}")

        if H == 0:
            print(f"la massa totale dell'idrogeno non è disponibile, in quanto essi sono assenti e bisogna aggiungerli")
        else:
            print(f"la massa totale degli idrogeni è {Hm_tot}") 

        #calcolo centro di massa della proteina

        massa_tot = Cm_tot + Nm_tot + Om_tot + Sm_tot    
        for riga in open('dataset'):
            if "C" == tipo:
                MixRi_x = float(Cm) * float(x)
                MixRi_y = float(Cm) * float(y)
                MixRi_z = float(Cm) * float(z)
                massa_x = massa_x + MixRi_x
                massa_y = massa_y + MixRi_y
                massa_z = massa_z + MixRi_z
            elif "N" == tipo:
                MixRi_x = float(Nm) * float(x)
                MixRi_y = float(Nm) * float(y)
                MixRi_z = float(Nm) * float(z)
                massa_x = massa_x + MixRi_x
                massa_y = massa_y + MixRi_y
                massa_z = massa_z + MixRi_z
            elif "O" == tipo:
                MixRi_x = float(Om) * float(x)
                MixRi_y = float(Om) * float(y)
                MixRi_z = float(Om) * float(z)
                massa_x = massa_x + MixRi_x
                massa_y = massa_y + MixRi_y
                massa_z = massa_z + MixRi_z
            elif "S" == tipo:
                MixRi_x = float(Sm) * float(x)
                MixRi_y = float(Sm) * float(y)
                MixRi_z = float(Sm) * float(z)
                massa_x = massa_x + MixRi_x
                massa_y = massa_y + MixRi_y
                massa_z = massa_z + MixRi_z
        risultato_x = massa_x // massa_tot
        risultato_y = massa_y // massa_tot
        risultato_z = massa_z // massa_tot

        print(risultato_x)
        print(risultato_y)
        print(risultato_z)

        #calcolo centro geometrico







if __name__ == "__main__":
    MyFrame().mainloop()