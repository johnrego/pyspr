import math as m
import numpy as np

class kretschmann:
  def __init__ (self, luz, camadas, ang):
    self.luz = luz
    self.camadas = camadas
    self.ang = []
    self.ang.append(ang)
    for a in range(1, len(self.camadas)):
      try:
        theta = m.sqrt(1-abs(pow(self.camadas[a-1][0]/self.camadas[a][0], 2)*pow(m.sin(self.ang[0]), 2)))
      except ValueError:
        # theta = m.sqrt(abs(pow(self.camadas[a-1][0]/self.camadas[a][0], 2)*pow(m.sin(self.ang[0]), 2))-1)
        print (abs(pow(self.camadas[a-1][0]/self.camadas[a][0], 2)*pow(m.sin(self.ang[0]), 2)))
        exit ()
      self.ang.append(theta)
  
  def getBj (self, nCam):
    indPris = self.camadas[0][0]
    k0 = ((2*m.pi)/self.luz)
    nj = self.camadas[nCam][0]
    dj = self.camadas[nCam][1]
    return k0*dj*m.sqrt(abs(pow(nj, 2)-pow(indPris*m.sin(self.ang[nCam]), 2)))

  def getQj (self, nCam):
    indPris = self.camadas[0][0]
    nj = self.camadas[nCam][0]
    return m.sqrt(abs(pow(nj, 2)-pow(indPris*m.sin(self.ang[nCam]), 2)))/pow(nj, 2)

  def getMj (self, nCam):
    i = complex(0,1)
    bj = self.getBj(nCam)
    qj = self.getQj(nCam)
    return np.array([
      (m.cos(bj), m.sin(bj)*(-i/qj)),
      (-i*qj*m.sin(bj), m.cos(bj))
    ])
  
  def getMtotal (self):
    mat = 1
    for a in range(len(self.camadas)):
      mat = mat * self.getMj(a)
    return mat
  
  def refle (self):
    mat = self.getMtotal()
    q1 = self.getQj(0)
    qn = self.getQj(-1)
    a = (mat[0][0] + (mat[0][1]*qn))*q1
    b = mat[1][0] + (mat[1][1]*qn)
    r = (a-b)/(a+b)
    return pow(abs(r), 2)
  


