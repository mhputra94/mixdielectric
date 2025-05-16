import numpy as np
from scipy.optimize import fsolve

def lorentz_lorenz_equation(n_mix, n_list, phi_list):
    # Konversi n_mix dari nilai float ke list agar bisa digunakan oleh fsolve
    n_mix = n_mix[0] if isinstance(n_mix, (list, np.ndarray)) else n_mix
    lhs = (n_mix**2 - 1) / (n_mix**2 + 2)
    rhs = sum([
        phi * (n**2 - 1) / (n**2 + 2)
        for n, phi in zip(n_list, phi_list)
    ])
    return lhs - rhs

def calc_n_mix_lorentz_lorenz(n_list, phi_list, guess=1.4):
    assert len(n_list) == len(phi_list), "Panjang list n dan phi harus sama"
    assert np.isclose(sum(phi_list), 1.0), "Jumlah phi harus 1.0"
    
    solution = fsolve(lorentz_lorenz_equation, x0=guess, args=(n_list, phi_list))
    return solution[0]

# === Contoh penggunaan ===
# TEA: n = 1.400, volume fraction = 0.3
# Water: n = 1.333, volume fraction = 0.1
# ACN: n = 1.344, volume fraction = 0.6

n_list = [1.400, 1.333, 1.344]
phi_list = [0.3, 0.1, 0.6]

n_mix = calc_n_mix_lorentz_lorenz(n_list, phi_list)
print(f"Refractive index (Lorentz–Lorenz model): {n_mix:.5f}")
