import math

def venturi_discharge(d1, d2, h, Cd=0.98, g=9.81):
    """
    Calculate discharge through a venturimeter.
    
    Parameters:
    d1 : float - diameter of main pipe (m)
    d2 : float - diameter of throat (m)
    h : float - manometric head difference (m)
    Cd : float - coefficient of discharge (default=0.98)
    g : float - gravitational acceleration (m/s^2)
    """
    A1 = math.pi * (d1**2) / 4
    A2 = math.pi * (d2**2) / 4
    Q = Cd * A2 * math.sqrt(2 * g * h / ((A1/A2)**2 - 1))
    return Q  # m^3/s

# Example input
d1 = 0.1   # 10 cm
d2 = 0.05  # 5 cm
h = 0.2    # 20 cm head difference

Q = venturi_discharge(d1, d2, h)
print(f"Discharge through venturimeter = {Q:.6f} m³/s")
