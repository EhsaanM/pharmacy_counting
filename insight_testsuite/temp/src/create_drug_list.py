def create_drug_list(drugDict):
    """
    This function receives the dictionary as input and creates a list of tuples. Each tuple contains drug name,
    total cost of the drug, and number of unique prescibers for that drug. It, then, sorts the list based on the
    total cost.
    """
    output_data = list()
    for key in drugDict:
        prescriber_names = drugDict[key][0]
        total_cost = drugDict[key][1]
        if total_cost % 10 == 0:
            total_cost = int(total_cost)
        output_data.append((total_cost,key,len(set(prescriber_names))))
    output_data.sort(reverse=True)
    return output_data