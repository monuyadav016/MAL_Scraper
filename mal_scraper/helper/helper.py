import json
import pymongo

def get_remaining_id_list(db_name, col_name, filename):
    id_list = []
    collection = None
    client = pymongo.MongoClient()
    try:
        # if db_name in client.list_database_names():
        #     db = client[db_name]
        #     if col_name in db.list_collection_names():
        #         collection = db[col_name]
        db = client[db_name]
        collection = db[col_name]
        if collection is not None:
            with open(filename, "r") as id_file:
                id_list = json.load(id_file)
            db_list = collection.find({}, {"_id":1})
            for anime in db_list:
                mal_id = anime["_id"]
                found = False
                for _id in id_list:
                    if mal_id == _id["mal_id"]:
                        id_list.remove(_id)
        return id_list
    except Exception as e:
        print(e)
    finally:
        client.close()
        return id_list