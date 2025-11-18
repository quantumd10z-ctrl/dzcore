import math

def fractal_spiral(n_points=200, scale=1.0):
    """
    Genera una espiral nodal conceptual basada en la estructura TTA-D10Z.
    """
    coords = []
    for i in range(n_points):
        angle = i * 0.25
        radius = math.log(i + 1) * scale
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        coords.append((x, y))
    return coords
