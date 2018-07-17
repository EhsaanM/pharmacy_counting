def create_drug_dict(input_data):
    """ 
    This function creates a dictionary using the drug names as keys. The values corresponding to each key is 
    a list consisting of another list of last name, first name tuples and the total cost of the drug.
    """
    from add_update_dict import add_update_dict
    drugDict = dict()
    for line in input_data:
        line_list = line.strip().split(',')     # breaks each line into a list of words using ',' as delimiter
        drugDict = add_update_dict(drugDict,line_list) 

    input_data.close()
    return drugDict