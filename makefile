
dir_input = input/json_inputs
## 1. uniform:
uniform: main.py $(dir_input)/vacants.json output
	python3 main.py $(dir_input)/vacants.json

## 2. gaussiam:
gaussian: main.py $(dir_input)/vacants_gauss.json output
	python3 main.py $(dir_input)/vacants_gauss.json

## 3. radio:
radio: main.py $(dir_input)/vacants_radio.json output
	python3 main.py $(dir_input)/vacants_radio.json

## 4. number_uniform:
number_uniform: main.py $(dir_input)/vacants_number.json output
	python3 main.py $(dir_input)/vacants_number.json

## 5. number_gauss:
number_gauss: main.py $(dir_input)/vacants_gauss_number.json output
	python3 main.py $(dir_input)/vacants_gauss_number.json

## 6. number_radio:
number_radio: main.py $(dir_input)/vacants_radio_number.json output
	python3 main.py $(dir_input)/vacants_radio_number.json

## 7. number_antiradio:
number_antiradio: main.py $(dir_input)/vacants_antiradio_number.json output
	python3 main.py $(dir_input)/vacants_antiradio_number.json

## 8. number_semi_radio:
number_semi_radio: main.py $(dir_input)/vacants_semiradio_number.json output
	python3 main.py $(dir_input)/vacants_semiradio_number.json

## 9. number_semi_radio:
number_semi_radio: main.py $(dir_input)/vacants_antisemiradio_number.json output
	python3 main.py $(dir_input)/vacants_antisemiradio_number.json

output:
	mkdir output

.PHONY : help
help:
	@sed -n 's/^##//p' makefile
