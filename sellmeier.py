import math as m

class sellmeier:
  def getN (self, luz):
    # A luz é recebida em \micro
    # Coeficientes para o BK7
    a1 = 1.03961212
    a2 = 0.231792344
    a3 = 1.01046945
    b1 = 6.00069867*pow(10, -3)
    b2 = 2.00179144*pow(10, -2)
    b3 = 1.03560653*pow(10, 2)
    p1 = a1*(pow(luz, 2)/(pow(luz, 2) - b1))
    p2 = a2*(pow(luz, 2)/(pow(luz, 2) - b2))
    p3 = a3*(pow(luz, 2)/(pow(luz, 2) - b3))
    return m.sqrt(1+p1+p2+p3)
