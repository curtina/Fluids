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

This python file solves the continuity and Euler equations for a slight gaussian perturbation in density and velocity. If we give a large enough perturbation to the density, a shock will form. After the left and right parts of the wave reflect off their respective walls and again return to the center, the amplitude of the perturbation has increased and its width has decreased. As we increase the amplitude of the perturbation, the width of the shock wave decreases. Shock widths are set by two factors: viscosity and velocity. The shock width ~ mu (viscosity) / u (velocity). Thus, if we increase our velocity, we decrease our shock width. In our analysis, we test perturbing rho, and then perturbing rho and u. In both cases, as we increase the perturbation, we decrease the width of the shock and it steepens. 

Collaborators:
Sabrina Berger
Constanza Echiburu 
Capucine Barfety
