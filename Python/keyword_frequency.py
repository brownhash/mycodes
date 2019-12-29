#input the keywords as lists
#input the data in any form

class keyword_frequency:

    def frequency(self,keywords,data):
        frequency_list=[]
        for iterator in keywords:
            data=str(data)
            data2=data.split(str(iterator))
            frequency_list.append(len(data2)-1)

        return (frequency_list)
