import numpy as np	


def compute_Radio_prob(filename2,prob,r):

	atomic_symbol2_=[]
	x2_=[]
	y2_=[]
	z2_=[]
	prob_new=[]
	
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
	
	
	count=0
	
	for i in range(len(x2_)):
	
		distance = np.sqrt((x2_[i]-x0)*(x2_[i]-x0)+(y2_[i]-y0)*(y2_[i]-y0))
		
		if distance < r :
			count=count+1
			
	print ("Number of particles inside the radius:", count)
	for p in prob:
		prob_new.append( float(num_atoms_total)/float(count)*p)
	print("New probability:", prob_new)
	
	return prob_new

