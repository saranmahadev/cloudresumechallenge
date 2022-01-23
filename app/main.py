from flask import Flask, request
import pymongo
from uuid import uuid4
import os

app = Flask(__name__)

class Db:
    def __init__(self) -> None:        
        self.client = pymongo.MongoClient(os.environ['MONGO_URI'])
        self.db=self.client.get_database("countDatabase")
        self.collection = self.db.get_collection("countCollection")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

    def get_count(self) -> int:
        return self.collection.count_documents({})
    
    def insert_view(self,view: dict) -> dict:
        self.collection.insert_one({
            "_id": uuid4().hex,
            "ip": view["ip"],
            "timestamp": view["timestamp"],
            "country": view["country"],
            "city": view["city"]            
        })
        
        return {
            "status": "success",
            "message": "View inserted",
            "code": 200
        }

@app.route('/add')
def hello():
    try:
        with Db() as db:
            if(db.insert_view(request.json)["code"] == 200):
                return {
                    "status": "success",
                    "message": "View inserted",
                    "code": 200
                }
            else:
                return {
                    "status": "fail",
                    "message": "View already exists",
                    "code": 400
                }
    except Exception as e:
        return {
            "status": "fail",
            "message": "Something went wrong",
            "code": 500
        }

@app.route('/count')
def count():
    try:
        with Db() as db:
            return {
                "status": "success",
                "message": "Views count",
                "code": 200,
                "count": db.get_count()
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "code": 500
        }

if __name__ == '__main__':
    app.run()