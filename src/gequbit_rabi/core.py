import numpy as np

def rabi_probability(t_s, omega_rad_s, detuning_rad_s=0.0):
    t=np.asarray(t_s,float)
    if omega_rad_s < 0:
        raise ValueError("omega must be nonnegative")
    generalized=np.sqrt(omega_rad_s**2+detuning_rad_s**2)
    if generalized==0:
        return np.zeros_like(t)
    contrast=omega_rad_s**2/generalized**2
    return contrast*np.sin(0.5*generalized*t)**2

def pi_pulse_time(omega_rad_s):
    if omega_rad_s<=0:
        raise ValueError("omega must be positive")
    return np.pi/omega_rad_s

def pulse_area(omega_rad_s, duration_s):
    if duration_s<0:
        raise ValueError("duration must be nonnegative")
    return omega_rad_s*duration_s

def apply_contrast_envelope(probability, envelope):
    p=np.asarray(probability,float); e=np.asarray(envelope,float)
    return 0.5+(p-0.5)*e
