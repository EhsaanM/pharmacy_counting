# Project Title
Pharmacy Counting (Insight Data Engineering)

# Problem
Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name. 

# Approach
Python 3.6.3 is used to solve the problem. `pharmacy_counting.py` is the main file that calls the other functions and generates the output file. It, first, calls the `read_file.py` which opens the input data file and then sends it to `create_drug_dict.py`. This file reads the input data line by line and calls `add_update_dict.py` to create a dictionary called drugDict using drug names as keys and a list contaning names of all the prescribers as well as total cost of the drug as the value corresponding to each key. The dictionary created by this file looks like:
```
drugDict = {'AMBIEN':[[('Smith','James'),('Garcia','Maria')],300],
		'CHLORPROMAZINE':[[('Johnson','James'),('Rodriguez','Maria')],3000],
		'BENZTROPINE MESYLATE':[[('Smith','David')],1500]}
```
After the dictionary is created, it is read by the `create_drug_list.py` to create a list of tuples each containing the total drug cost, name of the drug and number of unique prescribes for that specific drug. Here is the output of this file:
```
output_data = [(3000,'CHLORPROMAZINE',2),
			   (1500,'BENZTROPINE MESYLATE',1),
			   (300,'AMBIEN',2)]
```
The list is sorted based on the total drug cost in descending order, and in case of a tie based on the drug name.
Then, the `write_to_file.py` writes the results to a text file as specified in the description of the problem.
`run.sh` runs the programs. It reads the input file from the `input` folder and writes the output file to the `output` directory.