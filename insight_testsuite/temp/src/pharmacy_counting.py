"""
Pharmacy Counting (Insight Data Engineering)

@author: Ehsan Mirzaei
contact: emirzae@g.clemson.edu
"""
import sys

def main():
    from read_file import read_file
    from create_drug_dict import create_drug_dict
    from create_drug_list import create_drug_list
    from write_to_file import write_to_file
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_data = read_file(input_file)        # reads the input file
    drugDict = create_drug_dict(input_data)                   # creates a dictionary from the input data
    output_data = create_drug_list(drugDict)                  # creates a list of tuples from the dictionary
    write_to_file(output_data, output_file)     # writes the output file to disk


if __name__ == '__main__':
    main()