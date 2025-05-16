import numpy as np

def calc_surface_tension_guggenheim(gamma_list, x_list):
    assert len(gamma_list) == len(x_list)
    assert np.isclose(sum(x_list), 1.0), "Jumlah fraksi molar harus = 1"
    
    ln_gamma_mix = sum(x * np.log(gamma) for x, gamma in zip(x_list, gamma_list))
    gamma_mix = np.exp(ln_gamma_mix)
    return gamma_mix

# Contoh data
gamma_list = [29.3, 29.0, 72.8]  # ACN, TEA, Water (mN/m)
x_list = [0.5, 0.3, 0.2]         # Fraksi molar

gamma_mix = calc_surface_tension_guggenheim(gamma_list, x_list)
print(f"Surface tension (Guggenheim–Katayama): {gamma_mix:.2f} mN/m")
