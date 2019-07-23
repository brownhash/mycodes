import time

def log_reader(filename):
    process_output = []
    logs = []
    messages = []

    reader = open(filename,'r')
    reader_data = reader.readlines()
    reader.close()

    for i in reader_data:
        data = i.split(" ")
        temp_data = []

        # month
        temp_data.append(data[0])
        # date
        temp_data.append(data[1])
        # time
        time = data[2].split(":")
        temp_data.append(str(time[0])+":"+str(time[1]))
        # process name
        process = data[4].split("[")
        temp_data.append(process[0])

        process_output.append(temp_data)

    for i in process_output:
        if (len(messages) == 0):
            messages.append(i)
        else:
            date = messages[len(messages) - 1][1]
            time = messages[len(messages) - 1][2]
            if ((i[1] == date) and (i[2] == time)):
                messages[len(messages) - 1][3] += str(" " + i[3])
            else:
                messages.append(i)

    for i in range(0, len(messages)):
        temp = []
        processes = messages[i][3].split(" ")
        for j in processes:
            num = processes.count(j)
            if ((str(j) + ":" + str(num)) not in temp):
                temp.append(str(j) + ":" + str(num))
        mess = ""
        for j in temp:
            mess += str(j) + ", "
        messages[i][3] = mess
        temp_data = ("{} {} {}\t{}".format(messages[i][0], messages[i][1], messages[i][2], messages[i][3]))
        if (temp_data not in logs):
            logs.append(temp_data)
    return(logs)

log_messages=[]
while(True):
    for i in log_reader('process.log'):
        if(i not in log_messages):
            log_messages.append(i)
            print(i)
    time.sleep(2)