import pymongo

client = pymongo.MongoClient(
  "mongodb+srv://neeraj:Fh778MAlyqBm8t4m@vignanlms.9qfu1wx.mongodb.net/")
db = client["attendence"]
col = db["3yeareeea"]