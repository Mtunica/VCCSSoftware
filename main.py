import sys
import json
#from aux.create_material import create_material
from aux.create_vacants import create_vacants
from aux.create_vacants import create_vacants_gaussian
from aux.create_vacants import create_vacants_radio
from aux.create_vacants import create_vacants_number
from aux.create_vacants import create_vacants_gaussian_number
from aux.create_vacants import create_vacants_radio_number
from aux.create_vacants import create_vacants_semiradio_number
from aux.create_vacants import create_vacants_antiradio_number
from aux.create_vacants import create_vacants_semiantiradio_number

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
	create_vacants_number(f['probabilities_file'], f['input'], f['output'], int(f['num_files']),float(f['length']))

elif f['action'] == 'vacants gauss number':
	create_vacants_gaussian_number(f['probabilities_file'], f['input'], f['output'], int(f['num_files']),float(f['sigma']),float(f['amplitude']),float(f['length']),int(f['count']))

elif f['action'] == 'vacants radio number':
	create_vacants_radio_number(f['probabilities_file'], f['input'], f['output'], int(f['num_files']),float(f['radio']),float(f['length']))
	
elif f['action'] == 'vacants semi radio number':
	create_vacants_semiradio_number(f['probabilities_file'], f['input'], f['output'], int(f['num_files']),float(f['radio']),float(f['distance']),float(f['length']))

elif f['action'] == 'vacants antiradio number':
	create_vacants_antiradio_number(f['probabilities_file'], f['input'], f['output'], int(f['num_files']),float(f['radio']),float(f['length']))
	
elif f['action'] == 'vacants semi antiradio number':
	create_vacants_semiantiradio_number(f['probabilities_file'], f['input'], f['output'], int(f['num_files']),float(f['radio']),float(f['distance']),float(f['length']))


else:
	print("No action in database \n")
