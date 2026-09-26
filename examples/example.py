import numpy as np
from gequbit_rabi.core import rabi_probability, pi_pulse_time

omega=2*np.pi*5e6
tpi=pi_pulse_time(omega)
print("pi pulse [ns]:",tpi*1e9)
print("excited-state probability:",rabi_probability(tpi,omega))
