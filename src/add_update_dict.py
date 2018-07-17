def add_update_dict(drugDict,line_list):
    """
    This function adds to/updates the dictionary created in the create_dict.py file. It receives each line of the 
    input file as a list and checks to see if the drug is already in the dictionary. If yes, it updates the dictionary
    by adding prescriber's name and drug cost. Otherwise, it adds the line to the dictionary.
    """
    drug_name = line_list[3]
    drug_cost = line_list[-1]
    prescriber_last_name = line_list[1]
    prescriber_first_name = line_list[2]
    if drug_name in drugDict:
            drugDict[drug_name][1] += float(drug_cost)
            drugDict[drug_name][0].append((prescriber_last_name,prescriber_first_name))
    else:
        drugDict[drug_name] = [[(prescriber_last_name,prescriber_first_name)],float(drug_cost)]
    return drugDict