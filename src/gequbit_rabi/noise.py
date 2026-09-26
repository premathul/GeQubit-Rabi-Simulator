import numpy as np
from .core import rabi_probability

def gaussian_envelope(t_s, T_s):
    if T_s<=0: raise ValueError("T_s must be positive")
    t=np.asarray(t_s,float)
    return np.exp(-(t/T_s)**2)

def exponential_envelope(t_s, T_s):
    if T_s<=0: raise ValueError("T_s must be positive")
    return np.exp(-np.asarray(t_s,float)/T_s)

def quasistatic_detuning_average(t_s, omega_rad_s, sigma_detuning_rad_s, n_samples=2001):
    if sigma_detuning_rad_s<0 or n_samples<3:
        raise ValueError("invalid sigma or sample count")
    if sigma_detuning_rad_s==0:
        return rabi_probability(t_s,omega_rad_s,0.0)
    det=np.linspace(-5*sigma_detuning_rad_s,5*sigma_detuning_rad_s,n_samples)
    w=np.exp(-0.5*(det/sigma_detuning_rad_s)**2)
    w/=np.trapezoid(w,det)
    probs=np.array([rabi_probability(t_s,omega_rad_s,d) for d in det])
    return np.trapezoid(probs*w[:,None],det,axis=0)
