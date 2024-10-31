def check_data_type(data):
    if isinstance(data, (int, float, str)):
        print(f"{data} is an individual data type.")
    else:
        print(f"{data} is not an individual data type.")


check_data_type(0)        