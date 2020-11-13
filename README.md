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

This python file solves the continuity and Euler equations for a slight gaussian perturbation in density and velocity. After we give a perturbation, the gaussian wave splits into a left and right wave. After the left and right waves reflect off the boundaries (we assumed reflective BCs), and if the initial perturbation was large enough, the waves start to steepen and take on the form of the shocks. As they continue to reflect, they steepen further (i.e. smaller width, larger amplitude, discontinous). As derived in class, shock widths are set by two factors: viscosity and velocity. The shock width ~ mu (viscosity) / u (velocity). Thus, if we increase our velocity, we decrease our shock width. In our analysis, we first test perturbations to rho and then test perturbations to rho and u. In both cases, as we increase the amplitude of the perturbation (and thus increase rho and u), the perturbation leads to a stronger shock. There is also a sort of "numerical" viscosity contained within the advection, but we cannot adjust it and so it is not one the factors we can change for the shock width. 

Collaborators:
Sabrina Berger,
Constanza Echibura,
Capucine Barfety,
Alexandre Adam
