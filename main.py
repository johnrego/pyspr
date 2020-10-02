import numpy as np
from kretschmann import kretschmann

print ('Simulador')
print ('')
print ('Escolha o tipo de configuracao:')
print ('1 - Kretschmann-Raether')
print ('2 - Turbadar-Otto')
conf = int(input(''))
nCam = int(input('Informe o numero de camadas: '))-1
luz = float(input('Informe o comprimento de luz incidente (nm): '))*pow(10, -9)
indPris = float(input('Informe o indice de refracao do prisma: '))
camadas = []
for a in range (nCam):
  print ('Informe o indice de refração da camada %d' % (a+2))
  real = float(input('Parte real: '))
  imag = float(input('Parte imaginaria: '))
  esp = float(input('Informe a espessura (nm): '))*pow(10, -9)
  camadas.append([complex(real, imag), esp])

for ang in np.arange(0, 1.5707, 0.001):
  teste = kretschmann(indPris, luz, camadas)
  print (teste.getMtotal(ang))
