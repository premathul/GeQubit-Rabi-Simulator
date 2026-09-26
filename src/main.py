"""Analytic rotating-wave two-level dynamics with phenomenological contrast decay."""
import argparse
import math

def excited_probability(time_s, rabi_hz, detuning_hz=0., contrast_time_s=math.inf):
    if time_s < 0 or rabi_hz < 0 or contrast_time_s <= 0:
        raise ValueError("Invalid time, drive, or envelope")
    omega = 2*math.pi*rabi_hz
    delta = 2*math.pi*detuning_hz
    effective = math.hypot(omega,delta)
    if effective == 0: return 0.
    return 0.5*(omega/effective)**2*(1-math.exp(-time_s/contrast_time_s)*math.cos(effective*time_s))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rabi-mhz",type=float,default=1.)
    p.add_argument("--detuning-mhz",type=float,default=0.)
    p.add_argument("--contrast-us",type=float,default=100.)
    p.add_argument("--end-us",type=float,default=5.)
    p.add_argument("--points",type=int,default=101)
    args=p.parse_args()
    if args.points < 2 or args.end_us < 0: raise ValueError("Need >=2 points and end >=0")
    print("time_us,p_excited")
    for i in range(args.points):
        t=args.end_us*1e-6*i/(args.points-1)
        prob=excited_probability(t,args.rabi_mhz*1e6,args.detuning_mhz*1e6,args.contrast_us*1e-6)
        print(f"{t*1e6:.9g},{prob:.9g}")
if __name__=="__main__": main()
