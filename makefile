uniform: main.py input/vacants.json output
	python3 main.py input/vacants.json
	
gaussian: main.py input/vacants_gauss.json output
	python3 main.py input/vacants_gauss.json
	
radio: main.py input/vacants_radio.json output
	python3 main.py input/vacants_radio.json
	
number: main.py input/vacants_number.json output
	python3 main.py input/vacants_number.json	

output:
	mkdir output
