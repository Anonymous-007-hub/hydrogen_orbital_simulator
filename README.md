# Hydrogen Orbital Simulator

A Python-based simulator for visualizing hydrogen atom orbitals using quantum mechanics. This project solves the Schrödinger equation to compute the wave functions of hydrogen orbitals and generates interactive 3D plots of the probability densities.

## Features

- **Wave Function Computation**: Implements the mathematical functions for hydrogen orbitals, including associated Legendre polynomials, Laguerre polynomials, and spherical harmonics.
- **3D Visualization**: Uses Matplotlib to create 3D surface plots of orbital shapes.
- **Three Simulator Scripts**:
  - `simulator_without_sign.py`: Plots the absolute value of the hydrogen orbital wave function (probability density).
  - `simulator_with_sign.py`: Plots the signed hydrogen orbital wave function with positive and negative regions in different colors.
  - `spherical_harmonics_simulator.py`: Visualizes the angular part of the wave function (spherical harmonics Y_lm) for given l and m.
- **Interactive Input**: Prompts for quantum numbers n, l, and m (or l and m for spherical harmonics).
- **Quantum Number Validation**: Ensures valid inputs according to quantum mechanics rules.

## Requirements

- Python 3.6 or higher
- NumPy
- Matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Anonymous-007-hub/hydrogen_orbital_simulator.git
   cd hydrogen_orbital_simulator
   ```

2. Install the required packages:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

Run one of the simulator scripts:

```bash
python simulator_without_sign.py
# or
python simulator_with_sign.py
# or
python spherical_harmonics_simulator.py
```

For the orbital simulators (`simulator_without_sign.py` and `simulator_with_sign.py`), enter the quantum numbers:
- **n** (principal quantum number): Positive integer (1, 2, 3, ...)
- **l** (azimuthal quantum number): Integer from 0 to n-1
- **m** (magnetic quantum number): Integer from -l to +l

For the spherical harmonics simulator (`spherical_harmonics_simulator.py`), enter:
- **l** (azimuthal quantum number): Non-negative integer (0, 1, 2, ...)
- **m** (magnetic quantum number): Integer from -l to +l

### Examples

- **1s orbital**: n=1, l=0, m=0
- **2p orbital**: n=2, l=1, m=0 (or m=±1 for different orientations)
- **3d orbital**: n=3, l=2, m=0 (or m=±1, ±2)

The script will generate a 3D plot showing the orbital shape.

## Physics Background

Hydrogen orbitals are described by the quantum numbers:
- **n**: Determines the energy level and average distance from the nucleus
- **l**: Determines the orbital shape (s: l=0, p: l=1, d: l=2, etc.)
- **m**: Determines the orientation in space

The wave function ψ_{n,l,m}(r,θ,φ) = R_{n,l}(r) × Y_{l,m}(θ,φ), where R is the radial part and Y are the spherical harmonics.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is open-source. Feel free to use and modify as needed.
