import numpy as np
from gequbit_rabi.core import rabi_probability, pi_pulse_time
from gequbit_rabi.noise import quasistatic_detuning_average

def test_pi_pulse():
    omega=2*np.pi*1e6
    t=pi_pulse_time(omega)
    assert np.isclose(rabi_probability(t,omega),1.0)

def test_zero_time():
    assert np.isclose(rabi_probability(0.0,1.0),0.0)

def test_zero_noise_average():
    t=np.linspace(0,1e-6,20)
    a=quasistatic_detuning_average(t,1e7,0)
    b=rabi_probability(t,1e7)
    assert np.allclose(a,b)
