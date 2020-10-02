import math as m
import numpy as np

class kretschmann:
  def __init__ (self, indPris, luz, camadas):
    self.indPris = indPris
    self.luz = luz
    self.camadas = camadas
  
  def getBj (self, nCam, ang):
    k0 = ((2*m.pi)/self.luz)
    nj = self.camadas[nCam][0]
    dj = self.camadas[nCam][1]
    return k0*dj*m.sqrt(abs(pow(nj, 2)-pow(self.indPris*m.sin(ang), 2)))

  def getQj (self, nCam, ang):
    nj = self.camadas[nCam][0]
    return m.sqrt(abs(pow(nj, 2)-pow(self.indPris*m.sin(ang), 2)))/pow(nj, 2)

  def getMj (self, nCam, ang):
    return np.array([
      (m.cos(self.getBj(nCam, ang)), m.sin(self.getBj(nCam, ang))*(-complex(0,1)/self.getQj(nCam, ang))),
      (-complex(0,1)*self.getQj(nCam, ang)*m.sin(self.getBj(nCam, ang)), m.cos(self.getBj(nCam, ang)))
    ])
  
  def getMtotal (self, ang):
    m = 1
    for a in range(len(self.camadas)):
      m = m * self.getMj(a, ang)
    return m
  


