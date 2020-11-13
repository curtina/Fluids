# Astrophysical Fluids
Alice P. Curtin
November 12, 2020
Python 3.6.11

This github repository contains three python files. The file names and short descriptions of each are listed below. 

1. Advection.py

This python file solves the advection equation using the FTCS and Lax-Friedrich methods. Note that the Lax-Friedrich method is stable while the FTCS is unstable.

2. AdvectionDiffusion.py

This python file solves the advection-diffusion equation using the Lax-Friedrich method for the advection and an implicit method for diffusion.

3. HydroSolver.py

This python file solves the continuity and Euler equations for a slight gaussian perturbation in density and velocity. If we give a large enough perturbation to the density, a shock will form. After the left and right parts of the wave reflect off their respective walls, the two wave starts to steepen. As the waves continue to reflect, they (along with their recombination) steepens further (ie the waves are no longer gaussians but instead discontinuities in the density that are propogating). Shock widths are set by two factors: viscosity and velocity. The shock width ~ mu (viscosity) / u (velocity). Thus, if we increase our velocity, we decrease our shock width. In our analysis, we first test perturbations to rho and then test perturbations to rho and u. In both cases, as we increase the amplitude of the perturbation, the shock steepends with its width decreasing. 

Collaborators:
Sabrina Berger,
Constanza Echibura,
Capucine Barfety,
Alexandre Adam
