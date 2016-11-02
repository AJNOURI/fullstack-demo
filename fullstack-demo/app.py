from flask import Flask
import pymongo
import json

app = Flask(__name__)

# api root dir: nouri.local/api
@app.route('/')
def hello_method():
    uri = "mongodb://127.0.0.1:27017"

    access = pymongo.MongoClient(uri)

    try:
        database = access['fullstack']

        collection = database['credentials']

        # Cursor of 1st document of the collecton
        #usercreds = collection.find({})

        # list comprehension
        users = [i for i in collection.find({})]

        doc_counts = collection.count()

        return "Super FullStack application online: " + str(doc_counts) + " documents"

    except:
        return "Cannot access the db at: " + str(uri)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
