#import libraries
import pandas as pd
import numpy as np
import random
import csv

#===============================================================================================================
#...............................................................................................................
def vacants_gaussian_number(filename, number_new_atoms, output_file,x0,y0,sigma,amplitude,length):

    """This function generates vacancies following a Gaussian distribution considering a specific number of Vacancies."""
    """Inputs: Input file, number of vacancies, output file, Center of the nanowire(coordinate x), Center of the nanowire(coordinate y), sigma of the Gaussian distribution, Amplitude of the Gaussian distribution"""


#===============================================================================================================
#Variable
    inside
    x_ = []; y_ = []; z_ = []
    symbol_=[]
    potential_=[]
#===============================================================================================================
#===============================================================================================================

	#Open Filename with the original list of elements.
    with open(filename, "r") as file:
		#Reading the original File
        count =0
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

                count+=1
                symbol_.append(atomic_symbol)
                x_.append(float(x))
                y_.append(float(y))
                z_.append(float(z))
                potential_.append(float(pot))
                inside.append(True)

    random_sample = random.sample(range(count), int(count))

    end_of_loop =  number_new_atoms
    for ii in range(0,end_of_loop):

        x=x_[ii]; y=y_[ii]; z=z_[ii]

        r= np.sqrt((float(x)-x0)*(float(x)-x0)+(float(y)-y0)*(float(y)-y0))
        random_number_gauss = amplitude*np.exp(-0.5*(r/sigma)*(r/sigma))/sigma/np.sqrt(2.0*np.pi)
        random_number2= random.random()

        if  random_number2 < random_number_gauss:
            inside[rand_num]=False

        else:
            end_of_loop +=1

	#Print in an output File.
    with open(output_file, "w") as fileout1:
		#Writing number of atoms.
        fileout1.write("LAMMPS 	coordinates with atom_style = atomic\n")
        fileout1.write("\n")
        fileout1.write(str(count-int(number_new_atoms))+" atoms\n")
        fileout1.write("\n")
        fileout1.write(" 1 atom types\n")
        fileout1.write("\n")
        fileout1.write("-69.91928        69.91926 xlo xhi\n")
        fileout1.write("-68.77384        68.77382 ylo yhi\n")
        fileout1.write("0.0        {:8.5f} zlo zhi\n".format(length))
        fileout1.write("\n")

        fileout1.write("Masses\n")
        fileout1.write("\n")
        fileout1.write("1 28.0855\n")
        fileout1.write("\n")
        fileout1.write("Atoms\n")
        fileout1.write("\n")

        step=0
        for aaa in range(len(x_)):
            if inside[aaa] == True:
                step+=1
                fileout1.write("{:8d} {} {:12.5f} {:12.5f} {:12.5f} {:12.3f} \n".format(step,symbol_[aaa],x_[aaa],y_[aaa],z_[aaa],potential_[aaa]))
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
