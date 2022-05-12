#===============================================================================================================
#===============================================================================================================
#vacants.py.....................................................................................................
#===============================================================================================================
#===============================================================================================================
#import libraries
import pandas as pd
import numpy as np
import random
import csv
#...............................................................................................................
#...............................................................................................................
#Vacants_creation_xyz...........................................................................................
#ToDo:Optimitzation of the File writing, and paral·lelitzation..................................................
#...............................................................................................................
#...............................................................................................................
def vacants_creation_xyz(filename, probability, new_element, output_file):
#...............................................................................................................
#Security comprovations
	#Emergency exit for total probability bigger than 1
	if sum(probability)>1:
		print("ERROR:Probability higer than 1")
		exit() #Stop program
#===============================================================================================================
#Variable declaration
	x_ = []
	y_ = []
	z_ = []
	count_=[]
	symbol_=[]
	potential_=[]
	 #Array xyz_coordinates = atomic symbol, x, y, z
	num_atoms = [] #Number of new_elements on the file
	num_atoms=[0 for i in range(len(new_element))]
	probability_calculation = []
	probability_calculation=[0 for i in range(len(new_element)+1)]

	for i in range(1, len(probability_calculation)):
		probability_calculation[i] = probability_calculation[i-1] + probability[i-1]

#===============================================================================================================
#
#===============================================================================================================

	#Open Filename with the original list of elements.
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
				random_number = random.random()

				for i in range(len(new_element)):
					#Aplication of probability


					if  ((random_number <= probability_calculation[i+1]) and (random_number > probability_calculation[i])) :
						num_atoms[i] = num_atoms[i] + 1
						element_change = True

						if new_element[i] == "void":
							break
						else:
							count+=1
							count_.append(count)
							symbol_.append(new_element[i])
							x_.append(float(x))
							y_.append(float(y))
							z_.append(float(z))
							potential_.append(float(pot))
							break

				if element_change == False:
					count+=1
					count_.append(count)
					symbol_.append(atomic_symbol)
					x_.append(float(x))
					y_.append(float(y))
					z_.append(float(z))
					potential_.append(float(pot))

#===============================================================================================================
#===============================================================================================================
#Calculus of the numbers
	with open("log_out", "a") as fileout2:
		num_atoms_delete = 0
		fileout2.write("Element,num_atoms,prob target,prob real\n")
		for i in range(len(new_element)):
			fileout2.write(str(new_element[i])+ " " + str(num_atoms[i]) + " " + str(probability[i]) + " " + str(num_atoms[i]/num_atoms_total)+ "\n")
			if (new_element[i] == "void"):
				num_atoms_delete+=num_atoms[i]

			fileout2.write("\n\n")
#===============================================================================================================
#===============================================================================================================
		#Print in an output File.
		with open(output_file, "w") as fileout1:
			#Writing number of atoms.
			fileout1.write("LAMMPS 	coordinates with atom_style = atomic\n")
			fileout1.write("\n")
			fileout1.write(str(num_atoms_total-num_atoms_delete)+" atoms\n")
			fileout1.write("\n")
			fileout1.write(" 1 atom types\n")
			fileout1.write("\n")
			fileout1.write("-59.91928        59.91926 xlo xhi\n")
			fileout1.write("-58.77384        58.77382 ylo yhi\n")
			fileout1.write("0.0        893.5607 zlo zhi\n")
			fileout1.write("\n")

			fileout1.write("Masses\n")
			fileout1.write("\n")
			fileout1.write("1 28.0855\n")
			fileout1.write("\n")
			fileout1.write("Atoms\n")
			fileout1.write("\n")

			for aaa in range(len(x_)):
				fileout1.write("{:8d} {} {:12.5f} {:12.5f} {:12.5f} {:12.3f} \n".format(count_[aaa],symbol_[aaa],x_[aaa],y_[aaa],z_[aaa],potential_[aaa]))

		return
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#...............................................................................................................
#...............................................................................................................
def vacants_creation_radio(filename, probability, new_element, output_file,radio,x0,y0):
#...............................................................................................................
#Security comprovations
	#Emergency exit for total probability bigger than 1
	if sum(probability)>1:
		print("ERROR:Probability higer than 1")
		exit() #Stop program
