import sys
from aux.vacants import vacants_creation_xyz
from aux.obtained.obtained_vacants import vacants_obtained
from aux.vacants import vacants_creation_gaussian
from aux.vacants import vacants_creation_radio
from aux.obtained.obtained_vacants import vacants_obtained_radio
from aux.vacancies.uniform_number import vacants_creation_number
from aux.obtained.obtained_vacants import vacants_obtained_number
from aux.vacancies.gaussian_number import vacants_gaussian_number
from aux.vacancies.radio import vacants_radio_number
from aux.vacancies.semiradio import vacants_semiradio_number
from aux.vacancies.antiradio import vacants_antiradio_number
from aux.vacancies.antisemiradio import vacants_antisemiradio_number

from aux.mu import compute_mu

from aux.create_xyz_file import create_xyz_file

from aux.compare_xyz_file import comprare_xyz_file

from aux.compute_radio_prob import compute_Radio_prob

import timeit

#**********************************************************************************************************************************
#**********************************************************************************************************************************
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
def create_vacants_gaussian_number(probabilities_file, input_file, output_file,num_files,sigma, amplitude,length,max_count):

	#Time computing
	start = timeit.default_timer()

	#Define element and probabilities vector

	x0,y0=compute_mu(input_file)
	print("x0:", x0, "y0:", y0)
	for i in range(num_files):
		num = vacants_obtained_number(probabilities_file,i)
		vacants_gaussian_number(input_file, num, "output/"+str(i)+output_file,x0,y0,sigma,amplitude,length,max_count)


		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element"+str(i)+".xyz" )

	#Time computing
	stop = timeit.default_timer()
	print('Time: ', stop - start)

#**********************************************************************************************************************************
#**********************************************************************************************************************************
def create_vacants_radio_number(probabilities_file, input_file, output_file,num_files,radio,length):

	#Time computing
	start = timeit.default_timer()

	#Define element and probabilities vector

	x0,y0=compute_mu(input_file)
	print("x0:", x0, "y0:", y0)
	for i in range(num_files):
		num = vacants_obtained_number(probabilities_file,i)
		vacants_radio_number(input_file, num, "output/"+str(i)+output_file,x0,y0,radio,length)


		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element"+str(i)+".xyz" )

	#Time computing
	stop = timeit.default_timer()
	print('Time: ', stop - start)
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def create_vacants_semiradio_number(probabilities_file, input_file, output_file,num_files,radio,midle,length):

	#Time computing
	start = timeit.default_timer()

	#Define element and probabilities vector

	x0,y0=compute_mu(input_file)
	print("x0:", x0, "y0:", y0)
	for i in range(num_files):
		num = vacants_obtained_number(probabilities_file,i)
		vacants_semiradio_number(input_file, num, "output/"+str(i)+output_file,x0,y0,radio,midle,length)


		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element"+str(i)+".xyz" )

	#Time computing
	stop = timeit.default_timer()
	print('Time: ', stop - start)	

#**********************************************************************************************************************************
#**********************************************************************************************************************************
def create_vacants_antiradio_number(probabilities_file, input_file, output_file,num_files,radio,length):

	#Time computing
	start = timeit.default_timer()

	#Define element and probabilities vector

	x0,y0=compute_mu(input_file)
	print("x0:", x0, "y0:", y0)
	for i in range(num_files):
		num = vacants_obtained_number(probabilities_file,i)
		vacants_antiradio_number(input_file, num, "output/"+str(i)+output_file,x0,y0,radio,length)


		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element"+str(i)+".xyz" )

	#Time computing
	stop = timeit.default_timer()
	print('Time: ', stop - start)
#**********************************************************************************************************************************
#**********************************************************************************************************************************
def create_vacants_semiantiradio_number(probabilities_file, input_file, output_file,num_files,radio,midle,length):

	#Time computing
	start = timeit.default_timer()

	#Define element and probabilities vector

	x0,y0=compute_mu(input_file)
	print("x0:", x0, "y0:", y0)
	for i in range(num_files):
		num = vacants_obtained_number(probabilities_file,i)
		vacants_semi_antiradio_number(input_file, num, "output/"+str(i)+output_file,x0,y0,radio,midle,length)


		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element"+str(i)+".xyz" )

	#Time computing
	stop = timeit.default_timer()
	print('Time: ', stop - start)
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
def create_vacants_number(probabilities_file, input_file, output_file,num_files,length):

	#We want to compute time as well
	start = timeit.default_timer()

	for i in range(num_files):
		num = vacants_obtained_number(probabilities_file,i)

		vacants_creation_number(input_file, num, "output/"+str(i)+output_file,length)

		create_xyz_file("output/"+str(i)+output_file,"output/"+str(i)+".xyz")
		comprare_xyz_file("output/"+str(i)+output_file,input_file,"output/element_number_"+str(i)+".xyz" )
	stop = timeit.default_timer()
	print('Time: ', stop - start)
