import numpy as np
import matplotlib.pyplot as plt
import sigen as si
import timeit

def create_material (file_name, lattice, atom, nx, ny, nz, charge):

	if lattice == 'diamond':
		if atom == 'si':
			start = timeit.default_timer()
			si.sigen(file_name, nx, ny, nz, charge)
			stop = timeit.default_timer()
			print('Time: ', stop - start) 
	else: 
		print('No lattice found')
