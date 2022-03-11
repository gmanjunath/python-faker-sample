from json import dumps
from faker import Faker
import collections
import json
import random
import datetime

import radar 


#recordClassification=["OFFICIAL","OFFICIAL SENSITIVE","SECRET","TOP SECRET"]
recordClassification=["OFFICIAL","OFFICIAL SENSITIVE"]
auditType= ["MACHiNE", "AUTH", "TRANS", "CDDP"]
#auditType= ["MACHiNE", "AUTH"]
metaSecurityRole = ["Admin Only","Role 1","Role 2","Role 3","Role 4","Role 5","Role 6 Restricted"]
unauthorisedAuditViewer = ["Mike", "Caesar", "Clarke", "Steve", "Anita"]
authorisedAuditViewer = ["John", "Sam", "Adam", "Ian", "Andrew", "Maria"]
applicationIdentifier = ["MySQL", "Ignix", "ElasticSearch", "DHCP Audit", "MYSQL Audit", "Data Ingestion"]
#applicationIdentifier = ["MySQL", "Ignix", "ElasticSearch"]
#device = ['windows', 'linux', 'MacOS']
device = ['Windows', 'MacOS']
loggin_options = ['in', 'out']

def fake_person_generator(length, fake):
    for x in range(length):  # xrange in Python 2.7
        yield {'last_name': fake.last_name(),
               'first_name': fake.first_name(),
               'street_address': fake.street_address(),
               'email': fake.email(),
               'index': x}

def createtimestamp():
    dummy_time = fake.date_time()
    dummy_time.strftime("%Y-%m-%dX%H:%M:%S.000-0000 %z")
    return str(dummy_time)


def fake_person_generator_json_schema(length, fake):
    for x in range(length):  # xrange in Python 2.7
        yield  {"iasAuditEntry": {
                    "iasAuditHeader": {
                        "iasAuditRecordDate": "2013-03-24T23:59:34",
                        "iasClientIdentifier": fake.last_name(),
                        "iasApplicationIdentifier": random.choice(applicationIdentifier),
                        "iasAuditType": random.choice(auditType),
                        "iasAuditSessionID": ("iasAuditSessionID" + str(x)),
                        "iasOrganisationalUnit": fake.company(),
                        "iasAuditID": str(x),
                        "iasAuditMetadata":{
                            #"iasMetaDate":str(radar.random_datetime(start='2021-01-24', stop='2021-05-24T23:59:59')),
                            "iasMetaData":createtimestamp(),
                            "iasMetaType": ("iasMetaType" + str(x)),
                            "iasMetaSecurityRole": random.choice(metaSecurityRole),
                            "iasMetaSecurityViewer": {
                                "iasAuditRecordViewer" : {
                                    "unauthorisedAuditViewer": random.choice(unauthorisedAuditViewer),
                                    "authorisedAuditViewer": random.choice(authorisedAuditViewer)
                                },
                            },
                            "iasMetaClassification": {
                                "iasDataClassification": {
                                    "iasAuditRecordClassifaction": random.choice(recordClassification),
                                }
                            },  
                            # "iasMetaDataPayload": ( "\"" + "user:" +  "\'" + "\'"  + str(random.choice (authorisedAuditViewer)) + "\'" + 
                            #                           " log: " + random.choice(loggin_options) + " into " + random.choice (device)),
                            "iasMetaDataPayload" : ("user : Matt"),
                            "iasMetaRetension": ("iasMetaRetension" + str(x)),
                        },
                    },
            }
        }                 
            
database = []
filename = 'H1'
length   = 50
fake     = Faker() # <--- Forgot this
fpg = fake_person_generator_json_schema(length, fake)
# with open('%s.json' % filename, 'w') as output:
#     output.write('[')  # to made json file valid according to JSON format
#     for person in fpg:
#         json.dump(person, output)
#     output.write(']')  # to made json file valid according to JSON format
# print ("Done.")
print(radar.random_datetime(start='2013-03-24T23:59:34', stop='2013-05-24T23:59:59'))
dummy_time = fake.date_time()
dummy_time.strftime("%Y-%m-%dT%H:%M:%S.000-0000")
print(dummy_time)
i = 0
for person in fpg:
    i = i + 1 
    with open('%s.json' % (filename+str(i)), 'w') as output:
        output.write('[') 
        json.dump(person, output)
        output.write(']\n')  # to made json file valid according to JSON format