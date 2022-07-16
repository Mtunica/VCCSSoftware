<h1 align="center">VCCS-Software</h1>

<div align="center">
This is a program to generate the vacants given an input file (example in folder input, pure.xyz). It reads a json input file (example in vacants.json) and creates the probabilities from input file probabilities (example in input folder).

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
	+ [Execution](#execution)
- [TODO](#todo)
- [Authors](#authors)

## Structure of the code <a name = "structure"></a>
### Main <a name = "main"></a>

The main file reads the action of the input json file, which is introduced via argument when executing the code. Then it selects the relevant parameters according to the action we want to implement.

### Make file <a name = "make"></a>

Tha make file contains a serie of predeterminated actions with the predeterminated json files located in the input folder.

1. **uniform:** 
2. **gaussian:** 
3. **radio:**
4. **number_uniform_:** 
5. **number_gauss:**
6. **number_radio:**
7. **number_antiradio:**
8. **number_semi_radio:**
9. **number_anti_semi_radio:** 

### Aux <a name = "aux"></a>

Aux is a folder which contains the functions and modules of the code.

#### vacants.py

The file **vacants.py** contains the following functions for generating the vacancies:

* **vacants\_creation\_xyz(filename, probability, new\_element, output\_file)**: Uniform distribution of the vacancies.

* **vacants\_creation\_radio(filename, probability, new\_element, output\_file,radio,x0,y0)**: Uniform distribution in a given radio of the vacancies.


* **vacants\_creation\_gaussian(filename, probability, new\_element, output\_file,x0,y0,sigma,amplitude)**: Gaussian distribution of the vacancies.

#### vacancies/antiradio.py

* **vacants_antiradio_number(filename, number_new_atoms, output_file,x0,y0,radius,length)**: "This function generates vacancies inside a particular radius considering a specific number of Vacancies.

#### vacancies/antisemiradio.py

* **vacants_antisemiradio_number(filename, number_new_atoms, output_file,x0,y0,radius,middle_radius,length)**: This function generates vacancies inside a particular radius considering a specific number of Vacancies.

#### vacancies/radio.py

* **vacants_radio_number(filename, number_new_atoms, output_file,x0,y0,radius,length)**:  This function generates vacancies inside a particular radius considering a specific number of Vacancies. 

#### vacancies/semiradio.py

* **vacants_semiradio_number(filename, number_new_atoms, output_file,x0,y0,radius,middle_radius,length)**: This function generates vacancies inside a particular radius considering a specific number of Vacancies. 

#### vacancies/uniform_number.py

* **vacants_creation_number(filename, number_new_atoms, output_file,length)**: This function creates a uniform distribution given a particular number of the vacancies.

 #### obtained_vacants.py

The following functions aim to read the probabilities files:

* **vacants\_obtained (file_name,num\_file)**: Return element and probability.

* **vacants\_obtained\_radio (file\_name,num_file):** Return element, probability and radius.


* **vacants\_obtained\_number (file\_name,num_file):** Return number of vacancies.



#### create\_vacants.py

All this functions are the coordinator between the obtained vacancies file and the creation functions.

* **create_vacants (probabilities_file, input_file, output_file,num_files)**
* **create_vacants_gaussian (probabilities_file, input_file, output_file,num_files,sigma, amplitude)**
* **create_vacants_gaussian_number(probabilities_file, input_file, output_file,num_files,sigma, amplitude,length,max_count)**:
* **create_vacants_radio_number(probabilities_file, input_file, output_file,num_files,radio,length)**:
* **create_vacants_semiradio_number(probabilities_file, input_file, output_file,num_files,radio,midle,length)**
* **create_vacants_antiradio_number(probabilities_file, input_file, output_file,num_files,radio,length)** 
* **create_vacants_semiantiradio_number(probabilities_file, input_file, output_file,num_files,radio,midle,length)**
*  **create_vacants_radio(probabilities_file, input_file, output_file,num_files)** 
* **create_vacants_number(probabilities_file, input_file, output_file,num_files,length)** 

#### mu.py

* **compute_mu(filename)**: Given a coordinates file of a nanowire along z, computes the x,y center.

### Inputs <a name = "inputs"></a>

There are two input files.

1. **Json inputs**

   1. **vacants.json:**

      1.  action: Always vacants

      2.  input: The input file of coordinates.

      3.  output: name of the output_file

      4.  probabilities_file: Link to the probabilities file.

      5.  num_files: Number of probabilities of probabilities file.

   2. **vacants_number.json:**

      1.  action: Always vacants

      2.  input: The input file of coordinates.

      3.  output: name of the output_file

      4.  probabilities_file: Link to the probabilities file.

      5.  num_files: Number of probabilities of probabilities file.

      6.  length: length of the nanowire to write for LAMMPS.

   3. **vacants_gauss.json**: 

      1. action: Always vacants gauss

      ​	2. input: The input file of coordinates.

      ​	3. output: name of the output_file

      ​	4. probabilities_file: Link to the probabilities file.

      	5. num_files: Number of probabilities of probabilities file.
      	5. sigma: Standard deviation

   4. **vacants_gauss_number.json:** 

      1. action: Always vacants gauss number

      ​	2. input: The input file of coordinates.

      ​	3. output: name of the output_file

      ​	4. probabilities_file: Link to the probabilities file.

      	5. num_files: Number of probabilities of probabilities file.
      	5. sigma: Standard deviation
      	5. length: length of the nanowire to write for LAMMPS.
      	5. count: Number of times it is accepted.

   5. **vacants_radio_number.json:**

      1.  action: Always vacants radio number
      2. input: The input file of coordinates.
      3. output: name of the output_file
      4.  probabilities_file: Link to the probabilities file.
      5. num_files: Number of probabilities of probabilities file.
      6. radio: The radius of the cylinder.
      7. length: length of the nanowire to write for LAMMPS.

   6. **vacants_radio.json:**

      1. action: Always vacants radio

      ​	2. input: The input file of coordinates.

      ​	3. output: name of the output_file

      ​	4. probabilities_file: Link to the probabilities file.

      ​	5. num_files: Number of probabilities of probabilities file.

   7. **vacants_semiradio_number.json:**

      1.  action: Always vacants semi radio number
      2. input: The input file of coordinates.
      3. output: name of the output_file
      4.  probabilities_file: Link to the probabilities file.
      5. num_files: Number of probabilities of probabilities file.
      6. radio: The thickness of the ring.
      7. distance: Average radius of the ring
      8. length: length of the nanowire to write for LAMMPS.

   8. **vacants_antiradio_number.json:**

      1.  action: Always vacants anti radio number
      2. input: The input file of coordinates.
      3. output: name of the output_file
      4.  probabilities_file: Link to the probabilities file.
      5. num_files: Number of probabilities of probabilities file.
      6. radio: The radius of the cylinder.
      7. length: length of the nanowire to write for LAMMPS.

   9. **vacants_antisemiradio_number.json:**

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

### Execution<a name = "execution"></a>


To execute, write in terminal ``` make  number``` .



## ToDo <a name = "todo"></a>

* Optimise
* Finish readme

## Authors
