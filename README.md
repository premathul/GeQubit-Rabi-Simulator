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

## Contact

**Athul Prem**

For scientific discussion, collaboration, or suggestions related to this project, please contact Athul Prem through the GitHub account associated with this repository.
