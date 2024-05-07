import numpy as np
def raices_cuadratica(a,b,c):
    """
    Este programa encuentra las raíces de una ecuación cuadrática
        • Datos de entrada:
            ► [ a,b,c ] : Coeficientes de la fórmula: ax^2 + bx + c
        • Datos de salida:
            ► [ R1,R2 ] : Raices de la ecuación dada
    """
    D2 = ((b**2)-(4*a*c)) # Discriminante
    if D2 < 0:
        return "La ecuación no tiene raíces reales"
    else:
        D = np.sqrt(D2)
        R1 = ((-b) + D) /(2.0*a)
        R2 = ((-b) - D) /(2.0*a)
    
        return('las raices son: {:7.4f} y {:7.4f}' .format(R1, R2))