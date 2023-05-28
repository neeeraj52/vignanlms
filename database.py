from sqlalchemy import create_engine,text
my_secret="mysql+pymysql://obzelc11m8fizde85sua:pscale_pw_iYRsbD3IbCQZf3E1ipvvufAd7Rd4T4YUJG3uLjXlkqq@aws.connect.psdb.cloud/vignanlms?charset=utf8mb4"
engine = create_engine(my_secret,connect_args={
  "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem"
  }
})
with engine.connect() as conn:
  result=conn.execute(text("select * from students"))
  print(result.all())

