def data_list(file):

    with open(file) as f:
        data = []
        for line in f:
            str_data = line.split()
            data.append((str_data[0], str_data[5].strip('"'), str_data[6]))
    print(data)

data_list("data.txt")
