import pymongo

client = pymongo.MongoClient(
  "mongodb+srv://neeraj:Fh778MAlyqBm8t4m@vignanlms.9qfu1wx.mongodb.net/")
db = client["marks"]
col = db["3yeareee" + "dppm"]
x = col.delete_many({})
print(x.deleted_count)
