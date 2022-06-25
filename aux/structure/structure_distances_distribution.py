import numpy as np
import sys
from matplotlib import pyplot as plt

x2_=[]
y2_=[]
z2_=[]
atomic_symbol2_=[]

filename=sys.argv[1]
filename_out = "histogram_distance_from_center.out"

#Read file 2
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

            atomic_symbol2_.append(atomic_symbol)
            x2_.append(float(x))
            y2_.append(float(y))
            z2_.append(float(z))

x0= (max(x2_)+min(x2_))/2.0
y0= (max(y2_)+min(y2_))/2.0



with open(filename_out, "w") as fileout:

    for number in range(len(atomic_symbol2_)):
        fileout.write( str(np.sqrt((x2_[number]-x0)*(x2_[number]-x0) +(y2_[number]-y0)*(y2_[number]-y0)))+ "\n")


with open(filename_out) as f:
    v = np.loadtxt(f, delimiter=",", dtype='float', comments="#", skiprows=0, usecols=None)


v_hist = np.ravel(v)   # 'flatten' v
fig = plt.figure()
ax1 = fig.add_subplot(111)


n, bins, patches = ax1.hist(v_hist, bins=7, density=False, stacked=True, facecolor='green')
plt.ylabel("Frequency")
plt.xlabel("Distance from the center in Angstroms")
plt.savefig(filename_out+"image.png")
