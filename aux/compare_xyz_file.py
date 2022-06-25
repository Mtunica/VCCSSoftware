import numpy as np
import sys
from matplotlib import pyplot as plt

def gaussian_function(r_gauss,sigma_gauss):
	return 1.0/(2.0*np.pi*sigma_gauss)*np.exp(-0.5*r_gauss*r_gauss/sigma_gauss/sigma_gauss)

def comprare_xyz_file(filename1,filename2,filename_out):

	x_=[]
	y_=[]
	z_=[]
	atomic_symbol_=[]

	x2_=[]
	y2_=[]
	z2_=[]
	atomic_symbol2_=[]

	distances=[]

	#Read file 1
	with open(filename1, "r") as file:
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

	#Read file 2
	#Open Filename with the original list of elements.
	with open(filename2, "r") as file:
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

				atomic_symbol2_.append(atomic_symbol)
				x2_.append(float(x))
				y2_.append(float(y))
				z2_.append(float(z))

	x0= (max(x2_)+min(x2_))/2.0
	y0= (max(y2_)+min(y2_))/2.0


	#Write output

	file_extra = open(filename_out+"histogram_distance_from_center.out", "w")

	with open(filename_out, "w") as fileout:

		fileout.write(str(num_atoms_total) + "\n\n")

		count=0
		print("Number of atoms", len(x_))

		for number in range(len(atomic_symbol2_)):


			if (x_[count]== x2_[number] and y_[count]== y2_[number] and z_[count]== z2_[number] ):

				fileout.write(" {} {:12.5f} {:12.5f} {:12.5f} \n".format("A",x2_[number],y2_[number],z2_[number]))
				count=count+1

			else:
				fileout.write(" {} {:12.5f} {:12.5f} {:12.5f} \n".format("B",x2_[number],y2_[number],z2_[number]))
				file_extra.write( str(np.sqrt((x2_[number]-x0)*(x2_[number]-x0) +(y2_[number]-y0)*(y2_[number]-y0)))+ "\n")
				distances.append(np.sqrt((x2_[number]-x0)*(x2_[number]-x0) +(y2_[number]-y0)*(y2_[number]-y0)))

	file_extra.close()


	# bin=(max(distances)-min(distances))/0.01
	# print("Bin size: ",bin)

	with open(filename_out+"histogram_distance_from_center.out") as f:
		v = np.loadtxt(f, delimiter=",", dtype='float', comments="#", skiprows=0, usecols=None)


	v_hist = np.ravel(v)   # 'flatten' v
	fig = plt.figure()
	ax1 = fig.add_subplot(111)

	#plt.plot(v,gaussian_function(v,1.0))
	plt.ylabel("Frequency")
	plt.xlabel("Distance from the center in Angstroms")
	n, bins, patches = ax1.hist(v_hist,bins=7, range=[0,25],density=False, stacked=False, facecolor='black')
	plt.savefig(filename_out+"image.png")
