process_output = {}
time_global = ""
logs = []
def log_handler(filename):
    def log_rotate(filename):
        def process_reader(filename):
            global process_output
            global time_global
            file = open(filename, 'r')
            # logs grabbed line by line
            reader = file.readlines()
            file.close()

            for iterator in reader:
                process_tab = iterator.split(" ")
                month = process_tab[0]
                date = process_tab[1]
                timestamp = process_tab[2]
                time_seperate = timestamp.split(":")
                min = time_seperate[1]
                hour = time_seperate[0]
                if (time_global != hour):
                    time_global = hour
                    process_output[time_global] = []
                    process_name = process_tab[4]
                    temp_name = ""
                    for i in process_name:
                        if (i == "["):
                            break
                        else:
                            temp_name += i
                    process_name = temp_name

                    process_dict = {'month': month, 'date': date, 'time': str(hour) + ":" + str(min),
                                    'process_name': process_name, 'multiples': 0}
                    final_dict = {min + "-" + process_name: process_dict}
                    process_output[time_global].append(final_dict)
                elif (process_output[time_global]):
                    process_name = process_tab[4]
                    temp_name = ""
                    for i in process_name:
                        if (i == "["):
                            break
                        else:
                            temp_name += i
                    process_name = temp_name

                    process_dict = {'month': month, 'date': date, 'time': str(hour) + ":" + str(min),
                                    'process_name': process_name, 'multiples': 0}
                    final_dict = {min + "-" + process_name: process_dict}
                    process_output[time_global].append(final_dict)
                else:
                    process_output[time_global] = []
                    process_name = process_tab[4]
                    temp_name = ""
                    for i in process_name:
                        if (i == "["):
                            break
                        else:
                            temp_name += i
                    process_name = temp_name

                    process_dict = {'month': month, 'date': date, 'time': str(hour) + ":" + str(min),
                                    'process_name': process_name, 'multiples': 0}
                    final_dict = {min + "-" + process_name: process_dict}
                    process_output[time_global].append(final_dict)

        process_reader(filename)

        result = []
        counter_dict = {}
        counter_num = {}
        for i in process_output:
            counter_dict[i] = []
            for j in process_output.get(i):
                for k in j:
                    counter_dict.get(i).append(k)



        for i in counter_dict:
            counter_num[i] = {}
            temp = counter_dict.get(i)
            for j in temp:
                num = temp.count(j)
                counter_num.get(i)[j] = num

        for i in process_output:
            data = counter_num.get(i)
            for j in process_output.get(i):
                for k in j:
                    multiple = data.get(k)
                    j.get(k)['multiples'] = multiple

        for i in process_output:
            for j in process_output.get(i):
                if (j not in result):
                    result.append(j)

        return_data = []

        for i in result:
            for j in i:
                data = i.get(j)
                res = str("{} {} {}\t{}:{}".format(data.get('month'), data.get('date'), data.get('time'),
                                                   data.get('process_name'), data.get('multiples')))
                return_data.append(res)

        for i in return_data:
            data = i.split("\t")
            return_data[return_data.index(i)] = data

        for i in range(0, len(return_data)):
            for j in range(i, len(return_data)):
                if (j != i):
                    if (return_data[i][0] == return_data[j][0]):
                        data = return_data[i][1] + ", " + return_data[j][1]
                        return_data[i][1] = data

        logs = []
        temp = ""
        for i in return_data:
            if (i[0] != temp):
                temp = i[0]
                logs.append(i)
        return (logs)

    data = log_rotate(filename)
    result=[]
    for i in data:
        log = i[0] + "\t" + i[1]
        result.append(log)
    return(result)

import time

while(True):
    get = log_handler('process.log')
    for i in get:
        if(i not in logs):
            logs.append(i)
            print(i)
    time.sleep(2)