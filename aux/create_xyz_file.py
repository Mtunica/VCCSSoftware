import numpy as np
import sys

def create_xyz_file(filename, filename_out):
	x_=[]
	y_=[]
	z_=[]
	atomic_symbol_=[]

	with open(filename, "r") as file:
			#Reading the original File.
			count =0;
			read=False
			for line_number,line in enumerate(file):
				#Taking the number of atoms for the Filename
				if read ==True:
						#Reading from original File.
					num, atomic_symbol, x, y, z, pot = line.split() 
					element_change = False
						
					x_.append(float(x))
					y_.append(float(y))
					z_.append(float(z))
					atomic_symbol_.append(atomic_symbol)
					
				elif "atoms" in line:
					line=line.split()
					num_atoms_total = int(line[0])  #Will use num_atoms afterward.
					
				#Taking the charge of the atoms for the Filename	
				elif "Atoms" in line:
					read=True	
					next(file)
					
	with open(filename_out, "w") as fileout:

		fileout.write(str(num_atoms_total) + "\n\n")
		
		for number, element in enumerate(atomic_symbol_):
		
			fileout.write(" {} {:12.5f} {:12.5f} {:12.5f} \n".format(element,x_[number],y_[number],z_[number]))
