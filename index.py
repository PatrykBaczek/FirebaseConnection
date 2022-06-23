from dataclasses import dataclass
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from conn import databaseLink


conn = credentials.Certificate('accountKey.json')

firebase_admin.initialize_app(conn, {
    'databaseURL' : databaseLink
})

def add_new_data(n, s, p):

    data = {
        "Name" : n,
        "Surname" : s,
        "Password" : p
    }

    ref = db.reference('person/' + n)
    ref.set(data)


# def readData():
#     references = db.reference()
#     data = references.get()
#     print(data)

# readData()

# def updateData():
#     references = db.reference()
#     data = references.update({"name" : "Jacek"})


# def deleteData():
#     references = db.reference()
#     data = references.child("age")
#     data.delete()

# updateData()
# readData()
# deleteData()
# readData()

#data example



# reference = db.reference()
# user = reference.set(data)