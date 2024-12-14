import numpy as np
import matplotlib.pyplot as plt

# Constants
Hs = 6  # Significant wave height in meters
Tp = 10  # Peak period in seconds
gamma = 3.3  # Peak enhancement factor
g = 9.81  # Gravity (m/s^2)

# Derived parameters
fp = 1 / Tp  # Peak frequency in Hz
alpha = 0.076 * (Hs**2) / (Tp**4)  # Phillips constant

# Frequency range
f = np.linspace(0.01, 1.0, 1000)  # Frequency range (Hz)

# JONSWAP spectrum calculation
S = []
for fi in f:
    if fi <= fp:
        sigma = 0.07
    else:
        sigma = 0.09
    r = np.exp(-((fi - fp)**2) / (2 * (sigma**2) * (fp**2)))
    spectrum = alpha * g**2 * fi**-5 * np.exp(-1.25 * (fi / fp)**-4) * gamma**r
    S.append(spectrum)

S = np.array(S)

# Convert frequency to angular frequency (rad/s) and adjust spectral density
omega = 2 * np.pi * f
S_rad = S * 2 * np.pi  # Convert spectral density to m^2 s/rad

# Convert frequency to period (T = 1/f)
T = 1 / f

# Sort data for increasing period
T = T[::-1]
S_rad = S_rad[::-1]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(T, S_rad, label=f'JONSWAP Spectrum (Hs={Hs}m, Tp={Tp}s, γ={gamma})')
plt.xlim([0, 20])  # Match the period range from the reference plot
plt.ylim([0, 17000])  # Match the y-axis range from the reference plot
plt.xlabel('Period (s)')
plt.ylabel('Spectral Density (m$^2$s/rad)')
plt.legend(loc='upper right')
#plt.title('JONSWAP Wave Spectrum')
plt.grid(True)
plt.legend()
plt.show()