#===============================================================================================================
#Variable declaration
	x_ = []
	y_ = []
	z_ = []
	count_=[]
	symbol_=[]
	potential_=[]
	 #Array xyz_coordinates = atomic symbol, x, y, z
	num_atoms = [] #Number of new_elements on the file
	num_atoms=[0 for i in range(len(new_element))]
	probability_calculation = []
	probability_calculation=[0 for i in range(len(new_element)+1)]

	for i in range(1, len(probability_calculation)):
		probability_calculation[i] = probability_calculation[i-1] + probability[i-1]

#===============================================================================================================
#
#===============================================================================================================

	#Open Filename with the original list of elements.
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
				random_number = random.random()

				for i in range(len(new_element)):
					#Aplication of probability

					distance = np.sqrt((float(x)-x0)*(float(x)-x0)+(float(y)-y0)*(float(y)-y0))

					if  ((random_number <= probability_calculation[i+1]) and (random_number > probability_calculation[i]) and distance < radio[i]) :
						num_atoms[i] = num_atoms[i] + 1
						element_change = True

						if new_element[i] == "void":
							break
						else:
							count+=1
							count_.append(count)
							symbol_.append(new_element[i])
							x_.append(float(x))
							y_.append(float(y))
							z_.append(float(z))
							potential_.append(float(pot))
							break

				if element_change == False:
					count+=1
					count_.append(count)
					symbol_.append(atomic_symbol)
					x_.append(float(x))
					y_.append(float(y))
					z_.append(float(z))
					potential_.append(float(pot))

#===============================================================================================================
#===============================================================================================================
#Calculus of the numbers
	with open("log_out", "a") as fileout2:
		num_atoms_delete = 0
		fileout2.write("Element,num_atoms,prob target,prob real\n")
		for i in range(len(new_element)):
			fileout2.write(str(new_element[i])+ " " + str(num_atoms[i]) + " " + str(probability[i]) + " " + str(num_atoms[i]/num_atoms_total)+ "\n")
			if (new_element[i] == "void"):
				num_atoms_delete+=num_atoms[i]

			fileout2.write("\n\n")
#===============================================================================================================
#===============================================================================================================
		#Print in an output File.
		with open(output_file, "w") as fileout1:
			#Writing number of atoms.
			fileout1.write("LAMMPS 	coordinates with atom_style = atomic\n")
			fileout1.write("\n")
			fileout1.write(str(num_atoms_total-num_atoms_delete)+" atoms\n")
			fileout1.write("\n")
			fileout1.write(" 1 atom types\n")
			fileout1.write("\n")
			fileout1.write("-59.91928        59.91926 xlo xhi\n")
			fileout1.write("-58.77384        58.77382 ylo yhi\n")
			fileout1.write("0.0        893.5607 zlo zhi\n")
			fileout1.write("\n")

			fileout1.write("Masses\n")
			fileout1.write("\n")
			fileout1.write("1 28.0855\n")
			fileout1.write("\n")
			fileout1.write("Atoms\n")
			fileout1.write("\n")

			for aaa in range(len(x_)):
				fileout1.write("{:8d} {} {:12.5f} {:12.5f} {:12.5f} {:12.3f} \n".format(count_[aaa],symbol_[aaa],x_[aaa],y_[aaa],z_[aaa],potential_[aaa]))

		return
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================
#...............................................................................................................
#...............................................................................................................
#Vacants_creation_xyz...........................................................................................
#ToDo:Optimitzation of the File writing, and paral·lelitzation..................................................
#...............................................................................................................
#...............................................................................................................
def vacants_creation_gaussian(filename, probability, new_element, output_file,x0,y0,sigma,amplitude):
#...............................................................................................................
#Security comprovations
	#Emergency exit for total probability bigger than 1
	if sum(probability)>1:
		print("ERROR:Probability higer than 1")
		exit() #Stop program
