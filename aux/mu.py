import numpy as np

def compute_mu(filename):
	x_=[]
	y_=[]
	z_=[]

	with open(filename, "r") as file:
			#Reading the original File.
			count =0;
			for line_number,line in enumerate(file):
				#Taking the number of atoms for the Filename
				if line_number == 0:
					num_atoms_total = int(line)  #Will use num_atoms afterward.
				
				#Taking the charge of the atoms for the Filename	
				elif line_number == 1:
					if "charge=" in line:			
						charge = int(line.split("=")[1])		
					else:
						charge = 0
					# Reading atoms with a 1-probability. Note that is the same that delete atoms with a probability.		
				else:
					#Reading from original File.
					num, atomic_symbol, x, y, z, pot = line.split() 
					element_change = False
					
					x_.append(float(x))
					y_.append(float(y))
					z_.append(float(z))
					
	return (max(x_)+min(x_))/2.0, (max(y_)+min(y_))/2.0
	
