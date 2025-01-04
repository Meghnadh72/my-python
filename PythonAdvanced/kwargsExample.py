""" def sample_method(**kwargs):
    print(getFullName(**kwargs))

def getFullName(surname="", firstName="", last_name=''):
    return surname + " " + firstName + " " + last_name

sample_method(firstName="Ram Sai", last_name="Meghnadh")

 """

import boto3
c = boto3.client('lambda', region_name='us-east-1')
print(type(c))