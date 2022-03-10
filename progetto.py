#!/usr/bin/python
import os

def decor1():
	print('=' * 20)


def decor2():
	print('-' * 20)

newline = '\n'


#Variabili massa atomica, conta atomi, coordinate

C = 12.0107
N = 14.0067
O = 15.999
H = 1.00784
S = 32.065

conta_TOT = 0
conta_C = 0
conta_N = 0
conta_O = 0
conta_S = 0

x_geom = 0
y_geom = 0
z_geom = 0

x_massa = 0
y_massa = 0
z_massa = 0


#argomenti inseribili: file.pdb, nome progetto, massa molecolare, centro geometrico, centro di massa


decor1()
s = input('Inserire path file .pdb: ')
decor1()
b = input('Inserire nome lavoro: ')
decor1()
massa = input('Eseguire calcolo della massa molecolare? (y/n)')
decor1()
centro_geom = input('Eseguire calcolo del centro geometrico? (y/n)')
decor1()
centro_mass = input('Eseguire calcolo del centro di massa? (y/n)')
decor1()
write_COM = input('Salvare il Centro di Massa come eteroatomo di nome COM in un nuovo file .pdb? (y/n)')
decor1()

for i in range(10):
	print('O')




tabella = open('dataset', 'w+')


#Crea dataset se il formato è valido

try:
	for line in open(s):
		list = line.split()
		id = list[0]
		if id == 'ATOM':
			residue = list[3]
			if len(residue) == 3:
				tipo = list[-1] #esempio atomo 626
				chain = list[4] #indica la catena della proteina posta nella 4 riga
				if chain == 'A':
					x = list[6]
					y = list[7]
					z = list[8]
					templato = id + ' ' + residue + ' ' + tipo + ' ' + chain + ' ' + x + ' ' + y + ' ' + z
					row = str(templato)
					row += newline
					tabella.write(row)
	tabella.close()
except:
	print('Formato o percorso file non validi!')
	exit()


#Lista componenti dataset:

for line in open('dataset'):
		list = line.split()
		id = list[0]
		residuo = list[1]
		tipo = list[2]
		catena = list[3]
		x = list[4]
		y = list[5]
		z = list[6]



#Calcola quantità C, N, O, S


for line in open('dataset'):
	list = line.split()
	tipo = list[2]
	if 'C' in tipo:
		conta_C += 1
	elif 'N'in tipo:
		conta_N += 1
	elif 'O' in tipo:
		conta_O += 1
	elif 'S' in tipo:
		conta_S += 1
	conta_TOT += 1


#Funzione calcolo Massa Molecolare della Proteina
#Gli atomi di idrogeno vengono stimati come 50% degli atomi totali (Elias, M., Liebschner, D., Koepke, J. et al. Hydrogen atoms in protein structures: high-resolution X-ray diffraction structure of the DFPase. BMC Res Notes 6, 308 (2013) doi:10.1186/1756-0500-6-308)



if massa == 'y': #y sta per yes dato in input!
	peso= (conta_C * C) + (conta_N * N) + (conta_O * O) + (conta_S * S) + (conta_TOT * H)
	decor1()
	print('Massa Molecolare ', b, ':')
	decor2()
	print(round(peso, 3), 'u')
	decor1()



#Funzione calcolo Centro Geometrico della Proteina


if centro_geom == 'y':	
	for line in open('dataset'):
		if 'C' in tipo:
			coord_x_massa = float(x) * float(C)
			x_geom = x_geom + coord_x_massa
			coord_y_massa = float(y) * float(C)
			y_geom = y_geom + coord_y_massa
			coord_z_massa = float(z) * float(C)
			z_geom = z_geom + coord_z_massa
			print(x)
		elif 'N'in tipo:
			coord_x_massa = float(x) * float(N)
			x_geom = x_geom + coord_x_massa
			coord_y_massa = float(y) * float(N)
			y_geom = y_geom + coord_y_massa
			coord_z_massa = float(z) * float(N)
			z_geom = z_geom + coord_z_massa
		elif 'O' in tipo:
			coord_x_massa = float(x) * float(O)
			x_geom = x_geom + coord_x_massa
			coord_y_massa = float(y) * float(O)
			y_geom = y_geom + coord_y_massa
			coord_z_massa = float(z) * float(O)
			z_geom = z_geom + coord_z_massa
		elif 'S' in tipo:
			coord_x_massa = float(x) * float(S)
			x_geom = x_geom + coord_x_massa
			coord_y_massa = float(y) * float(S)
			y_geom = y_geom + coord_y_massa
			coord_z_massa = float(z) * float(S)
			z_geom = z_geom + coord_z_massa
	valore_finale_x = x_geom // conta_TOT
	valore_finale_y = y_geom // conta_TOT
	valore_finale_z = z_geom // conta_TOT
	print('Coordinate centro geometrico ', b, ':')
	decor2()
	print('x: ', valore_finale_x)
	print('y: ', valore_finale_y)
	print('z: ', valore_finale_z)
	decor1()


#Funzione calcolo Centro di Massa Proteina

if centro_mass == 'y':
	massa_tot = (conta_C * C) + (conta_N * N) + (conta_O * O) + (conta_S * S)
	for line in open('dataset'):
		if tipo == 'C':
			coord_x_massa = float(x) * float(C)
			x_massa = x_massa + coord_x_massa
			coord_y_massa = float(y) * float(C)
			y_massa = y_massa + coord_y_massa
			coord_z_massa = float(z) * float(C)
			z_massa = z_massa + coord_z_massa
		elif tipo == 'N':
			coord_x_massa = float(x) * float(N)
			x_massa = x_massa + coord_x_massa
			coord_y_massa = float(y) * float(N)
			y_massa = y_massa + coord_y_massa
			coord_z_massa = float(z) * float(N)
			z_massa = z_massa + coord_z_massa
		elif tipo == 'O':
			coord_x_massa = float(x) * float(O)
			x_massa = x_massa + coord_x_massa
			coord_y_massa = float(y) * float(O)
			y_massa = y_massa + coord_y_massa
			coord_z_massa = float(z) * float(O)
			z_massa = z_massa + coord_z_massa
		elif tipo == 'S':
			coord_x_massa = float(x) * float(S)
			x_massa = x_massa + coord_x_massa
			coord_y_massa = float(y) * float(S)
			y_massa = y_massa + coord_y_massa
			coord_z_massa = float(z) * float(S)
			z_massa = z_massa + coord_z_massa
	valore_finale_x = x_massa // massa_tot
	valore_finale_y = y_massa // massa_tot
	valore_finale_z = z_massa // massa_tot
	print('Coordinate centro di massa ', b, ':')
	decor2()
	print('x: ', valore_finale_x)
	print('y: ', valore_finale_y)
	print('z: ', valore_finale_z)
	decor1()


#Salvataggio file .pdb con Centro di Massa come eteroatomo

if write_COM == 'y':
	dest = s[:-4] + '_COM.pdb'
	lines = open(s).read().splitlines()
	lines[-3] = str('HETATM 99999 C   COM A9999      ' + str(valore_finale_x) + ' ' + str(valore_finale_y) + ' ' + str(valore_finale_z) + ' 0.00 00.00          C')
	open(dest, 'w').write('\n'.join(lines))
	print('Nuovo file:')
	decor2()
	print(dest)
	decor1()

os.remove("dataset")
