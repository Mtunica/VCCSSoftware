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
	+ [Uniform distribution of a particular number of vacancies](#Uniform Number)
	+ [Gaussian radial distribution](#Gaussian)
	+ [Gaussian radial distribution  of a particular number of vacancies](#Gaussian Number)
	+ [Uniform vacancies approximated to a percentage concentrated in a particular radius](#Radius)
	+ [Uniform vacancies of a particular number of vacancies concentrated in a particular radius](#Radius number)
	+ [Uniform vacancies of a particular number of vacancies concentrated outside a particular radius](#AntiRadius Number)
	+ [Uniform vacancies of a particular number of vacancies in a ring](#Semi Radius Number)
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

There are two input files.

1. **Json inputs**

   1. **vacants_gauss.json**: 

      1. action: Always vacants gauss

      ​	2. input: The input file of coordinates.

      ​	3. output: name of the output_file

      ​	4. probabilities_file: Link to the probabilities file.

      ​	5. num_files: Number of probabilities of probabilities file.

       	7. sigma:

   2. **vacants.json:**

      1.  action: Always vacants gauss

      2. input: The input file of coordinates.

      3. output: name of the output_file

      4.  probabilities_file: Link to the probabilities file.

      5. num_files: Number of probabilities of probabilities file.

   3. **vacants_gauss_number.json:** 

      1. action: Always vacants gauss number

      ​	2. input: The input file of coordinates.

      ​	3. output: name of the output_file

      ​	4. probabilities_file: Link to the probabilities file.

      ​	5. num_files: Number of probabilities of probabilities file.

       	7. sigma:

      8. length: length of the nanowire to write for LAMMPS.
      9. count: Number of times it is accepted.

   4. **vacants_radio_number.json:**

      1.  action: Always vacants radio number
      2. input: The input file of coordinates.
      3. output: name of the output_file
      4.  probabilities_file: Link to the probabilities file.
      5. num_files: Number of probabilities of probabilities file.
      6. radio: The radius of the cylinder.
      7. length: length of the nanowire to write for LAMMPS.

   5. **vacants_radio.json:**

      1. action: Always vacants radio

      ​	2. input: The input file of coordinates.

      ​	3. output: name of the output_file

      ​	4. probabilities_file: Link to the probabilities file.

      ​	5. num_files: Number of probabilities of probabilities file.

   6. **vacants_semiradio_number.json:**

      1.  action: Always vacants semi radio number
      2. input: The input file of coordinates.
      3. output: name of the output_file
      4.  probabilities_file: Link to the probabilities file.
      5. num_files: Number of probabilities of probabilities file.
      6. radio: The thickness of the ring.
      7. distance: Average radius of the ring
      8. length: length of the nanowire to write for LAMMPS.

   7. **vacants_antiradio_number.json:**

      1.  action: Always vacants anti radio number
      2. input: The input file of coordinates.
      3. output: name of the output_file
      4.  probabilities_file: Link to the probabilities file.
      5. num_files: Number of probabilities of probabilities file.
      6. radio: The radius of the cylinder.
      7. length: length of the nanowire to write for LAMMPS.

   8. **vacants_antisemiradio_number.json:**

      1.  action: Always vacants antisemi radio number
      2. input: The input file of coordinates.
      3. output: name of the output_file
      4.  probabilities_file: Link to the probabilities file.
      5. num_files: Number of probabilities of probabilities file.
      6. radio: The thickness of the ring.
      7. distance: Average radius of the ring
      8. length: length of the nanowire to write for LAMMPS.

2. **Probabilities Folder**

   1. **probabilities:** The list of percentages of vacancies. the format is: ```element percentage``` . At the end of the file, add ```end```.
   2. **probabilities_number**: The list of number of vacancies. the format is: ```element number of vacancies``` . At the end of the file, add ```end```
   3. **probabilities_radio**:  

### Outputs <a name = "outputs"></a>

1. data.xyz containing the nanowire without the deleted atoms.
2. element.xyz containing the vacancies with letter B and the atoms with letter A.
3. Histogram of the vacancies. 


## Operations <a name = "operations"></a>

This is a program to generate the vacants given an input file (example in folder input, pure.xyz). It reads a json input file (example in vacants.json) and creates the probabilities from input file probabilities (example in input folder).



### Execution


To execute, write in terminal ``` make  number``` .



## ToDo <a name = "todo"></a>

* Optimise
* Finish readme

## Authors
