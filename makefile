dir_input = input/json_inputs

uniform: main.py $(dir_input)/vacants.json output
	python3 main.py $(dir_input)/vacants.json

gaussian: main.py $(dir_input)/vacants_gauss.json output
	python3 main.py $(dir_input)/vacants_gauss.json

radio: main.py $(dir_input)/vacants_radio.json output
	python3 main.py $(dir_input)/vacants_radio.json

number: main.py $(dir_input)/vacants_number.json output
	python3 main.py $(dir_input)/vacants_number.json

number_gauss: main.py $(dir_input)/vacants_gauss_number.json output
	python3 main.py $(dir_input)/vacants_gauss_number.json

output:
	mkdir output
