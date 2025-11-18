"""
D10Z Core Framework
===================

Paquete oficial del ecosistema TTA–D10Z.

Proporciona:
- Motor matemático nodal (TTA Engine)
- Funciones de estabilidad (Zₙ-core)
- Visualizaciones fractales (Nodal Maps)
- Herramientas de análisis conceptual (Homo Fractalis Toolkit)
- Manifesto integrado (versión liviana)

Este módulo NO ejecuta código oculto ni procesos automatizados.
Todo lo relacionado a inicialización se hace explícitamente con:

    >>> import d10z
    >>> d10z.init()

©2025 Jamil Al Thani — D10Z Institute
"""

__version__ = "1.0.0"
__author__ = "Jamil Al Thani"
__license__ = "Apache-2.0"

# ------------------------------------------------------------
#  Núcleo del sistema — valor universal Zₙ
# ------------------------------------------------------------

Z_N = 1e-51  # Constante nodal universal TTA–D10Z


# ------------------------------------------------------------
#  Motor Matemático (mínimo operativo)
# ------------------------------------------------------------

def nodal_energy(x, f=1.0, v=1.0):
    """
    Calcula la energía nodal según la ecuación TTA-D10Z:

        E_x = f * sqrt(v * ln(x / Z_n))

    Parámetros:
        x (float): valor medido o intensidad nodal
        f (float): fuerza nodal
        v (float): velocidad nodal

    Retorna:
        float: energía nodal E_x
    """
    import math

    if x <= 0:
        return 0.0

    try:
        return f * math.sqrt(v * math.log(x / Z_N))
    except ValueError:
        return 0.0


# ------------------------------------------------------------
#  Inicialización simbólica (ritual no-executable)
# ------------------------------------------------------------

def init():
    """
    Ritual simbólico de inicialización D10Z.
    No ejecuta procesos del sistema.
    Solo imprime un banner conceptual.

    Ejemplo:
        >>> import d10z
        >>> d10z.init()
    """
    banner = r"""
============================================
    D10Z CORE – NODAL INITIALIZATION
============================================
Estado: OK
Constante universal Zₙ: 1e-51
Motor TTA: listo
Homo Fractalis Toolkit: preparado
============================================
    "La coherencia no se instala. Se activa."
============================================
    """
    print(banner)


# ------------------------------------------------------------
#  Exportaciones públicas
# ------------------------------------------------------------

__all__ = [
    "Z_N",
    "nodal_energy",
    "init",
]
