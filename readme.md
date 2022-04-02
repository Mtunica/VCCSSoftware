<h1 align="center">VCCS-Software</h1>

<div align="center">


</div>

---

<p align="center">     <br> 
</p>
## Table of Contents

- [Structure](#structure)
	+ [Main](#main)
	+ [Make file](#make)
	+ [Aux](#aux)
	+ [Input parameters](#inputs)
	+ [Output files and plots](#outputs)
- [Operations](#operations)
	+ [Uniform vacancies approximated to a percentage](#uniform)
	+ [Uniform distribution of a particular number of vacancies](#number)
	+ [Gaussian radial distribution](#gaussian)
	+ [Uniform vacancies approximated to a percentage concentrated in a particular radius](#radius)
- [TODO](#todo)
- [Authors](#authors)

## Structure of the code <a name = "structure"></a>
### Main <a name = "main"></a>
### Make file <a name = "make"></a>
### Aux <a name = "aux"></a>

Aux is a folder which contains the functions and modules of the code. 

#### vacants.py 

The file **vacants.py** contains the following functions for generating the vacancies:

* **vacants\_creation\_xyz(filename, probability, new\_element, output\_file)**: [Uniform distribution](#uniform) of the vacancies.

* **vacants\_creation\_radio(filename, probability, new\_element, output\_file,radio,x0,y0)**: [Uniform distribution in a given radio](#radio) of the vacancies.


* **vacants\_creation\_gaussian(filename, probability, new\_element, output\_file,x0,y0,sigma,amplitude)**: [Gaussian distribution](#gaussian) of the vacancies.


* **vacants\_creation\_number(filename, number\_new\_atoms, output\_file)**:  [Uniform distribution given a particular number](#number) of the vacancies.

The file **vacants.py** contains the following functions to read the probabilities files:

* **vacants\_obtained (file_name,num\_file)**:

* **vacants\_obtained\_radio (file\_name,num_file):**


* **vacants\_obtained\_number (file\_name,num_file):**


#### compare\_xyz\_file.py

#### compute\_radio\_prob.py 
#### create\_vacants.py
#### create\_xyz\_file.py
#### mu.py 

Given a coordinates file of a nanowire along z, computes the x,y center.
* **create\_material.py** : In process... 


### Inputs <a name = "inputs"></a>

### Outputs <a name = "outputs"></a>


## Operations <a name = "operations"></a>

This is a program to generate the vacants given an input file (example in folder input, pure.xyz). It reads a json input file (example in vacants.json) and creates the probabilities from input file probabilities (example in input folder).



### Create vacancies random uniform with an approximated probability <a name = "uniform"></a>

#### Input file

There are two input files. 

1. **vacants.json**: It contains the following parameters:
	* **action**: Always vacants
	* **input**: The input file of coordinates. 
	* **output**: name of the output_file
	* **probabilities_file**: Link to the probabilities file.
	* **num_files**: Number of probabilities of probabilities file.

2. **probabilities**: The list of percentages of vacancies. the format is: ```element percentage``` . At the end of the file, add ```end```.


#### Execution


To execute, write in terminal ``` make  uniform``` .


### Create a particular number of vacancies<a name = "number"></a>


#### Input file

There are two input files. 

1. **vacants_number.json**: It contains the following parameters:
	* **action**: Always vacants number
	* **input**: The input file of coordinates. 
	* **output**: name of the output_file
	* **probabilities_file**: Link to the probabilities file.
	* **num_files**: Number of probabilities of probabilities file.

2. **probabilities_number**: The list of percentages of vacancies. the format is: ```element number of vacancies``` . At the end of the file, add ```end```.


### Execution


To execute, write in terminal ``` make  number``` .



### Create vacancies following a radial Gaussian distribution<a name = "gaussian"></a>


#### Input file

There are two input files. 

1. **vacants_gauss.json**: It contains the following parameters:
	* **action**: Always vacants gauss
	* **input**: The input file of coordinates. 
	* **output**: name of the output_file
	* **probabilities_file**: Link to the probabilities file.
	* **num_files**: Number of probabilities of probabilities file.
	* **mean**:
	* **sigma**:
	* **amplitude**:

2. **probabilities_number**: The list of percentages of vacancies. the format is: ```element number of vacancies``` . At the end of the file, add ```end```.



### Execution

To execute, write in terminal ``` make  gaussian``` .




### Create vacancies randomly approximated to a percentage in a particular radius.  <a name = "radio"></a>

#### Input file

There are two input files. 

1. **vacants_gauss.json**: It contains the following parameters:
	* action: Always vacants gauss
	* input: The input file of coordinates. 
	* output: name of the output_file
	* probabilities_file: Link to the probabilities file.
	* num_files: Number of probabilities of probabilities file.
	* mean:
	* sigma:
	* amplitude:

2. **probabilities_number**: The list of percentages of vacancies. the format is: ```element number of vacancies``` . At the end of the file, add ```end```.


#### Execution

To execute, write in terminal ``` make  radio``` .



## ToDo <a name = "todo"></a>

* Optimise
* Finish readme
* Add radio+number

## Authors
