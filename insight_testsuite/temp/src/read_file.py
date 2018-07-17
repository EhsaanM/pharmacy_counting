def read_file(input_file_name):
    """
    This function opens the input file, and passes it the next function to create a dictionary.
    It throws an error in case the file is not found.
    """
    try:
        data = open(input_file_name)
    except FileNotFoundError:
        print('Input file not found!')
        raise SystemExit
    data.readline()
    return data
