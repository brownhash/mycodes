import sys
import time

class check:

    def check(self, data):
        percent = 0
        nums = []
        names = []
        for i in data:
            try:
                num = int(data.get(i))
                nums.append(num)
                names.append(i)
                if (percent < 100):
                    percent += num
                    if (percent > 100):
                        print("Error in data, % data cannot be greter than 100\n")
                        print("Sum of {} -> {} is greter than 100".format(names, nums))
                        sys.exit()
            except Exception as error:
                print("Error in data:\n", error)


class horizontal_graphs:

    def __init__(self):
        message="#  Horizontal Graph Representation  #"
        print("\n\n")
        print("#"*len(message))
        print(message)
        print("#" * len(message)+"\n")

    def data_represent(self, data, design):

        writer = open('graph_out.txt', 'a')
        writer.write("----------------------------------------------------------\n")
        writer.write(time.strftime("%d/%m/%y - %H:%M:%S")+"\n")
        writer.write("----------------------------------------------------------\n")
        writer.close()

        if (len(design) > 1):
            print("Error, design cannot take more than 1 char. Given {} >> {} << ".format(len(design), design))
            sys.exit()

        def represent(data, design):

            check().check(data)

            lon = ""
            for i in data:
                if (len(str(i)) > len(lon)):
                    lon = str(i)

            seperator = len(lon) * 2

            errors = []
            total = 0
            for i in data:
                head = i
                num = data.get(i)
                if (num > 100):
                    errors.append("Error! %data cannot be greter than 100. input - {} for {}".format(num, head))
                else:
                    rep = str(head) + " " * (seperator - len(str(i))) + (design * int(num)) + " ({})".format(num)
                    print(rep)
                    writer = open('graph_out.txt','a')
                    writer.write(rep+"\n")
                    writer.close()
                    total += int(num)

            for i in errors:
                print(i)

            left = 100 - int(total)
            if (left > 0):
                print("\nCovered - {} %".format(total))
                print("Left - {} %".format(left))

                writer = open('graph_out.txt', 'a')
                writer.write("\nCovered - {} %\n".format(total))
                writer.write("Left - {} %\n".format(left)+"\n")
                writer.close()

        represent(data, design)

class vertical_graphs:
    def __init__(self):
        message="#  Vertical Graph Representation  #"
        print("\n\n")
        print("#"*len(message))
        print(message)
        print("#" * len(message)+"\n")

    def data_represent(self, data, design):

        writer = open('graph_out.txt', 'a')
        writer.write("----------------------------------------------------------\n")
        writer.write(time.strftime("%d/%m/%y - %H:%M:%S") + "\n")
        writer.write("----------------------------------------------------------\n")
        writer.close()

        if (len(design) > 1):
            print("Error, design cannot take more than 1 char. Given {} >> {} << ".format(len(design),design))
            sys.exit()

        graph = {100:[],90:[],80:[],70:[],60:[],50:[],40:[],30:[],20:[],10:[]}

        def represent(data, design):
            design = design*2
            check().check(data)
            fields = {}
            lon = ""

            for i in data:
                if(len(str(i)) > len(lon)):
                    lon = str(i)
                percent_data = int(data.get(i))
                if(percent_data/10 > percent_data//10):
                    fields[i] = (percent_data//10)+1
                else:
                    fields[i] = percent_data // 10

            total = 0
            for i in graph:
                var = int(i/10)
                d= ""
                for j in fields:
                    bar_len = int(fields.get(j))
                    if(bar_len >= var):
                        d = design
                    elif(var == bar_len+1):
                        d = str(data.get(j))
                        total += data.get(j)
                        if(len(d) < 2):
                            d = "0"+d
                    else:
                        d = "  "
                    space = len(j) + 2
                    format = (" " * space) + d
                    graph.get(i).append(format)

            for i in graph:
                if(i!=100):
                    s = " "+str(i)
                else:
                    s = str(i)
                for i in graph.get(i):
                    s += i
                print(s)
                writer = open('graph_out.txt', 'a')
                writer.write(s+"\n")
                writer.close()

            names = "   "
            for i in fields:
                space = len(i) + 2
                names += (" "*(space-len(str(i))))+(" "*len(design))+str(i)
            print(names)
            writer = open('graph_out.txt', 'a')
            writer.write(names + "\n")
            writer.close()

            left = 100 - int(total)
            if (left > 0):
                print("\nCovered - {} %".format(total))
                print("Left - {} %".format(left))

                writer = open('graph_out.txt', 'a')
                writer.write("\nCovered - {} %\n".format(total))
                writer.write("Left - {} %\n".format(left)+"\n")
                writer.close()

        represent(data, design)


data = {
    'Uttar Pradesh':16,
    'Maharashtra':9,
    'Bihar':8,
    'West Bengal':7,
    'Madhya Pradesh':6,
    'Tamil Nadu':6,
    'Rajasthan':6,
    'Karnataka':5,
    'Gujarat':5,
    'Andhra Pradesh':4,
    'Odisha':3,
    'Telangana':3
}

horizontal_graphs().data_represent(data,"~")
vertical_graphs().data_represent(data,"|")
