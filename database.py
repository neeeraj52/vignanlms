import pymongo
if __name__ == "__main__":
  client = pymongo.MongoClient(
    "mongodb+srv://neeraj:Fh778MAlyqBm8t4m@vignanlms.9qfu1wx.mongodb.net/")
  db = client["neeraj"]
  col = db["students"]
  doc = {"SNAME": "VINAY", "ROLL NO": "20891AO225"}
  col.insert_one(doc)
