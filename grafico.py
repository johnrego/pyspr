import matplotlib.pyplot as plt

class grafico:
  def __init__ (self, nome):
    f = open(nome, 'r')
    cont = f.readlines()
    f.close()
    ang = []
    val = []
    for linha in cont:
      a = linha.replace('\n','')
      a = a.split(',')
      ang.append(float(a[0]))
      val.append(float(a[1]))
    plt.plot(ang, val)
    plt.show()
