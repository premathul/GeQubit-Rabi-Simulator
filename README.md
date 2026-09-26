# GeQubit-Rabi-Simulator

GeQubit-Rabi-Simulator is a compact research framework for modeling coherent driven dynamics of semiconductor spin qubits, with particular emphasis on Ge/SiGe hole-spin systems. The project is intended to connect experimentally controlled microwave or electric-drive parameters to time-domain qubit observables such as Rabi oscillations, pulse fidelity, detuning sensitivity, and noise-induced contrast decay.

In the rotating-wave approximation, a driven two-level system can be represented by an effective Hamiltonian with detuning Delta and on-resonance Rabi angular frequency Omega. Starting from the lower state, the ideal excited-state probability is

P(t) = [Omega^2/(Omega^2 + Delta^2)] sin^2[sqrt(Omega^2 + Delta^2)t/2].

This equation provides the basic reference model implemented in the current code. On resonance, a pi pulse has duration pi/Omega and ideally transfers the complete population to the opposite state.

Real experiments show reduced contrast because the qubit frequency, drive amplitude, or control phase fluctuates from shot to shot and during the pulse. The present repository therefore includes ideal Rabi dynamics, phenomenological exponential and Gaussian contrast envelopes, pulse-area utilities, and ensemble averaging over quasistatic detuning distributions. This makes it possible to compare an ideal coherent pulse with a noisy ensemble without requiring a full density-matrix simulation at the first stage.

Installation is performed with

\`\`\`bash
git clone https://github.com/premathul/GeQubit-Rabi-Simulator.git
cd GeQubit-Rabi-Simulator
python -m pip install -e .
\`\`\`

The long-term development plan is to add amplitude noise, pulse shaping, arbitrary phase control, Bloch-sphere trajectories, Lindblad relaxation and dephasing, randomized pulse errors, and optimization of pi and pi/2 gates under experimentally realistic noise. The project is intended to interoperate with QuantumDot-Noise-Lab for frequency-domain noise models and GeQubit-SweetSpot-Finder for operating-point optimization.

## Runnable scientific baseline

For a constant drive in the rotating-wave approximation, the generalized angular frequency is √(Ω² + Δ²), with Ω and Δ obtained by multiplying the supplied frequencies in hertz by 2π. Starting in the lower state, the ideal excitation probability is (Ω²/(Ω²+Δ²)) sin²(√(Ω²+Δ²)t/2). The program applies a phenomenological exponential decay to the oscillatory cosine while preserving the reduced detuned oscillation amplitude. This envelope is a modeling choice, not a derivation of a specific microscopic noise spectrum.

Run `python src/main.py --rabi-mhz 1 --detuning-mhz 0.1 --contrast-us 100 --end-us 5 --points 101 > trace.csv`. Each output row contains time in microseconds and excitation probability. The trace can test pulse-duration choices, but extracting fidelity from real data requires preparation and measurement error, drive calibration, leakage, pulse shape, and a noise model consistent with the experimental protocol. A fitted Rabi contrast time should never be silently substituted for Ramsey T₂* or relaxation T₁.

## Validation and scope

The calculations in `src/main.py` are transparent baseline models intended for reproducibility and extension. Inputs and assumptions should be reported alongside outputs; numerical agreement with a plotted trace alone does not validate a material-specific prediction. New physical terms should be accompanied by dimensional checks and independent limiting-case comparisons.

## Contact

**Athul Prem** — [GitHub profile](https://github.com/premathul). For scientific discussion or collaboration, open an issue in this repository or reach out through my GitHub profile.
