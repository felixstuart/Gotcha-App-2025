import firebase_admin

import os

import json

from firebase_admin import credentials, firestore

cred = credentials.Certificate("./Felix's Gotcha Test Firebase Service Account.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

f = open('gotcha_data.json', 'r')

docs = json.loads(f.read())

for doc in docs:

    id = doc.pop('id', None)

    if id:

        db.collection("data").document(id).set(doc, merge=True)

    else:

        db.collection("data").add(doc)
