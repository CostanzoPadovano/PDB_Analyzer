#LIBRERIA PER ANALIZZATORE PDB
nuova_linea = '\n'
#creare dataset     
def PDBcalc(filename,tabella):
    
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


def PESOMOLECOLARE(filename):
    MW = 0

    A = 0
    C = 0
    D = 0
    E = 0
    F = 0
    G = 0
    H = 0
    I = 0
    K = 0
    L = 0
    M = 0
    N = 0
    P = 0
    Q = 0
    R = 0
    S = 0
    T = 0
    V = 0
    W = 0
    Y = 0
    MSel = 0

#massa molecolare degli aminoacidi
    ALA = 71.08
    CYS = 103.14
    ASP = 115.09
    GLU = 129.12
    PHE = 147.18
    GLY = 57.06
    HIS= 137.15
    ILE = 113.17
    LYS = 128.18
    LEU = 113.17
    MET = 131.21
    ASN = 114.11
    PRO = 97.12
    GLN = 128.41
    ARG = 156.20
    SER = 87.08
    THR = 101.11
    VAL = 99.14
    TRP = 186.21 
    TYR = 163.18
    MSE = 196.106
    with open(filename, "r") as files:
        for riga in files:
            lista1 = riga.split()
            if lista1[0] == "SEQRES":
                A += riga.count("ALA")
                C += riga.count("CYS")
                D += riga.count("ASP")
                E += riga.count("GLU")
                F += riga.count("PHE")
                G += riga.count("GLY")
                H += riga.count("HIS")
                I += riga.count("ILE")
                K += riga.count("LYS")
                L = riga.count("LEU")
                M = riga.count("MET")
                N = riga.count("ASN")
                P = riga.count("PRO")
                Q = riga.count("GLN")
                R = riga.count("ARG")
                S = riga.count("SER")
                T = riga.count("THR")
                V = riga.count("VAL")
                W = riga.count("TRP")
                Y = riga.count("TYR")
                MSel = riga.count("MSE")
    
    MW = A*ALA+C*CYS+D*ASP+E*GLU+F*PHE+G*GLY+H*HIS+I*ILE+K*LYS+L*LEU+M*MET+N*ASN+P*PRO+Q*GLN+R*ARG+S*SER+T*THR+V*VAL+W*TRP+Y*TYR+MSel*MSE
    print(f"{MW} g/mol calcolato cone le masse degli aminoacidi")
                    

