#!pip install firebase_admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
serviceAccountKey_json_file = "firestore.json"
cred = credentials.Certificate(serviceAccountKey_json_file)
firebase_admin.initialize_app(cred)

db = firestore.client()

# CREATING DATA TO THE CLOUD FIRESTORE

# auto ids allow us to create duplicate data over an over if we re-run it documents with auto IDs
data = dict(name="John", age=40, employed=True)
db.collection("people").add(data)

# Add documents with auto IDs
data = dict(name="John", age=40, employed=True)
db.collection("people").add(data)

# Set documents with auto IDs
data = dict(name="Jane David", age=32, employed=False)
db.collection("people").document().set(data) # doc_name is not passed here.. so auto IDs


# Set documents with known IDs
data = dict(name="Jane Doe", age=40, employed=False)
id_no = 1  # use for loop in seriious projects
doc_name = str(id_no).zfill(4) + "_" + (data['name']).lower().replace(" ", "_") # just setting doc_name like 0001_name_etc
db.collection("people").document(doc_name).set(data)  # adding document to collection with document reference

db.collection("people").document(doc_name).set(data, merge=True) 

# Merging data or update sometimes
data = dict(address="#566, 24th Avenue, Ist Main, Bengalore", age=60) # earlier age of Jane Doe was 40 now changeing it 60
db.collection("people").document(doc_name).set(data, merge=True) 
# using same doc_name from Jane Doe section of set doc with known ids

# adding movies which Jane Doe watched |  ==== Collection inside a document
# use add for autoIds or set for our own ids for movies, here i use unique ids
data = dict(name="Avengers")
db.collection("people").document(doc_name).collection("movies").document("001_Avengers").set(data)

data = dict(name="Harry Potter")
db.collection("people").document(doc_name).collection("movies").document("002_Harry_Potter").set(data)

# getting a document with a known ID (not generated Ids)
result = db.collection("people").document(doc_name).get()
if result.exists:
    print(result.to_dict())

docs = db.collection("people").get()
for doc in docs:
    print(doc.to_dict())

# getting all documents in a collection
docs = db.collection("people").get()
for doc in docs:
    print(doc.to_dict())

# QUERYING - where, 
# equal - work with integer, float 
docs = db.collection("people").where("age", "==", 40).get() # where
for doc in docs:
    print(doc.to_dict())

# equal - work with integer, float 
docs = db.collection("people").where("age", "==", 40).get() # where

for doc in docs:
    print(doc.to_dict())

# greater than - work with only integers 
docs = db.collection("people").where("age", ">", 40).get() # where
for doc in docs:
    print(doc.to_dict())

# same way use == != > < >= <=
docs = db.collection("people").where("name", "==", "John").get() # where
for doc in docs:
    print(doc.to_dict())

# equal - work with strings 
docs = db.collection("people").where("name", "==", "John").get() # where
for doc in docs:
    print(doc.to_dict())

# array search
docs = db.collection("people").where("socials", "array_contains", "YouTube").get() # where
for doc in docs:
    print(doc.to_dict())

# array search
docs = db.collection("people").where("socials", "array_contains", "YouTube").get() # where
for doc in docs:
    print(doc.to_dict())

# IN OPERATOR
docs = db.collection("people").where(
    "address", "in", ["#566, 24th Avenue, Ist Main, Bengalore", "Africa"] # this shoudl be an array for IN to work
).get() # where in

for doc in docs:
    print(doc.to_dict())