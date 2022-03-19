import sys
from aux.vacants import vacants_creation_xyz
from aux.vacants import vacants_obtained
from aux.vacants import vacants_creation_gaussian
from aux.vacants import vacants_creation_radio
from aux.vacants import vacants_obtained_radio
from aux.vacants import vacants_creation_number
from aux.vacants import vacants_obtained_number

from aux.mu import compute_mu

from aux.create_xyz_file import create_xyz_file

from aux.compare_xyz_file import comprare_xyz_file

from aux.compute_radio_prob import compute_Radio_prob

import timeit


def create_vacants (probabilities_file, input_file, output_file,num_files):
	
	#We want to compute time as well
	start = timeit.default_timer()
	
	#Define element and probabilities vector
	new_elements=[]
	probabilities = []
	
	for i in range(num_files):
		new_elements, probabilities = vacants_obtained(probabilities_file,i)
		print(probabilities)
		vacants_creation_xyz(input_file, probabilities, new_elements, str(i)+output_file)
		probabilities.clear()
		new_elements.clear()
	stop = timeit.default_timer()
	print('Time: ', stop - start) 

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def create_vacants_gaussian (probabilities_file, input_file, output_file,num_files,sigma, amplitude):
	
	#We want to compute time as well
	start = timeit.default_timer()
	
	#Define element and probabilities vector
	new_elements=[]
	probabilities = []
	x0,y0=compute_mu(input_file)
	print("x0:", x0, "y0:", y0)
	for i in range(num_files):
		new_elements, probabilities = vacants_obtained(probabilities_file,i)
		print(probabilities)
		vacants_creation_gaussian(input_file, probabilities, new_elements, "output/"+str(i)+output_file,x0,y0,sigma,amplitude)
		probabilities.clear()
		new_elements.clear()
		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element"+str(i)+".xyz" )
	stop = timeit.default_timer()
	print('Time: ', stop - start) 

#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def create_vacants_radio(probabilities_file, input_file, output_file,num_files):
	
	#We want to compute time as well
	start = timeit.default_timer()
	
	#Define element and probabilities vector
	new_elements=[]
	probabilities = []
	x0,y0=compute_mu(input_file)
	print("x0:", x0, "y0:", y0)
	for i in range(num_files):
		new_elements, probabilities, radio = vacants_obtained_radio(probabilities_file,i)
		probabilities = compute_Radio_prob(input_file,probabilities,radio)
		print("Radio:", radio)
		vacants_creation_radio(input_file, probabilities, new_elements, "output/"+str(i)+output_file,radio,x0,y0)
		probabilities.clear()
		new_elements.clear()
		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element_radio_"+str(i)+".xyz" )
	stop = timeit.default_timer()
	print('Time: ', stop - start) 
	
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def create_vacants_number(probabilities_file, input_file, output_file,num_files):
	
	#We want to compute time as well
	start = timeit.default_timer()
	
	for i in range(num_files):
		num = vacants_obtained_number(probabilities_file,i)

		vacants_creation_number(input_file, num, "output/"+str(i)+output_file)

		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element_number_"+str(i)+".xyz" )
	stop = timeit.default_timer()
	print('Time: ', stop - start) 
