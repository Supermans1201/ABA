
import os
import json
import GetFilePathRoot
print GetFilePathRoot.get_root_dir()
from pymongo import MongoClient
import csv

def drawpull():
    client = MongoClient()
    i =0
    with open(os.path.join(GetFilePathRoot.get_root_dir(),"data","pulls.csv"),"w") as f:
        ff = csv.writer(f)
        ff.writerow(["name", "count"])
        for name in client.database_names():
            db = client[name]
            if "issue_pull_commit" in db.collection_names():
                ff.writerow([name,str(db["issue_pull_commit"].count())])


def drawfilechanges():
    client = MongoClient()
    i =0
    with open(os.path.join(GetFilePathRoot.get_root_dir(),"data","filechanges.csv"),"w") as f:
        ff = csv.writer(f)
        ff.writerow(["name", "count"])
        for name in client.database_names():
            db = client[name]
            if "filechanges" in db.collection_names():
                ff.writerow([name,str(db["filechanges"].count())])



if __name__ =="__main__":
    # drawpull()
    # drawfilechanges()
    pass


