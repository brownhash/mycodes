#pre-requisite
#pip install pyyaml
#find data.yml in the same repository

import yaml

stream = open('data.yml', 'r')
data = yaml.load(stream)
name=data.get('data').get('name')
age=data.get('data').get('age')
empstatus=data.get('data').get('emp')

if(empstatus==True):
    print("{} is employed at the age of {}".format(name,age))
else:
    print("{} is not employed at the age of {}".format(name, age))
