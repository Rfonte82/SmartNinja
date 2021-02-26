import pymongo

#Connect to Engine
connection = pymongo.MongoClient('localhost',27017)
#print(connection)
#Create Database
database = connection['myoffice']
#Create Collection
colletion = database['mydoc']


#data={'Type':"fact1"}
#colletion.insert_one(data)


def insert_data(data):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    document = collection.insert_one(data)
    return document.inserted_id