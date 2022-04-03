def data_list(file):

    with open(file) as f:
        data = []
        spam_dict = {}
        for line in f:
            str_data = line.split()
            data.append((str_data[0], str_data[5].strip('"'), str_data[6]))
            spam_dict.setdefault(str_data[0], 0)
            spam_dict[str_data[0]] += 1
        spam_dict = sorted(spam_dict.items(), key= lambda x: x[1], reverse=True)
    print(spam_dict[0:5])


data_list("data.txt")