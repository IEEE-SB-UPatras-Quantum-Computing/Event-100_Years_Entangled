with open("data.txt", "r") as f:
        data_list = []      
        for item in f:
            data_list.append(item.rstrip())
        # mydata = ''.join(map(str, data_list))
        mydata=' '.join(data_list)
        # print(mydata)
        c = "{:07s}".format
        bit_data=[c(item) for item in mydata]
        print(bit_data)
        print(mydata)

