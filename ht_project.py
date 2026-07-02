import numpy as np

def calculate_aeroplane_cooling():
    print("AEROPLANE COOLING SYSTEM PERFORMANCE ANALYZER")

    try:
        T1 = float(input("Enter Bleed Air Inlet Temp (T1) in K: "))
        rp = float(input("Enter Pressure Ratio (rp): "))
        eta_c = float(input("Enter Compressor Efficiency (nc): "))
        eta_t = float(input("Enter Turbine Efficiency (nt): "))
        epsilon = float(input("Enter Heat Exchanger Effectiveness (eps): "))
        Tcabin = float(input("Enter Cabin Target Temperature in K: "))
        
        Tram_std = float(input("Enter Baseline Ambient RAM Air Temp in K: "))
        Tram_imp = float(input("Enter Improved RAM Air Temp in K: "))
        
        cp = 1.005  
        gamma = 1.4  
    
        def run_cycle_analysis(Tram):
            # Process 1-2
            T2s = T1 * (rp**((gamma - 1) / gamma))
            T2 = T1 + (T2s - T1) / eta_c
            Wc = cp * (T2 - T1)
            
            # Process 2-3
            T3 = T2 - epsilon * (T2 - Tram)
            
            # Process 3-4
            T4s = T3 / (rp**((gamma - 1) / gamma))
            T4 = T3 - eta_t * (T3 - T4s)
            Wt = cp * (T3 - T4)
            
            # Performance Metrics
            Wnet = Wc - Wt
            Qin = cp * (Tcabin - T4)
            COP = Qin / Wnet
            return {"T2": T2, "T3": T3, "T4": T4, "Qin": Qin, "Wnet": Wnet, "COP": COP}

        std = run_cycle_analysis(Tram_std)
        imp = run_cycle_analysis(Tram_imp)

        print("\n" + "="*55)
        print(f"{'METRIC':<25} | {'BASELINE':<12} | {'HYBRID'}")
        print("-" * 55)
        print(f"{'Comp. Outlet (T2)':<25} | {std['T2']:>10.1f} K | {imp['T2']:>10.1f} K")
        print(f"{'HX Outlet (T3)':<25} | {std['T3']:>10.1f} K | {imp['T3']:>10.1f} K")
        print(f"{'Turbine Outlet (T4)':<25} | {std['T4']:>10.1f} K | {imp['T4']:>10.1f} K")
        print(f"{'Cooling Effect (Qin)':<25} | {std['Qin']:>10.2f} | {imp['Qin']:>10.2f}")
        print(f"{'System COP':<25} | {std['COP']:>10.3f} | {imp['COP']:>10.3f}")
        
        # Improvement Calculation [cite: 31, 32]
        improvement = ((imp['COP'] - std['COP']) / std['COP']) * 100
        print("-" * 55)
        print(f"TOTAL COP IMPROVEMENT: {improvement:.2f}%")
        print("="*55)

    except ValueError:
        print("\nERROR: enter only numerical values.")

if __name__ == "__main__":
    calculate_aeroplane_cooling()
