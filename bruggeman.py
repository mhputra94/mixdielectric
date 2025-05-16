import numpy as np
from scipy.optimize import fsolve

def bruggeman_equation(eps_mix, eps_list, phi_list):
    # Fungsi utama persamaan Bruggeman untuk N komponen
    return sum([
        phi * (eps - eps_mix) / (eps + 2 * eps_mix)
        for eps, phi in zip(eps_list, phi_list)
    ])

def calc_eps_mix_bruggeman(eps_list, phi_list, guess=10.0):
    # Pastikan panjang list sama dan total fraksi = 1
    assert len(eps_list) == len(phi_list), "Panjang eps dan phi harus sama"
    assert np.isclose(sum(phi_list), 1.0), "Jumlah phi harus 1.0"
    
    # Gunakan fsolve untuk menyelesaikan persamaan nonlinear
    solution = fsolve(bruggeman_equation, x0=guess, args=(eps_list, phi_list))
    return solution[0]

# === Contoh penggunaan ===
# Data contoh:
# TEA: eps = 2.4, volume fraction = 0.3
# Water: eps = 78.4, volume fraction = 0.1
# ACN: eps = 37.5, volume fraction = 0.6

eps_list = [2.4, 78.4, 37.5]
phi_list = [0.3, 0.1, 0.6]

eps_mix = calc_eps_mix_bruggeman(eps_list, phi_list)
print(f"Dielectric constant (Bruggeman model): {eps_mix:.4f}")
