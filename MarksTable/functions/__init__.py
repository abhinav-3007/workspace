from pymongo import MongoClient

connect = MongoClient('localhost', 27017)


def updateRoll(db, repo, name, roll):
    collection = connect[db][repo]
    collection.update_many({"name": name}, {"$set": {"roll": roll}})


def deleteRecord(db, repo, name):
    collection = connect[db][repo]
    collection.delete_one({"name": name})


def insertRecord(db, repo, data):
    collection = connect[db][repo]
    collection.insert_one(data)


def updateListener(db, repo, ):
    collection = connect[db][repo]

    cursor = collection.watch([{'$match': {'operationType': 'update'}}])

    id = []
    with cursor as stream:
        for change in stream:
            id.append(change["documentKey"]["_id"])
    return id


def getData(db, repo, filter):
    collection = connect[db][repo]
    data = collection.find_one(filter)
    return data
