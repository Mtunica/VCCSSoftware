#import libraries
import pandas as pd
import numpy as np
import random
import csv

#===============================================================================================================
#===============================================================================================================
def vacants_obtained (file_name,num_file):
	new_element=[]
	probabilities=[]
	boolean=False
	count=0
	with open(file_name, "r") as file_:
		for line in file_:

			if int(num_file)==count:
				boolean=True

			if line=="\n" or line=="end\n":
				count+=1

			if boolean == True:
				aux = line.split()

				if len(aux) == 2:
					element, probability = aux

					new_element.append(str(element))
					probabilities.append(float(probability))

				if line=="end\n" or line=="\n":

					return  new_element, probabilities;

#===============================================================================================================
#===============================================================================================================
def vacants_obtained_radio (file_name,num_file):
	new_element=[]
	probabilities=[]
	radios=[]
	boolean=False
	count=0
	with open(file_name, "r") as file_:
		for line in file_:

			if int(num_file)==count:
				boolean=True

			if line=="\n" or line=="end\n":
				count+=1

			if boolean == True:
				aux = line.split()

				if len(aux) == 3:
					element, probability, radio = aux

					new_element.append(str(element))
					probabilities.append(float(probability))
					radios.append(float(radio))

				if line=="end\n" or line=="\n":

					return  new_element, probabilities, radios;
#===============================================================================================================
#===============================================================================================================
def vacants_obtained_number (file_name,num_file):
	boolean=False
	count=0
	with open(file_name, "r") as file_:
		for line in file_:

			if int(num_file)==count:
				boolean=True

			if line=="\n" or line=="end\n":
				count+=1

			if boolean == True:
				aux = line.split()

				if len(aux) == 2:
					element, probability = aux


				if line=="end\n" or line=="\n":

					return  probability
