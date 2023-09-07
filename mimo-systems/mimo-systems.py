import numpy as np
import matplotlib.pyplot as plt

# System Parameters
Nt = 2  # Number of transmit antennas
Nr = 2  # Number of receive antennas
SNR_dB = 10  # Signal-to-Noise Ratio (in dB)

# Generate random transmit signal
Tx_signal = np.random.randint(2, size=(Nt, 1000))  # 1000 bits for each transmit antenna

# Channel Matrix
H = (1/np.sqrt(2)) * (np.random.randn(Nr, Nt) + 1j * np.random.randn(Nr, Nt))  # Complex Gaussian channel

# Noise Vector
SNR = 10**(SNR_dB/10)  # Convert SNR from dB to linear scale
noise_power = 1/SNR
noise = np.sqrt(noise_power/2) * (np.random.randn(Nr, 1000) + 1j * np.random.randn(Nr, 1000))  # Complex Gaussian noise

# Received Signal
Rx_signal = np.dot(H, Tx_signal) + noise

# Equalization
H_inverse = np.linalg.inv(H)
Eq_signal = np.dot(H_inverse, Rx_signal)

# Decoding
Rx_bits = np.real(Eq_signal) > 0.5  # Decision threshold of 0.5 for binary decoding

# Bit Error Rate (BER) calculation
error_bits = np.sum(Rx_bits != Tx_signal)
BER = error_bits / (Nt * 1000)

# Display Results
print('Bit Error Rate (BER):', BER)

# Plot Results
plt.plot(np.real(Rx_signal.flatten()), np.imag(Rx_signal.flatten()), 'r.', markersize=10)
plt.plot(np.real(Eq_signal.flatten()), np.imag(Eq_signal.flatten()), 'bo', markersize=5)
plt.legend(['Received Signal', 'Equalized Signal'])
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('MIMO System Simulation')
plt.show()
