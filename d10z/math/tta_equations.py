"""
Módulo matemático oficial D10Z
Ecuaciones TTA, Sahana, Isis, GM 10^-51 y nodal curves.
"""

import numpy as np

Z = 1e-51  # Z_n estándar
f = 1      # normalización nodal base

def sahana(r):
    """Ley Sahana — estabilización inicial del nodo."""
    return np.log(1 + Z * r)

def isis(r):
    """Ley Isis — formación nodal."""
    return np.sqrt(np.log(r / Z))

def efficiency_codon(f_real, f_exp=1/61, Z_n=Z):
    """Ecuación nodal del codón."""
    return np.sqrt(np.log(f_real / (f_exp * Z_n)))

def tta_curve(r, GM=1, r0=1, alpha=0.042):
    """Curva TTA universal."""
    term1 = np.sqrt(GM / r)
    term2 = np.sqrt((r/r0)**(-0.5) * (1 + alpha*np.log(r/r0)))
    return term1 * term2

def nodal_stability(r):
    return sahana(r) * isis(r)
