import pymongo

client = pymongo.MongoClient(
  "mongodb+srv://neeraj:Fh778MAlyqBm8t4m@vignanlms.9qfu1wx.mongodb.net/")
db = client["neeraj"]
col = db["students"]
stu = []
for x in col.find():
  stu.append(x)
print(stu)