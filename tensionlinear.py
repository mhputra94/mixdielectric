def calc_surface_tension_mix(gamma_list, phi_list):
    assert len(gamma_list) == len(phi_list)
    assert abs(sum(phi_list) - 1.0) < 1e-6, "Total phi harus = 1"

    gamma_mix = sum(g * phi for g, phi in zip(gamma_list, phi_list))
    return gamma_mix

# Data: TEA, water, ACN
gamma_list = [29.0, 72.8, 29.3]  # mN/m
phi_list = [0.3, 0.1, 0.6]

gamma_mix = calc_surface_tension_mix(gamma_list, phi_list)
print(f"Surface tension (linear mix): {gamma_mix:.2f} mN/m")
