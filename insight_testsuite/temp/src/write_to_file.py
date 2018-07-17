def write_to_file(output_data,output_file_name):
    """
    This function receives the output data as a list of tuples and writes them to file.
    """
    file = open(output_file_name, 'w')
    file.write('drug_name,num_prescriber,total_cost')
    for i in range(len(output_data)):
        total_cost = output_data[i][0]
        drug_name = output_data[i][1]
        num_prescribers = output_data[i][2]                  
        file.write('\n'+drug_name+','+str(num_prescribers)+','+str(total_cost))

    file.close()