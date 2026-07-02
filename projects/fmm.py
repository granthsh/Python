import math

# 1. Venturimeter (m³/s)
def venturi_discharge(d1, d2, h, Cd=0.98, g=9.81):
    A1 = math.pi * (d1**2) / 4
    A2 = math.pi * (d2**2) / 4
    Q = Cd * A1 * A2 * math.sqrt(2 * g * h / ((A1)**2 - (A2)**2))
    return Q 

# 2. Orifice Discharge (m³/s)
def orifice_discharge_d(Cd, d1, do, h):
    A1 = math.pi * (d1**2) / 4
    Ao = math.pi * (do**2) / 4
    Q = Cd * A1 * Ao * math.sqrt((2 * 9.81 * h) / ((A1**2) - (Ao**2)))
    return Q

# 3. Pipe Flow Head Loss (Darcy–Weisbach) (meter)
def head_loss(f, L, D, V, g=9.81):
    h_f = f * (L/D) * (V**2 / (2*g))
    return h_f 

# 4. Drip Irrigation Emitter Flow (Hagen–Poiseuille) (m³/s)
def emitter_flow(d, L, deltaP, mu):
    r = d / 2
    Q = (math.pi * r**4 * deltaP) / (8 * mu * L)
    return Q 


def main():
    print("===== Fluid Mechanics Irrigation Calculator =====")
    print("1. Venturimeter Discharge")
    print("2. Orifice Discharge")
    print("3. Pipe Flow Head Loss (Darcy–Weisbach)")
    print("4. Drip Irrigation Emitter Flow")
    choice = int(input("Select an option (1-4): "))

    if choice == 1:
        print("\n--- Venturimeter ---")
        d1 = float(input("Enter diameter at inlet (m): "))
        d2 = float(input("Enter diameter at throat (m): "))
        h = float(input("Enter manometric head difference (m): "))
        Cd = float(input("Enter coefficient of discharge (Cd, default 0.98): ") or 0.98)
        Q = venturi_discharge(d1, d2, h, Cd)
        print(f"\nDischarge through venturimeter = {Q:.6f} m³/s")

    elif choice == 2:
        print("\n--- Orifice ---")
        d1 = float(input("Enter diameter of tank/approach section (m): "))
        do = float(input("Enter diameter of orifice (m): "))
        h = float(input("Enter head (m): "))
        Cd = float(input("Enter coefficient of discharge (Cd): "))
        print(f"Discharge = {orifice_discharge_d(Cd, d1, do, h):.6f} m³/s")

    elif choice == 3:
        print("\n--- Pipe Flow (Darcy–Weisbach) ---")
        f = float(input("Enter friction factor (f): "))
        L = float(input("Enter length of pipe (m): "))
        D = float(input("Enter diameter of pipe (m): "))
        V = float(input("Enter mean velocity of flow (m/s): "))
        h_f = head_loss(f, L, D, V)
        print(f"\nHead loss due to friction = {h_f:.4f} m")

    elif choice == 4:
        print("\n--- Drip Irrigation Emitter ---")
        d = float(input("Enter diameter of emitter tube (m): "))
        L = float(input("Enter length of emitter tube (m): "))
        deltaP = float(input("Enter pressure difference (Pa): "))
        mu = float(input("Enter dynamic viscosity of water (Pa·s): "))
        Q = emitter_flow(d, L, deltaP, mu)
        print(f"\nFlow rate through emitter = {Q:.10f} m³/s")

    else:
        print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()
