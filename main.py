import sys
import json
#from aux.create_material import create_material
from aux.create_vacants import create_vacants
from aux.create_vacants import create_vacants_gaussian
from aux.create_vacants import create_vacants_radio
from aux.create_vacants import create_vacants_number

with open (sys.argv[1], 'r') as file:
	f = json.load(file)
	
	
#if f['action'] == 'create':
#	create_material(f['output'], f['lattice'], f['atom'], f['nx'], f['ny'], f['nz'], f['charge'])

if f['action'] == 'vacants':
	create_vacants(f['probabilities_file'], f['input'], f['output'], int(f['num_files']))	
	
elif f['action'] == 'vacants gauss':
	create_vacants_gaussian(f['probabilities_file'], f['input'], f['output'], int(f['num_files']),float(f['sigma']),float(f['amplitude']))
	
elif f['action'] == 'vacants radio':
	create_vacants_radio(f['probabilities_file'], f['input'], f['output'], int(f['num_files']))
	
elif f['action'] == 'vacants number':
	create_vacants_number(f['probabilities_file'], f['input'], f['output'], int(f['num_files']))
		
		
else:
	print("No action in database \n")