#===============================================================================================================
#Variable declaration
	x_ = []
	y_ = []
	z_ = []
	count_=[]
	symbol_=[]
	potential_=[]
	 #Array xyz_coordinates = atomic symbol, x, y, z
	num_atoms = [] #Number of new_elements on the file
	num_atoms=[0 for i in range(len(new_element))]
	probability_calculation = []
	probability_calculation=[0 for i in range(len(new_element)+1)]

	for i in range(1, len(probability_calculation)):
		probability_calculation[i] = probability_calculation[i-1] + probability[i-1]

#===============================================================================================================
#
#===============================================================================================================

	#Open Filename with the original list of elements.
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
				r= np.sqrt((float(x)-x0)*(float(x)-x0)+(float(y)-y0)*(float(y)-y0))
				random_number = amplitude*np.exp(-0.5*(r/sigma)*(r/sigma))/sigma/np.sqrt(2.0*np.pi)
				random_number2= random.random()

				for i in range(len(new_element)):
					#Aplication of probability


					if  (random_number2 <= random_number) :
						num_atoms[i] = num_atoms[i] + 1
						element_change = True

						if new_element[i] == "void":
							break
						else:
							count+=1
							count_.append(count)
							symbol_.append(new_element[i])
							x_.append(float(x))
							y_.append(float(y))
							z_.append(float(z))
							potential_.append(float(pot))
							break

				if element_change == False:
					count+=1
					count_.append(count)
					symbol_.append(atomic_symbol)
					x_.append(float(x))
					y_.append(float(y))
					z_.append(float(z))
					potential_.append(float(pot))

#===============================================================================================================
#===============================================================================================================
#Calculus of the numbers
	with open("log_out", "a") as fileout2:
		num_atoms_delete = 0
		fileout2.write("Element,num_atoms,prob target,prob real\n")
		for i in range(len(new_element)):
			fileout2.write(str(new_element[i])+ " " + str(num_atoms[i]) + " " + str(probability[i]) + " " + str(num_atoms[i]/num_atoms_total)+ "\n")
			if (new_element[i] == "void"):
				num_atoms_delete+=num_atoms[i]

			fileout2.write("\n\n")
#===============================================================================================================
#===============================================================================================================
		#Print in an output File.
		with open(output_file, "w") as fileout1:
			#Writing number of atoms.
			fileout1.write("LAMMPS 	coordinates with atom_style = atomic\n")
			fileout1.write("\n")
			fileout1.write(str(num_atoms_total-num_atoms_delete)+" atoms\n")
			fileout1.write("\n")
			fileout1.write(" 1 atom types\n")
			fileout1.write("\n")
			fileout1.write("-59.91928        59.91926 xlo xhi\n")
			fileout1.write("-58.77384        58.77382 ylo yhi\n")
			fileout1.write("0.0        893.5607 zlo zhi\n")
			fileout1.write("\n")

			fileout1.write("Masses\n")
			fileout1.write("\n")
			fileout1.write("1 28.0855\n")
			fileout1.write("\n")
			fileout1.write("Atoms\n")
			fileout1.write("\n")

			for aaa in range(len(x_)):
				fileout1.write("{:8d} {} {:12.5f} {:12.5f} {:12.5f} {:12.3f} \n".format(count_[aaa],symbol_[aaa],x_[aaa],y_[aaa],z_[aaa],potential_[aaa]))

		return
#===============================================================================================================
#===============================================================================================================
#...............................................................................................................
def vacants_creation_number(filename, number_new_atoms, output_file):
#...............................................................................................................
#Security comprovations
#===============================================================================================================
#Variable declaration
	inside=[]
	x_ = []
	y_ = []
	z_ = []

	symbol_=[]
	potential_=[]

#===============================================================================================================
#
#===============================================================================================================

	#Open Filename with the original list of elements.
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

				count+=1
				symbol_.append(atomic_symbol)
				x_.append(float(x))
				y_.append(float(y))
				z_.append(float(z))
				potential_.append(float(pot))
				inside.append(True)

	random_sample = random.sample(range(count), int(number_new_atoms))


	for rand_num in random_sample:

		inside[rand_num]=False

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
		fileout1.write("0.0        2699.49386 zlo zhi\n")
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
