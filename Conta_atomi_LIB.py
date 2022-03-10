import os


#una funzione deve contenere tutte le informazioni. in sostanza è come se fosse una scatola con tante lettere(informazioni).
def Scatola():
    
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
    filename = input("importa il file: ")
    with open(filename,"r") as files:
        for riga in files:
            Lista = riga.split() 
            id1 = Lista[0]    
            id1 == "ATOM"
            if riga.count("ATOM"):
                if "C" == Lista[-1]:
                    C += 1
                    Cm_tot = C * Cm 
                elif "N" == Lista[-1]:
                    N += 1    
                    Nm_tot = N * Nm
                elif "O" == Lista[-1]:
                    O += 1       
                    Om_tot = O * Om  
                elif "H" == Lista[-1]:
                    H += 1   
                    Hm_tot = H * Hm                 
                elif "S" == Lista[-1]:
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







                


                


                
